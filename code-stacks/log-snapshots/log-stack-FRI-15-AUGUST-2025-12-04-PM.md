# 📦 LOG SNAPSHOT (Last 60 Minutes)


---
## project-toolkit-2025-08-14_21-36-11.log
---
**Path:** `logs/project-toolkit-2025-08-14_21-36-11.log`
**Updated:** `2025-08-14 22:03:57`
[1;36m[INFO][0m Project Toolkit Initialised – Launching Main Menu...
[1;32m[SUCCESS][0m Log snapshot saved: code-stacks/log-snapshots/log-stack-THU-14-AUGUST-2025-09-36-PM.md
[1;36m[INFO][0m Running [PULL] workflow...
[1;36m[INFO][0m Running health check...
[1;31m[ERROR][0m /healthz not responding


---
## THU-14-AUG-2025-11-23-AM-ANALYZE_OPENAI.log
---
**Path:** `logs/analyse-openai/THU-14-AUG-2025-11-23-AM-ANALYZE_OPENAI.log`
**Updated:** `2025-08-14 20:53:33`


---
## FRI-15-AUG-2025-12-02-PM-ANALYZE_OPENAI.log
---
**Path:** `logs/analyse-openai/FRI-15-AUG-2025-12-02-PM-ANALYZE_OPENAI.log`
**Updated:** `2025-08-15 12:02:19`
2025-08-15 12:02:10,272 - __main__ - INFO - --- Starting analysis for: cassowary-test-01-test-run.jpg (User: anonymous) ---
2025-08-15 12:02:10,281 - __main__ - INFO - Determined aspect ratio for cassowary-test-01-test-run.jpg: 4x5
2025-08-15 12:02:10,283 - __main__ - INFO - Optimized image for AI: cassowary-test-01-test-run-OPTIMIZED.jpg (0.4 KB)
2025-08-15 12:02:10,283 - __main__ - INFO - Preparing to call OpenAI API for cassowary-test-01-test-run-OPTIMIZED.jpg with SKU RJC-0297.
2025-08-15 12:02:10,283 - __main__ - INFO - Sending request to OpenAI ChatCompletion API...
2025-08-15 12:02:18,867 - __main__ - INFO - Received response from OpenAI. Raw text length: 1508 chars.
2025-08-15 12:02:18,870 - __main__ - INFO - Saved artwork files to /home/artnarrator/artnarrator.com/art-processing/processed-artwork/cassowary-blue-symphony-art-by-robin-custance-RJC-0297
2025-08-15 12:02:19,857 - __main__ - INFO - Detected dominant colours for cassowary-blue-symphony-art-by-robin-custance-RJC-0297.jpg: ['Blue']
2025-08-15 12:02:19,859 - __main__ - INFO - Wrote final listing JSON to /home/artnarrator/artnarrator.com/art-processing/processed-artwork/cassowary-blue-symphony-art-by-robin-custance-RJC-0297/cassowary-blue-symphony-art-by-robin-custance-RJC-0297-listing.json
2025-08-15 12:02:19,859 - __main__ - INFO - Added cassowary-blue-symphony-art-by-robin-custance-RJC-0297.jpg to mockup queue.
2025-08-15 12:02:19,859 - __main__ - INFO - --- Successfully completed analysis for: cassowary-test-01-test-run.jpg ---


---
## FRI-15-AUG-2025-11-54-AM-ANALYZE_OPENAI.log
---
**Path:** `logs/analyse-openai/FRI-15-AUG-2025-11-54-AM-ANALYZE_OPENAI.log`
**Updated:** `2025-08-15 11:54:05`


---
## gunicorn-access.log
---
**Path:** `logs/gunicorn-access.log`
**Updated:** `2025-08-15 11:55:13`
127.0.0.1 - - [15/Aug/2025:11:54:30 +0930] "GET /static/css/edit_listing.css HTTP/1.0" 200 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:54:31 +0930] "GET /static/fonts/Urbanist-VariableFont_wght.ttf HTTP/1.0" 200 0 "https://artnarrator.com/static/css/style.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:54:32 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:54:32 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8817 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:07 +0930] "POST /login?next=/ HTTP/1.0" 302 189 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:08 +0930] "GET / HTTP/1.0" 200 10561 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:08 +0930] "GET /static/css/main.css HTTP/1.0" 304 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:08 +0930] "GET /static/icons/svg/light/number-circle-one-light.svg HTTP/1.0" 200 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:08 +0930] "GET /static/icons/svg/light/number-circle-two-light.svg HTTP/1.0" 200 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:08 +0930] "GET /static/js/main-overlay-test.js HTTP/1.0" 304 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:08 +0930] "GET /static/icons/svg/light/palette-light.svg HTTP/1.0" 304 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:08 +0930] "GET /static/icons/svg/light/number-circle-three-light.svg HTTP/1.0" 200 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/js/analysis-modal.js HTTP/1.0" 304 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/icons.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/style.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/edit_listing.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/layout.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/GDWS-style.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/buttons.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/art-cards.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/modals-popups.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/documentation.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/css/overlay-menu.css HTTP/1.0" 304 0 "https://artnarrator.com/static/css/main.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/icons/svg/light/number-circle-four-light.svg HTTP/1.0" 200 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/icons/svg/light/number-circle-five-light.svg HTTP/1.0" 200 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/icons/svg/light/arrows-clockwise-light.svg HTTP/1.0" 304 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/icons/svg/light/coffee-light.svg HTTP/1.0" 304 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:09 +0930] "GET /static/fonts/Urbanist-VariableFont_wght.ttf HTTP/1.0" 304 0 "https://artnarrator.com/static/css/style.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:10 +0930] "GET /favicon.ico HTTP/1.0" 404 568 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [15/Aug/2025:11:55:13 +0930] "GET /static/icons/svg/light/number-circle-four-light.svg HTTP/1.0" 304 0 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"


---
## composites-workflow.log
---
**Path:** `logs/composites-workflow.log`
**Updated:** `2025-08-15 11:55:10`
2025-08-15 11:55:07,911 [INFO] Registered new session 6bf33a72-8b33-4048-8e55-a79b7faf9bc3 for user 'robbie'.
2025-08-15 11:55:07,918 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-15 11:55:10,219 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico


---
## composite_gen_3a34000c6329415a8a3a06289cc53ab8.log
---
**Path:** `logs/composite-generation-logs/composite_gen_3a34000c6329415a8a3a06289cc53ab8.log`
**Updated:** `2025-08-15 12:02:20`
=== STDOUT ===


=== STDERR ===
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 33, in <module>
    import cv2
  File "/home/artnarrator/artnarrator.com/venv/lib/python3.11/site-packages/cv2/__init__.py", line 181, in <module>
    bootstrap()
  File "/home/artnarrator/artnarrator.com/venv/lib/python3.11/site-packages/cv2/__init__.py", line 153, in bootstrap
    native_module = importlib.import_module("cv2")
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ImportError: libGL.so.1: cannot open shared object file: No such file or directory


---
## project-toolkit-2025-08-15_12-04-18.log
---
**Path:** `logs/project-toolkit-2025-08-15_12-04-18.log`
**Updated:** `2025-08-15 12:04:18`
[1;36m[INFO][0m Project Toolkit Initialised – Launching Main Menu...


---
## gunicorn-error.log
---
**Path:** `logs/gunicorn-error.log`
**Updated:** `2025-08-15 11:54:03`
[2025-08-15 11:54:03 +0930] [185219] [INFO] Starting gunicorn 23.0.0
[2025-08-15 11:54:03 +0930] [185219] [INFO] Listening at: http://127.0.0.1:8000 (185219)
[2025-08-15 11:54:03 +0930] [185219] [INFO] Using worker: sync
[2025-08-15 11:54:03 +0930] [185222] [INFO] Booting worker with pid: 185222
[2025-08-15 11:54:03 +0930] [185223] [INFO] Booting worker with pid: 185223
[2025-08-15 11:54:03 +0930] [185224] [INFO] Booting worker with pid: 185224
