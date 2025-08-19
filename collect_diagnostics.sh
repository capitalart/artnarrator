#!/usr/bin/env bash
# Safe, verbose diagnostics collector (no hard fail on missing bits)
set -u
set -o pipefail

cd ~/artnarrator.com 2>/dev/null || cd "$(pwd)"

TS="$(date +%Y-%m-%d_%H-%M-%S)"
OUT="diagnostics/diag-$TS"
mkdir -p "$OUT"

echo "== System ==" > "$OUT/00_sys.txt"
{
  date -Is
  whoami
  uname -a
  command -v python3 || true
  python3 --version || true
  command -v pip || true
  pip --version || true
  [ -d venv ] && echo "venv exists: $(realpath venv)" || echo "venv: MISSING"
} >> "$OUT/00_sys.txt" 2>&1

echo "== Git ==" > "$OUT/01_git.txt"
{
  git rev-parse --show-toplevel 2>/dev/null || echo "(not a git repo?)"
  git status -sb || true
  git log --oneline -n 15 || true
  git rev-parse HEAD || true
  git config --get remote.origin.url || true
  echo -e "\n--- .gitignore ---"
  [ -f .gitignore ] && sed -n '1,200p' .gitignore || echo "(no .gitignore)"
} >> "$OUT/01_git.txt" 2>&1

echo "== .env (keys only, values masked) ==" > "$OUT/02_env.txt"
{
  if [ -f .env ]; then
    awk -F= '
      /^[[:space:]]*#/ || NF==0 {next}
      {
        key=$1; sub(/[[:space:]]+$/, "", key);
        val=$0; sub(/^[^=]+=/, "", val);
        n=length(val);
        printf "%s=%s (len:%d)\n", key, (n>0?"***":"<empty>"), n
      }
    ' .env
  else
    echo ".env not found"
  fi
} >> "$OUT/02_env.txt" 2>&1

echo "== config.py effective values ==" > "$OUT/03_config_effective.txt"
python3 - <<'PY' >> "$OUT/03_config_effective.txt" 2>&1
try:
    import config, os
    fields = [
        "ENVIRONMENT","BASE_DIR","ART_PROCESSING_DIR",
        "UNANALYSED_ROOT","PROCESSED_ROOT","LOGS_DIR",
        "ANALYZE_SCRIPT_PATH","AUTO_ANALYZE_ON_UPLOAD"
    ]
    for f in fields:
        print(f"{f}:", getattr(config, f, None))
    print("FLASK_SECRET_KEY set?:", bool(getattr(config,"FLASK_SECRET_KEY",None)))
    print("OPENAI_API_KEY set?:", bool(os.getenv('OPENAI_API_KEY')))
except Exception as e:
    print("ERROR importing config:", e)
PY

echo "== Flask routes ==" > "$OUT/04_routes.txt"
python3 - <<'PY' >> "$OUT/04_routes.txt" 2>&1
try:
    from app import app
    rules = sorted([(r.rule, ",".join(sorted(r.methods)), r.endpoint) for r in app.url_map.iter_rules()])
    for rule, methods, ep in rules:
        print(f"{rule:45}  {methods:25}  -> {ep}")
except Exception as e:
    print("ERROR introspecting routes:", e)
PY

echo "== Trees (art-processing, key folders) ==" > "$OUT/05_tree.txt"
{
  if command -v tree >/dev/null 2>&1; then
    tree -a -L 3 art-processing || true
  else
    echo "(tree not installed, using find)"
    find art-processing -maxdepth 3 -print 2>/dev/null || true
  fi
  echo
  [ -d logs ] && { echo "logs/:"; ls -la logs | sed -n '1,200p'; } || echo "logs/ (missing)"
  echo
  [ -d outputs ] && { echo "outputs/:"; ls -la outputs | sed -n '1,200p'; } || echo "outputs/ (missing)"
} >> "$OUT/05_tree.txt" 2>&1

echo "== Queue + sessions + recent app logs ==" > "$OUT/06_queues_logs.txt"
{
  for f in \
    "art-processing/processed-artwork/pending_mockups.json" \
    "art-processing/pending_mockups.json" \
    "logs/session_registry.json"
  do
    echo "--- $f ---"
    [ -f "$f" ] && sed -n '1,300p' "$f" || echo "(missing)"
    echo
  done

  echo "--- recent app logs (composites/gunicorn/other) ---"
  for log in logs/*.log ; do
    [ -f "$log" ] || continue
    echo "### $log"
    tail -n 200 "$log"
    echo
  done
} >> "$OUT/06_queues_logs.txt" 2>&1

echo "== SQLite schema (users, login_attempts) ==" > "$OUT/07_db.txt"
{
  DB="data/artnarrator.sqlite3"
  if command -v sqlite3 >/dev/null 2>&1 && [ -f "$DB" ]; then
    echo "-- .tables --"
    sqlite3 "$DB" ".tables" || true
    echo
    for t in users login_attempts ; do
      echo "-- schema: $t --"
      sqlite3 "$DB" ".schema $t" || echo "(no table $t)"
      echo "-- pragma table_info($t) --"
      sqlite3 "$DB" "PRAGMA table_info($t);" || true
      echo "-- count($t) --"
      sqlite3 "$DB" "SELECT COUNT(*) FROM $t;" || true
      echo
    done
  else
    echo "sqlite3 not installed or DB missing ($DB)"
  fi
} >> "$OUT/07_db.txt" 2>&1

echo "== Python environment & packages ==" > "$OUT/08_python.txt"
{
  python3 - <<'PY'
import sys, platform
print("executable:", sys.executable)
print("version:", sys.version)
print("platform:", platform.platform())
PY
  echo
  echo "-- pip freeze (sorted) --"
  (pip freeze 2>/dev/null | sort) || echo "(pip freeze failed)"
} >> "$OUT/08_python.txt" 2>&1

echo "== Services & ports ==" > "$OUT/09_services_ports.txt"
{
  PORT="${PORT:-8000}"
  echo "-- systemctl status (artnarrator / telemetry) --"
  (systemctl status artnarrator --no-pager | sed -n '1,120p') 2>&1 || echo "(no systemd unit: artnarrator)"
  echo
  (systemctl status telemetry --no-pager | sed -n '1,120p') 2>&1 || echo "(no systemd unit: telemetry)"
  echo
  echo "-- listening ports (8000, 5055) --"
  (ss -ltnp 2>/dev/null | egrep '(:8000|:5055)') || echo "(no listeners on 8000/5055)"
  echo
  echo "-- disk space summary --"
  df -h .
} >> "$OUT/09_services_ports.txt" 2>&1

echo "== Analyze CLI presence ==" > "$OUT/10_analyze_cli.txt"
{
  python3 - <<'PY'
try:
    import config
    print("ANALYZE_SCRIPT_PATH:", getattr(config, "ANALYZE_SCRIPT_PATH", None))
except Exception as e:
    print("ERROR importing config:", e)
PY
  ANP=$(python3 - <<'PY'
import config, sys
p = getattr(config, "ANALYZE_SCRIPT_PATH", None)
print(p if p else "")
PY
)
  if [ -n "$ANP" ] && [ -f "$ANP" ]; then
    echo "-- head of analyze script --"
    sed -n '1,60p' "$ANP" || true
  else
    echo "analyze script missing or path unresolved: $ANP"
  fi
} >> "$OUT/10_analyze_cli.txt" 2>&1

echo "== HTTP health checks ==" > "$OUT/11_health.txt"
{
  PORT="${PORT:-8000}"
  for URL in \
    "http://127.0.0.1:${PORT}/healthz" \
    "http://127.0.0.1:${PORT}/health" \
    "http://localhost:${PORT}/health" \
    "http://127.0.0.1/health"
  do
    echo "-- $URL --"
    code=$(curl -s -o /dev/null -w "%{http_code}" "$URL" || echo "ERR")
    echo "HTTP $code"
  done
} >> "$OUT/11_health.txt" 2>&1

echo "== Summary ==" > "$OUT/12_summary.txt"
{
  echo "Snapshot: $OUT"
  echo "Created:  $(date -Is)"
  echo
  echo "Key paths:"
  python3 - <<'PY'
try:
    import config
    print("UNANALYSED_ROOT:", getattr(config,"UNANALYSED_ROOT", None))
    print("PROCESSED_ROOT:", getattr(config,"PROCESSED_ROOT", None))
    print("PENDING_MOCKUPS:", getattr(config,"PROCESSED_ROOT", None), "/pending_mockups.json", sep="")
except Exception as e:
    print("ERROR importing config:", e)
PY
} >> "$OUT/12_summary.txt" 2>&1

# Tarball for easy sharing
tar -czf "$OUT.tar.gz" -C diagnostics "diag-$TS" 2>/dev/null || true

echo "== COMPLETE =="
echo "Saved to: $OUT/"
[ -f "$OUT.tar.gz" ] && echo "Bundle:  $OUT.tar.gz"
