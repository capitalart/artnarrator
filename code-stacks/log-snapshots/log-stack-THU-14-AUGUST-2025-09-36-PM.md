# 📦 LOG SNAPSHOT (Last 60 Minutes)


---
## project-toolkit-2025-08-14_21-36-11.log
---
**Path:** `logs/project-toolkit-2025-08-14_21-36-11.log`
**Updated:** `2025-08-14 21:36:11`
[1;36m[INFO][0m Project Toolkit Initialised – Launching Main Menu...


---
## THU-14-AUG-2025-11-23-AM-ANALYZE_OPENAI.log
---
**Path:** `logs/analyse-openai/THU-14-AUG-2025-11-23-AM-ANALYZE_OPENAI.log`
**Updated:** `2025-08-14 20:53:33`


---
## gunicorn-access.log
---
**Path:** `logs/gunicorn-access.log`
**Updated:** `2025-08-14 19:47:53`


---
## composites-workflow.log
---
**Path:** `logs/composites-workflow.log`
**Updated:** `2025-08-14 20:53:35`


---
## gunicorn-error.log
---
**Path:** `logs/gunicorn-error.log`
**Updated:** `2025-08-14 20:53:31`
  File "/home/artnarrator/artnarrator.com/venv/lib/python3.11/site-packages/gunicorn/util.py", line 370, in import_app
    mod = importlib.import_module(module)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1206, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/artnarrator/artnarrator.com/app.py", line 36, in <module>
    from routes.artwork_routes import bp as artwork_bp
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 118, in <module>
    import scripts.analyze_artwork as aa
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 32, in <module>
    if not API_KEY: raise RuntimeError("OPENAI_API_KEY not set in environment/.env file")
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: OPENAI_API_KEY not set in environment/.env file
[2025-08-14 11:13:04 +0000] [110670] [INFO] Worker exiting (pid: 110670)
[2025-08-14 11:13:05 +0000] [110669] [ERROR] Worker (pid:110670) exited with code 3
[2025-08-14 11:13:05 +0000] [110669] [ERROR] Shutting down: Master
[2025-08-14 11:13:05 +0000] [110669] [ERROR] Reason: Worker failed to boot.
[2025-08-14 11:23:31 +0000] [111972] [INFO] Starting gunicorn 23.0.0
[2025-08-14 11:23:31 +0000] [111972] [INFO] Listening at: http://127.0.0.1:8000 (111972)
[2025-08-14 11:23:31 +0000] [111972] [INFO] Using worker: sync
[2025-08-14 11:23:31 +0000] [111974] [INFO] Booting worker with pid: 111974
[2025-08-14 11:23:31 +0000] [111975] [INFO] Booting worker with pid: 111975
[2025-08-14 11:23:31 +0000] [111976] [INFO] Booting worker with pid: 111976
