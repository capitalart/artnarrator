#!/bin/bash
# ======================================================================================
# PROJECT TOOLKIT (ROBBIE MODE™ - Gemini Enhanced Edition)
# AUTHOR: Robin Custance & Gemini Assistant (2025-08-17)
# PURPOSE: Manage Git workflows, testing, auditing, backups, log snapshots, and services
# ======================================================================================

set -euo pipefail

# --- Force .env to load for ALL subprocesses, if it exists ---
if [ -f .env ]; then
  set -a
  source .env
  set +a
fi

# ======================================================================================
# SECTION 1: CONFIGURATION
# ======================================================================================
readonly LOG_DIR="logs"
readonly INCLUDES_FILE="backup_includes.txt"
readonly CODESTACK_SCRIPT="code-stacker.sh"
mkdir -p "$LOG_DIR"

readonly LOG_FILE="$LOG_DIR/project-toolkit-$(date +'%Y-%m-%d_%H-%M-%S').log"
readonly DEFAULT_BRANCH="${DEFAULT_BRANCH:-main}" # Default to 'main' if not in .env

# ======================================================================================
# SECTION 2: LOGGING FUNCTIONS
# ======================================================================================
log() {
  local level="$1"; shift
  local color;
  case "$level" in
    SUCCESS) color="\033[1;32m" ;; # Green
    ERROR)   color="\033[1;31m" ;; # Red
    WARN)    color="\033[1;33m" ;; # Yellow
    INFO)    color="\033[1;36m" ;; # Cyan
    *)       color="\033[0m"   ;; # Reset
  esac
  # Log to both stdout and the toolkit's log file
  echo -e "${color}[${level}]$(tput sgr0) $*" | tee -a "$LOG_FILE"
}

# Function to terminate the script on critical failure
die() {
  log ERROR "$*"
  echo -e "\n[ABORTED] Critical error occurred. See log for details: $LOG_FILE"
  exit 1
}

# ======================================================================================
# SECTION 3: CORE WORKFLOWS
# ======================================================================================
# A full workflow: check, test, stack, backup, push, and restart
full_push() {
  log INFO "Running [FULL PUSH] workflow..."
  health_and_deps_check
  run_full_test_suite
  run_code_stack
  local_backup
  safe_git_push
  restart_service
  log SUCCESS "[FULL PUSH] workflow completed successfully."
}

# Safely add, commit, and push changes to the default branch
safe_git_push() {
  log INFO "Committing and pushing to branch: '$DEFAULT_BRANCH'..."
  git add .
  # Check if there are changes to commit
  if git diff --staged --quiet; then
    log WARN "No changes to commit."
  else
    git commit -m "Toolkit push on $(date '+%Y-%m-%d %I:%M %p')"
    log SUCCESS "Changes committed."
  fi
  git push origin "$DEFAULT_BRANCH"
  log SUCCESS "Git push to '$DEFAULT_BRANCH' successful."
}

# ======================================================================================
# SECTION 4: BACKUPS
# ======================================================================================
# Create a local backup using a predefined list of files/folders
local_backup() {
  local timestamp
  timestamp=$(date "+%a-%d-%b-%Y-%I-%M-%p")
  local tarball="backups/local_backup_${timestamp}.tar.gz"
  mkdir -p backups
  [[ -f "$INCLUDES_FILE" ]] || die "Backup includes file not found: '$INCLUDES_FILE'"
  tar czf "$tarball" -T "$INCLUDES_FILE"
  log SUCCESS "Local backup created: $tarball"
}

# Manually trigger the cron backup script for a live backup
run_actual_backup() {
  log INFO "Running ACTUAL cloud backup (manual trigger)..."
  if [[ -x "./cron-backup.sh" ]]; then
    ./cron-backup.sh || log ERROR "The actual backup script failed."
  else
    log ERROR "'cron-backup.sh' not found or is not executable."
  fi
}

# Manually trigger the cron backup script for testing purposes
run_cron_backup_simulation() {
  log INFO "Running cron backup simulation (manual trigger)..."
  if [[ -x "./cron-backup.sh" ]]; then
    # Execute with dry-run flag for safety in the toolkit
    ./cron-backup.sh --dry-run || log ERROR "Cron backup script simulation failed."
  else
    log ERROR "'cron-backup.sh' not found or is not executable."
  fi
}

# ======================================================================================
# SECTION 5: TESTING & QA
# ======================================================================================
# Perform health checks and verify dependencies
health_and_deps_check() {
  log INFO "Running system health and dependency checks..."
  [[ -d venv ]] || die "Python virtual environment 'venv' not found."
  source venv/bin/activate || die "Failed to activate Python venv."
  pip check || log WARN "Pip dependency check reported issues."
  [[ -f .env ]] || die "Configuration file '.env' is missing."
  # Check if the PORT variable is set, otherwise default to 8000
  local app_port="${PORT:-8000}"
  curl -fs "http://localhost:${app_port}/healthz" > /dev/null || die "Application health check endpoint (/healthz) on port ${app_port} is not responding."
  log SUCCESS "All system health checks passed."
}

# Run the full pytest test suite
run_full_test_suite() {
  log INFO "Running test suite..."
  [[ -d tests ]] || { log WARN "No 'tests' directory found. Skipping tests."; return; }
  source venv/bin/activate
  export PYTHONPATH="$(pwd)"
  if python3 -m pytest -q; then
    log SUCCESS "All tests passed."
  else
    die "Pytest test suite failed."
  fi
}

# ======================================================================================
# SECTION 6: CLEANUP & SECURITY
# ======================================================================================
cleanup_logs() {
    log INFO "Cleaning up log files in '$LOG_DIR'..."
    # Use find for more robust deletion
    find "$LOG_DIR" -name "*.log" -type f -delete
    log SUCCESS "Log files cleaned up."
}

# Reset the login lockout by clearing the login attempts table
reset_login_lockout() {
    log INFO "Attempting to reset login lockout..."
    local db_file="data/artnarrator.sqlite3"
    local lockout_table="login_attempts"

    if ! command -v sqlite3 &> /dev/null; then
        log ERROR "'sqlite3' command not found. Please install it (e.g., 'sudo apt-get install sqlite3')."
        return 1
    fi

    if [[ ! -f "$db_file" ]]; then
        log ERROR "Database file '$db_file' not found in the project root."
        return 1
    fi

    log WARN "This will clear all records of failed login attempts from the '$lockout_table' table."
    read -p "Are you sure you want to continue? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sqlite3 "$db_file" "DELETE FROM $lockout_table;"
        log SUCCESS "Login lockout table has been cleared."
    else
        log INFO "Login reset cancelled by user."
    fi
}

# Clear all active sessions by deleting the session registry file
clear_all_sessions() {
    log INFO "Attempting to clear all active user sessions..."
    local session_file="logs/session_registry.json"

    if [[ ! -f "$session_file" ]]; then
        log WARN "Session registry file not found. No sessions to clear."
        return
    fi

    log WARN "This will immediately log out ALL users from the application. This is useful if you are locked out due to the session limit."
    read -p "Are you sure you want to delete the session file? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -f "$session_file"
        log SUCCESS "Session registry file has been deleted. All users have been logged out."
    else
        log INFO "Session clear cancelled by user."
    fi
}


# ======================================================================================
# SECTION 7: SNAPSHOT LOGGING & UTILITIES
# ======================================================================================
# Gather recent logs into a single snapshot file
gather_recent_logs() {
  local snapshot_dir="code-stacks/log-snapshots"
  local now
  now=$(date "+%a-%d-%B-%Y-%I-%M-%p")
  local outfile="${snapshot_dir}/log-stack-${now}.md"
  mkdir -p "$snapshot_dir"
  echo "# 📦 LOG SNAPSHOT (Last 60 Minutes) - ${now}" > "$outfile"
  find "$LOG_DIR" -type f \( -name "*.log" -o -name "*.txt" \) -mmin -60 | while read -r file; do
    echo -e "\n\n---\n## $(basename "$file")\n---" >> "$outfile"
    echo "**Path:** \`$file\`" >> "$outfile"
    echo "**Updated:** \`$(stat -c %y "$file")\`" >> "$outfile"
    echo "\`\`\`" >> "$outfile"
    cat "$file" >> "$outfile"
    echo "\`\`\`" >> "$outfile"
  done
  log SUCCESS "Log snapshot saved to: $outfile"
}

# Execute the code-stacker script
run_code_stack() {
  [[ -x "./${CODESTACK_SCRIPT}" ]] && ./"${CODESTACK_SCRIPT}" || log ERROR "'${CODESTACK_SCRIPT}' not found or not executable."
}

# Execute the folder tree generator script
run_folder_tree_generator() {
  log INFO "Generating folder tree..."
  if [[ -f "./generate_folder_tree.py" ]]; then
    python3 ./generate_folder_tree.py || log ERROR "Folder tree generator script failed."
  else
    log ERROR "'generate_folder_tree.py' not found."
  fi
}

# Generate all audit files at once
generate_all_audits() {
    log INFO "Generating all audit files: Code Stack, Folder Tree, and Log Snapshot..."
    run_code_stack
    run_folder_tree_generator
    gather_recent_logs
    log SUCCESS "All audit files have been generated."
}

# ======================================================================================
# SECTION 8: SERVICE & LOG CONTROL
# ======================================================================================
# --- Service Management ---
_service_action() {
    local action="$1"
    log INFO "${action^}ing 'artnarrator' service..."
    if sudo systemctl "$action" artnarrator; then
        log SUCCESS "Service '${action}' command issued successfully."
    else
        log ERROR "Failed to issue '${action}' command to service."
    fi
}

start_service() { _service_action start; }
stop_service() { _service_action stop; }
restart_service() { _service_action restart; }
enable_service_on_boot() { _service_action enable; }
disable_service_on_boot() { _service_action disable; }

# Restart all relevant services
restart_all_services() {
    log INFO "Restarting all services..."
    restart_service # Currently only one service, but this is extensible
    log SUCCESS "All services have been issued a restart command."
}

check_service_status() {
    log INFO "Checking 'artnarrator' service status..."
    sudo systemctl status artnarrator --no-pager
}

reload_systemd_daemon() {
    log INFO "Reloading systemd daemon..."
    if sudo systemctl daemon-reload; then
        log SUCCESS "Systemd daemon reloaded."
    else
        log ERROR "Failed to reload systemd daemon."
    fi
}

# --- Log Viewing ---
_tail_log() {
    local log_path="$1"
    local log_name="$2"
    if [[ -f "$log_path" ]]; then
        log INFO "Tailing $log_name... (Press Ctrl+C to exit)"
        tail -f "$log_path"
    else
        log WARN "$log_name not found at '$log_path'."
        sleep 2
    fi
}

view_gunicorn_access_log() { _tail_log "$LOG_DIR/gunicorn-access.log" "Gunicorn access log"; }
view_gunicorn_error_log() { _tail_log "$LOG_DIR/gunicorn-error.log" "Gunicorn error log"; }
view_main_app_log() { _tail_log "$LOG_DIR/composites-workflow.log" "Main application log"; }

view_latest_analysis_log() {
    log INFO "Finding and tailing the latest analysis script log..."
    local analysis_log_dir="$LOG_DIR/ANALYZE_SCRIPT"
    mkdir -p "$analysis_log_dir"
    local latest_log
    latest_log=$(find "$analysis_log_dir" -type f -printf '%T@ %p\n' | sort -nr | head -n 1 | cut -d' ' -f2-)

    if [[ -n "$latest_log" ]]; then
        _tail_log "$latest_log" "Latest analysis log"
    else
        log WARN "No analysis script log files found in '$analysis_log_dir'."
        sleep 2
    fi
}

# ======================================================================================
# SECTION 9: MENU SYSTEM
# ======================================================================================
_print_menu() {
    echo -e "\n$1"
    shift
    while [ $# -gt 0 ]; do
        echo "  [$1] $2"
        shift 2
    done
    echo "  [0] Back to Previous Menu / Exit"
}

main_menu() {
  while true; do
    _print_menu "========================\n      MAIN MENU\n========================" \
      "1" "PUSH Workflow (Test, Backup, Push, Restart)" \
      "2" "System Service Actions" \
      "3" "Live Log Viewer" \
      "4" "Backup Management" \
      "5" "Security & Cleanup" \
      "6" "Audit & Utility Tools"
    read -rp "Select an option: " main_sel
    case "$main_sel" in
      1) full_push ;;
      2) system_actions_menu ;;
      3) live_log_menu ;;
      4) backup_menu ;;
      5) security_menu ;;
      6) audit_menu ;;
      0) exit 0 ;;
      *) log WARN "Invalid option '$main_sel'" ;;
    esac
  done
}

system_actions_menu() {
  while true; do
    _print_menu "------ SYSTEM ACTIONS MENU ------" \
        "1" "Check App Status" "2" "Start App" "3" "Stop App" "4" "Restart App" \
        "---" "---" \
        "5" "Enable App on Boot" "6" "Disable App on Boot" \
        "---" "---" \
        "7" "Reload systemd Daemon" \
        "8" "Restart All Services"
    read -rp "Select: " sel
    case "$sel" in
        1) check_service_status ;; 2) start_service ;; 3) stop_service ;; 4) restart_service ;;
        5) enable_service_on_boot ;; 6) disable_service_on_boot ;; 7) reload_systemd_daemon ;;
        8) restart_all_services ;;
        0) return ;; *) log WARN "Invalid option '$sel'" ;;
    esac
  done
}

live_log_menu() {
  while true; do
    _print_menu "------ LIVE LOG VIEWER ------" \
        "1" "Gunicorn Access Log" \
        "2" "Gunicorn Error Log" \
        "3" "Main Application Log" \
        "4" "Latest Analysis Script Log"
    read -rp "Select a log to view: " sel
    case "$sel" in
        1) view_gunicorn_access_log ;; 2) view_gunicorn_error_log ;;
        3) view_main_app_log ;; 4) view_latest_analysis_log ;;
        0) return ;; *) log WARN "Invalid option '$sel'" ;;
    esac
  done
}

backup_menu() {
  while true; do
    _print_menu "------ BACKUP MENU ------" \
        "1" "Create Local Backup" \
        "2" "Run Full Cloud Backup (Live)" \
        "3" "Run Cloud Backup Simulation (Dry Run)"
    read -rp "Select: " sel
    case "$sel" in
        1) local_backup ;;
        2) run_actual_backup ;;
        3) run_cron_backup_simulation ;;
        0) return ;; *) log WARN "Invalid option '$sel'" ;;
    esac
  done
}

security_menu() {
    while true; do
        _print_menu "------ SECURITY & CLEANUP ------" \
            "1" "Reset Failed Login Lockout" \
            "2" "Clear All Active Sessions" \
            "3" "Delete all .log files"
        read -rp "Select: " sel
        case "$sel" in
            1) reset_login_lockout ;;
            2) clear_all_sessions ;;
            3) cleanup_logs ;;
            0) return ;; *) log WARN "Invalid option '$sel'" ;;
        esac
    done
}

audit_menu() {
    while true; do
        _print_menu "------ AUDIT & UTILITY MENU ------" \
            "1" "Generate Code Stack Snapshot" \
            "2" "Generate Folder Tree" \
            "3" "Generate Log Snapshot (last hour)" \
            "4" "Generate All Stacks and Tree"
        read -rp "Select: " sel
        case "$sel" in
            1) run_code_stack ;;
            2) run_folder_tree_generator ;;
            3) gather_recent_logs ;;
            4) generate_all_audits ;;
            0) return ;; *) log WARN "Invalid option '$sel'" ;;
        esac
    done
}

# ======================================================================================
# ENTRYPOINT
# ======================================================================================
log INFO "Project Toolkit Initialised – Launching Main Menu..."
main_menu
