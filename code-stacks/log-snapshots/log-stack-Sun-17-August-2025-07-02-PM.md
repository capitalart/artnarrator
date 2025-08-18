# 📦 LOG SNAPSHOT (Last 60 Minutes) - Sun-17-August-2025-07-02-PM


---
## project-toolkit-2025-08-17_19-02-00.log
---
**Path:** `logs/project-toolkit-2025-08-17_19-02-00.log`
**Updated:** `2025-08-17 19:02:09.102660624 +0930`
```
[1;36m[INFO](B[m Project Toolkit Initialised – Launching Main Menu...
[1;36m[INFO](B[m Generating all audit files: Code Stack, Folder Tree, and Log Snapshot...
[1;36m[INFO](B[m Generating folder tree...
```


---
## project-toolkit-2025-08-17_18-10-47.log
---
**Path:** `logs/project-toolkit-2025-08-17_18-10-47.log`
**Updated:** `2025-08-17 18:12:21.584847685 +0930`
```
[1;36m[INFO](B[m Project Toolkit Initialised – Launching Main Menu...
[1;36m[INFO](B[m Attempting to reset login lockout...
[1;33m[WARN](B[m This will clear all records of failed login attempts from the 'login_attempts' table.
```


---
## 2025-08-17_08.log
---
**Path:** `logs/delete/2025-08-17_08.log`
**Updated:** `2025-08-17 18:26:18.895650135 +0930`
```
2025-08-17 08:55:59 | user: robbie | action: delete | file: artwork-rjc-0482-by-robin-custance-rjc-rjc-0482 | status: success | detail: Initiating delete for 'artwork-rjc-0482-by-robin-custance-rjc-rjc-0482'
2025-08-17 08:55:59 | user: robbie | action: delete | file: artwork-rjc-0482-by-robin-custance-rjc-rjc-0482 | status: success | detail: Delete process completed.
2025-08-17 08:56:03 | user: robbie | action: delete | file: artwork-rjc-0445-by-robin-custance-rjc-rjc-0445 | status: success | detail: Initiating delete for 'artwork-rjc-0445-by-robin-custance-rjc-rjc-0445'
2025-08-17 08:56:03 | user: robbie | action: delete | file: artwork-rjc-0445-by-robin-custance-rjc-rjc-0445 | status: success | detail: Delete process completed.
2025-08-17 08:56:06 | user: robbie | action: delete | file: artwork-rjc-0447-by-robin-custance-rjc-rjc-0447 | status: success | detail: Initiating delete for 'artwork-rjc-0447-by-robin-custance-rjc-rjc-0447'
2025-08-17 08:56:06 | user: robbie | action: delete | file: artwork-rjc-0447-by-robin-custance-rjc-rjc-0447 | status: success | detail: Delete process completed.
2025-08-17 08:56:09 | user: robbie | action: delete | file: artwork-rjc-0450-by-robin-custance-rjc-rjc-0450 | status: success | detail: Initiating delete for 'artwork-rjc-0450-by-robin-custance-rjc-rjc-0450'
2025-08-17 08:56:09 | user: robbie | action: delete | file: artwork-rjc-0450-by-robin-custance-rjc-rjc-0450 | status: success | detail: Delete process completed.
2025-08-17 08:56:12 | user: robbie | action: delete | file: artwork-rjc-0449-by-robin-custance-rjc-rjc-0449 | status: success | detail: Initiating delete for 'artwork-rjc-0449-by-robin-custance-rjc-rjc-0449'
2025-08-17 08:56:12 | user: robbie | action: delete | file: artwork-rjc-0449-by-robin-custance-rjc-rjc-0449 | status: success | detail: Delete process completed.
2025-08-17 08:56:15 | user: robbie | action: delete | file: artwork-rjc-0452-by-robin-custance-rjc-rjc-0452 | status: success | detail: Initiating delete for 'artwork-rjc-0452-by-robin-custance-rjc-rjc-0452'
2025-08-17 08:56:15 | user: robbie | action: delete | file: artwork-rjc-0452-by-robin-custance-rjc-rjc-0452 | status: success | detail: Delete process completed.
2025-08-17 08:56:18 | user: robbie | action: delete | file: artwork-rjc-0454-by-robin-custance-rjc-rjc-0454 | status: success | detail: Initiating delete for 'artwork-rjc-0454-by-robin-custance-rjc-rjc-0454'
2025-08-17 08:56:18 | user: robbie | action: delete | file: artwork-rjc-0454-by-robin-custance-rjc-rjc-0454 | status: success | detail: Delete process completed.
```


---
## gunicorn-access.log
---
**Path:** `logs/gunicorn-access.log`
**Updated:** `2025-08-17 18:48:35.797542231 +0930`
```
127.0.0.1 - - [16/Aug/2025:13:40:24 +0930] "GET /status/analyze HTTP/1.0" 200 104 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:40:24 +0930] "POST /analyze/4x5/RJC-00312.jpg HTTP/1.0" 404 568 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:09 +0930] "GET /artworks HTTP/1.0" 200 10085 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:10 +0930] "GET /unanalysed-img/RJC-00312/RJC-00312-thumb.jpg HTTP/1.0" 200 0 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:14 +0930] "POST /delete-unanalysed/RJC-00312 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:14 +0930] "GET /artworks HTTP/1.0" 200 8975 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:18 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:45 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:46 +0930] "GET /artworks HTTP/1.0" 200 10219 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:46 +0930] "GET /artworks HTTP/1.0" 200 10079 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:47 +0930] "GET /unanalysed-img/RJC-00313/RJC-00313-thumb.jpg HTTP/1.0" 200 0 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:49 +0930] "GET /status/analyze HTTP/1.0" 200 104 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:43:50 +0930] "POST /analyze/4x5/RJC-00313.jpg HTTP/1.0" 404 568 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:51:15 +0930] "GET /artworks HTTP/1.0" 200 10079 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:51:15 +0930] "GET /unanalysed-img/RJC-00313/RJC-00313-thumb.jpg HTTP/1.0" 200 0 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:51:18 +0930] "GET / HTTP/1.0" 200 10561 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:51:20 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:13:59:19 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [16/Aug/2025:13:59:20 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [16/Aug/2025:14:10:40 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:02 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:03 +0930] "GET /artworks HTTP/1.0" 200 11481 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:03 +0930] "GET /artworks HTTP/1.0" 200 11341 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:04 +0930] "GET /unanalysed-img/RJC-00313/RJC-00313-thumb.jpg HTTP/1.0" 200 0 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:04 +0930] "GET /unanalysed-img/RJC-00314/RJC-00314-thumb.jpg HTTP/1.0" 404 568 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:10 +0930] "GET /status/analyze HTTP/1.0" 200 104 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:10 +0930] "POST /analyze/4x5/RJC-00314.jpg HTTP/1.0" 404 568 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:16 +0930] "GET /status/analyze HTTP/1.0" 200 104 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:16 +0930] "POST /analyze/4x5/RJC-00313.jpg HTTP/1.0" 404 568 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:22 +0930] "POST /delete-unanalysed/RJC-00314 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:23 +0930] "GET /artworks HTTP/1.0" 200 10237 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:23 +0930] "GET /unanalysed-img/RJC-00314/RJC-00314-thumb.jpg HTTP/1.0" 404 568 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:26 +0930] "POST /delete-unanalysed/RJC-00313 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:11:26 +0930] "GET /artworks HTTP/1.0" 200 8975 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:17:54 +0930] "POST /analyze/RJC-99999 HTTP/1.1" 302 247 "-" "curl/7.88.1"
127.0.0.1 - - [16/Aug/2025:14:23:16 +0930] "GET /health HTTP/1.1" 200 2 "-" "curl/7.88.1"
127.0.0.1 - - [16/Aug/2025:14:23:16 +0930] "GET /health/openai HTTP/1.1" 302 239 "-" "curl/7.88.1"
127.0.0.1 - - [16/Aug/2025:14:23:16 +0930] "GET /health/google HTTP/1.1" 302 239 "-" "curl/7.88.1"
127.0.0.1 - - [16/Aug/2025:14:25:16 +0930] "GET /artworks HTTP/1.0" 200 10181 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:25:23 +0930] "POST /delete-artwork/artwork-rjc-99999-by-robin-custance-rjc-rjc-99999 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:25:23 +0930] "GET /artworks HTTP/1.0" 200 9015 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:25:31 +0930] "GET /admin/gdws/ HTTP/1.0" 200 24494 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:25:36 +0930] "GET /admin/gdws/template/4x5 HTTP/1.0" 200 14076 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:25:50 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:26:24 +0930] "POST /analyze/RJC-TEST00 HTTP/1.1" 302 249 "-" "curl/7.88.1"
127.0.0.1 - - [16/Aug/2025:14:38:10 +0930] "GET /.env HTTP/1.0" 302 221 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:10 +0930] "GET /.env.bak HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:10 +0930] "GET /.env.local HTTP/1.0" 302 233 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:11 +0930] "GET /.env.production HTTP/1.0" 302 243 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:11 +0930] "GET /.env.dev HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:11 +0930] "GET /config/.env HTTP/1.0" 302 235 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:11 +0930] "GET /docker/.env HTTP/1.0" 302 235 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:12 +0930] "GET /api/.env HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:12 +0930] "GET /api/config HTTP/1.0" 302 233 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:12 +0930] "GET /login?next=/api/config HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:13 +0930] "GET /api/settings.json HTTP/1.0" 302 247 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:13 +0930] "GET /api/keys HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:13 +0930] "GET /login?next=/api/keys HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:13 +0930] "GET /api/credentials HTTP/1.0" 302 243 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:14 +0930] "GET /login?next=/api/credentials HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:14 +0930] "GET /phpinfo HTTP/1.0" 302 227 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:14 +0930] "GET /login?next=/phpinfo HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:14 +0930] "GET /phpinfo.php HTTP/1.0" 302 235 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:15 +0930] "GET /info.php HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:15 +0930] "GET /php.php HTTP/1.0" 302 227 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:15 +0930] "GET /test.php HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:15 +0930] "GET /index.php?=phpinfo() HTTP/1.0" 302 231 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:16 +0930] "GET /config.json HTTP/1.0" 302 235 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:16 +0930] "GET /settings.json HTTP/1.0" 302 239 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:16 +0930] "GET /secrets.json HTTP/1.0" 302 237 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:16 +0930] "GET /secure-config.json HTTP/1.0" 302 249 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:17 +0930] "GET /config/production.json HTTP/1.0" 302 257 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:17 +0930] "GET /config/dev.json HTTP/1.0" 302 243 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:17 +0930] "GET /config/default.json HTTP/1.0" 302 251 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:18 +0930] "GET /application.yml HTTP/1.0" 302 243 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:18 +0930] "GET /application.properties HTTP/1.0" 302 257 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:18 +0930] "GET /src/main/resources/application.yml HTTP/1.0" 302 281 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:18 +0930] "GET /.env.bak HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:19 +0930] "GET /.env_backup.txt HTTP/1.0" 302 243 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:19 +0930] "GET /config.old.php HTTP/1.0" 302 241 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:19 +0930] "GET /database_old.json HTTP/1.0" 302 247 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:19 +0930] "GET /settings.bak HTTP/1.0" 302 237 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:20 +0930] "GET /docker/.env HTTP/1.0" 302 235 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:20 +0930] "GET /.aws/credentials HTTP/1.0" 302 245 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:20 +0930] "GET /config.yaml HTTP/1.0" 302 235 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:20 +0930] "GET /settings.yaml HTTP/1.0" 302 239 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:21 +0930] "GET /helm/values.yaml HTTP/1.0" 302 245 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:21 +0930] "GET /main.js HTTP/1.0" 302 227 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:22 +0930] "GET /index.js HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:22 +0930] "GET /app.js HTTP/1.0" 302 225 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:23 +0930] "GET /bundle.js HTTP/1.0" 302 231 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:23 +0930] "GET /*.map HTTP/1.0" 302 223 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:23 +0930] "GET /pinfo.php HTTP/1.0" 302 231 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:24 +0930] "GET /sysinfo.php HTTP/1.0" 302 235 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:24 +0930] "GET /systeminfo.php HTTP/1.0" 302 241 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:24 +0930] "GET /php-version.php HTTP/1.0" 302 243 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:24 +0930] "GET /serverinfo.php HTTP/1.0" 302 241 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:25 +0930] "GET /phpinf.php HTTP/1.0" 302 233 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:25 +0930] "GET /phpv.php HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:25 +0930] "GET /next.config.js HTTP/1.0" 302 241 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:26 +0930] "GET /.next/env HTTP/1.0" 302 231 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:26 +0930] "GET /.next/static/development/pages/.env HTTP/1.0" 302 283 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:27 +0930] "GET /.next/static/env.js HTTP/1.0" 302 251 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:27 +0930] "GET /nuxt.config.js HTTP/1.0" 302 241 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:38:27 +0930] "GET /.output/server/.env HTTP/1.0" 302 251 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:43:12 +0930] "POST /analyze/RJC-TEST00 HTTP/1.1" 302 249 "-" "curl/7.88.1"
127.0.0.1 - - [16/Aug/2025:14:43:19 +0930] "POST /analyze/RJC-TEST00 HTTP/1.1" 302 249 "-" "curl/7.88.1"
127.0.0.1 - - [16/Aug/2025:14:58:43 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:58:43 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:58:57 +0930] "POST /login?next=/ HTTP/1.0" 302 189 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:58:57 +0930] "GET / HTTP/1.0" 200 10627 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:02 +0930] "GET /artworks HTTP/1.0" 200 10195 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:07 +0930] "POST /delete-artwork/artwork-rjc-test00-by-robin-custance-rjc-rjc-test00 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:07 +0930] "GET /artworks HTTP/1.0" 200 9017 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:10 +0930] "GET / HTTP/1.0" 200 10561 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:12 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:42 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:43 +0930] "GET /artworks HTTP/1.0" 200 10225 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:43 +0930] "GET /artworks HTTP/1.0" 200 10085 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:14:59:43 +0930] "GET /unanalysed-img/RJC-00325/RJC-00325-thumb.jpg HTTP/1.0" 404 568 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:15:00:23 +0930] "POST /delete-unanalysed/RJC-00325 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:15:00:23 +0930] "GET /artworks HTTP/1.0" 200 8975 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:15:00:36 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:15:00:54 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:15:00:54 +0930] "GET /artworks HTTP/1.0" 200 10219 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:15:00:54 +0930] "GET /artworks HTTP/1.0" 200 10079 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:15:00:55 +0930] "GET /unanalysed-img/RJC-00326/RJC-00326-thumb.jpg HTTP/1.0" 404 568 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:15:01:31 +0930] "GET /unanalysed/RJC-00326/RJC-00326-thumb.jpg HTTP/1.0" 404 568 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:17:28:27 +0930] "GET /unanalysed-img/RJC-00326/RJC-00326-thumb.jpg HTTP/1.0" 302 301 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:17:28:27 +0930] "GET /login?next=/unanalysed-img/RJC-00326/RJC-00326-thumb.jpg HTTP/1.0" 200 8817 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:02:28 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot"
127.0.0.1 - - [16/Aug/2025:18:07:36 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [16/Aug/2025:18:07:40 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [16/Aug/2025:18:18:53 +0930] "GET / HTTP/1.0" 302 213 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:18:53 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:19:05 +0930] "POST /login?next=/ HTTP/1.0" 302 189 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:19:06 +0930] "GET / HTTP/1.0" 200 10623 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:19:41 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:24:56 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:25:01 +0930] "GET /favicon.ico HTTP/1.0" 404 568 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:25:03 +0930] "GET / HTTP/1.0" 200 10623 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:28:41 +0930] "GET / HTTP/1.0" 200 10623 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:28:47 +0930] "GET / HTTP/1.0" 200 10623 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:28:52 +0930] "GET /favicon.ico HTTP/1.0" 404 568 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:29:46 +0930] "GET / HTTP/1.0" 200 10623 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:29:50 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:28 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:28 +0930] "GET /artworks HTTP/1.0" 200 30709 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:28 +0930] "GET /artworks HTTP/1.0" 200 30569 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:39 +0930] "POST /delete-artwork/artwork-rjc-00376-by-robin-custance-rjc-rjc-00376 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:40 +0930] "GET /artworks HTTP/1.0" 200 29412 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:47 +0930] "POST /delete-artwork/artwork-rjc-0338-by-robin-custance-rjc-rjc-0338 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:48 +0930] "GET /artworks HTTP/1.0" 200 28111 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:51 +0930] "POST /delete-artwork/artwork-rjc-0341-by-robin-custance-rjc-rjc-0341 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:51 +0930] "GET /artworks HTTP/1.0" 200 26812 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:54 +0930] "POST /delete-artwork/artwork-rjc-0342-by-robin-custance-rjc-rjc-0342 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:31:54 +0930] "GET /artworks HTTP/1.0" 200 25513 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:18:41:05 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [16/Aug/2025:18:41:11 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [16/Aug/2025:18:52:12 +0930] "GET /artworks HTTP/1.0" 200 8817 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:19:42:36 +0930] "GET / HTTP/1.0" 302 213 "http://104.21.74.59:80/" "-"
127.0.0.1 - - [16/Aug/2025:19:42:36 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "-"
127.0.0.1 - - [16/Aug/2025:19:54:03 +0930] "GET /7cnSsVvj?cost=0.0570000&external_id=b8c7a918-6225-11f0-b644-2257615b58f0_224591&creative_id=224591&ad_campaign_id=86347&source=377&sub_id_1=233&sub_id_2=classic_push&aff= HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36"
127.0.0.1 - - [16/Aug/2025:19:54:04 +0930] "GET /login?next=/7cnSsVvj HTTP/1.0" 200 8817 "https://artnarrator.com/7cnSsVvj?cost=0.0570000&external_id=b8c7a918-6225-11f0-b644-2257615b58f0_224591&creative_id=224591&ad_campaign_id=86347&source=377&sub_id_1=233&sub_id_2=classic_push&aff=" "Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36"
127.0.0.1 - - [16/Aug/2025:20:57:02 +0930] "GET / HTTP/1.0" 302 213 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:20:57:02 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [16/Aug/2025:21:21:40 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [16/Aug/2025:21:21:41 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [16/Aug/2025:23:39:37 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)"
127.0.0.1 - - [16/Aug/2025:23:53:40 +0930] "GET / HTTP/1.0" 302 213 "-" "-"
127.0.0.1 - - [17/Aug/2025:00:43:35 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:00:43:37 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:01:01:47 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:01:01:49 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:01:35:38 +0930] "GET / HTTP/1.0" 302 213 "http://104.21.74.59:80/" "-"
127.0.0.1 - - [17/Aug/2025:01:35:38 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "-"
127.0.0.1 - - [17/Aug/2025:01:37:23 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:01:37:24 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:01:46:39 +0930] "GET /.env HTTP/1.0" 302 221 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:01:46:40 +0930] "POST / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:03:36:28 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:03:36:29 +0930] "GET /admin/ HTTP/1.0" 302 225 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:03:36:30 +0930] "GET /login?next=/admin/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:03:39:40 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:03:39:42 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:04:51:23 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:05:06:29 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:05:06:29 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:05:06:30 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:05:07:15 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:05:07:15 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:05:07:16 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:05:07:16 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:05:07:20 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "-" "Googlebot-Image/1.0"
127.0.0.1 - - [17/Aug/2025:05:07:25 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8817 "-" "Googlebot-Image/1.0"
127.0.0.1 - - [17/Aug/2025:05:07:26 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "-" "Googlebot-Image/1.0"
127.0.0.1 - - [17/Aug/2025:05:07:27 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8817 "-" "Googlebot-Image/1.0"
127.0.0.1 - - [17/Aug/2025:07:10:03 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:07:10:09 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:07:13:15 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:07:13:16 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:07:15:32 +0930] "GET /login HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:08:45:32 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:08:45:33 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:09:46:04 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:09:46:05 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:09:58:50 +0930] "GET / HTTP/1.0" 302 213 "-" "-"
127.0.0.1 - - [17/Aug/2025:10:07:02 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:10:07:05 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:10:15:38 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36 Edg/115.0.1901.203"
127.0.0.1 - - [17/Aug/2025:10:15:38 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36 Edg/115.0.1901.203"
127.0.0.1 - - [17/Aug/2025:11:04:18 +0930] "GET /exports/nembol HTTP/1.0" 302 241 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:11:04:19 +0930] "GET /login?next=/exports/nembol HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.183 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
127.0.0.1 - - [17/Aug/2025:11:23:43 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:11:23:46 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:11:37:55 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:11:37:57 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:12:05:06 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot"
127.0.0.1 - - [17/Aug/2025:12:07:58 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
127.0.0.1 - - [17/Aug/2025:12:43:03 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:04 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:04 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:05 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8817 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:19 +0930] "POST /login?next=/ HTTP/1.0" 302 189 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:20 +0930] "GET / HTTP/1.0" 200 10623 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:21 +0930] "GET /favicon.ico HTTP/1.0" 404 568 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:27 +0930] "GET /admin/security HTTP/1.0" 200 9469 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:34 +0930] "GET /admin/gdws/ HTTP/1.0" 200 24494 "https://artnarrator.com/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:43:38 +0930] "GET /admin/gdws/template/4x5 HTTP/1.0" 200 14076 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:11 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 1009 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:14 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 1250 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:16 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 436 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:18 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 999 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:21 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 605 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:23 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 1317 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:25 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 410 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:29 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 1713 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:30 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 224 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:31 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 327 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:33 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 529 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:35 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 343 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:36 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 245 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:45:39 +0930] "POST /admin/gdws/regenerate-paragraph HTTP/1.0" 200 768 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:46:45 +0930] "GET /artworks HTTP/1.0" 200 24414 "https://artnarrator.com/admin/gdws/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:46:48 +0930] "GET /edit-listing/4x5/cassowary-test-01-test-run.jpg HTTP/1.0" 500 9121 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:47:04 +0930] "GET / HTTP/1.0" 200 10623 "https://artnarrator.com/edit-listing/4x5/cassowary-test-01-test-run.jpg" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:47:06 +0930] "GET /artworks HTTP/1.0" 200 24414 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:49:39 +0930] "GET /artworks HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:12:49:42 +0930] "GET / HTTP/1.0" 200 10561 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:01:35 +0930] "GET / HTTP/1.0" 200 10538 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:12:28 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:13:12:33 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:13:16:39 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:16:40 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:16:41 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:16:52 +0930] "GET / HTTP/1.0" 200 10538 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:16:54 +0930] "GET /artworks HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:17:02 +0930] "GET /artworks HTTP/1.0" 200 8817 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:17:04 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:18:23 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:18:24 +0930] "GET /artworks HTTP/1.0" 200 10307 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:18:24 +0930] "GET /artworks HTTP/1.0" 200 10167 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:19:03 +0930] "GET /artworks HTTP/1.0" 200 10167 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:20:17 +0930] "GET / HTTP/1.0" 200 10538 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:20:18 +0930] "GET /artworks HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:21:16 +0930] "GET /artworks HTTP/1.0" 200 10167 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:21:20 +0930] "POST /delete-artwork/artwork-rjc-0429-by-robin-custance-rjc-rjc-0429 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:21:21 +0930] "GET /artworks HTTP/1.0" 200 9013 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:13:21:53 +0930] "GET /upload HTTP/1.0" 200 9596 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:14:10:40 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (compatible; InternetMeasurement/1.0; +https://internet-measurement.com/)"
127.0.0.1 - - [17/Aug/2025:14:10:41 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com" "Mozilla/5.0 (compatible; InternetMeasurement/1.0; +https://internet-measurement.com/)"
127.0.0.1 - - [17/Aug/2025:14:20:20 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.2; +https://openai.com/gptbot)"
127.0.0.1 - - [17/Aug/2025:15:09:47 +0930] "GET / HTTP/1.0" 302 213 "http://www.artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:15:09:48 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://www.artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:15:41:38 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:39 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:40 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:41 +0930] "GET /exports/sellbrite/manage HTTP/1.0" 302 261 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:41 +0930] "GET /admin/coordinates/ HTTP/1.0" 302 249 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:41 +0930] "GET /login?next=/admin/coordinates/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:41 +0930] "GET /login?next=/exports/sellbrite/manage HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:43 +0930] "GET /ads.txt HTTP/1.0" 302 227 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:43 +0930] "GET /login?next=/ads.txt HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:48 +0930] "GET /llms.txt HTTP/1.0" 302 229 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:41:48 +0930] "GET /login?next=/llms.txt HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.3; rb.gy/qyzae5) Chrome/124.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:15:45:22 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0"
127.0.0.1 - - [17/Aug/2025:15:45:22 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0"
127.0.0.1 - - [17/Aug/2025:15:45:23 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0"
127.0.0.1 - - [17/Aug/2025:15:54:19 +0930] "GET / HTTP/1.0" 302 213 "https://artnarrator.com/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36; 360Spider"
127.0.0.1 - - [17/Aug/2025:15:54:24 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36; 360Spider"
127.0.0.1 - - [17/Aug/2025:16:15:15 +0930] "GET /healthz HTTP/1.1" 200 2 "-" "curl/7.88.1"
127.0.0.1 - - [17/Aug/2025:16:18:04 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:16:18:05 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:17:14:16 +0930] "POST /upload HTTP/1.0" 302 225 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:17:14:16 +0930] "GET /login?next=/upload HTTP/1.0" 200 8817 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:17:14:16 +0930] "GET /artworks HTTP/1.0" 302 229 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:17:14:17 +0930] "GET /login?next=/artworks HTTP/1.0" 200 8817 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:17:14:45 +0930] "POST /login?next=/artworks HTTP/1.0" 403 9283 "https://artnarrator.com/login?next=/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:17:21:43 +0930] "GET / HTTP/1.0" 302 213 "https://artnarrator.com/login?next=/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:17:21:44 +0930] "GET /login?next=/ HTTP/1.0" 200 8817 "https://artnarrator.com/login?next=/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:17:41:53 +0930] "GET /robots.txt HTTP/1.0" 302 233 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:02:50 +0930] "GET /login?next=/ HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:02:55 +0930] "POST /login?next=/ HTTP/1.0" 403 9325 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:03:08 +0930] "GET / HTTP/1.0" 302 213 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:03:08 +0930] "GET /login?next=/ HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:01 +0930] "GET /login?next=/ HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:03 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:03 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:07 +0930] "POST /login?next=/ HTTP/1.0" 403 9325 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:07 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:07 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:28 +0930] "GET /admin/security HTTP/1.0" 302 241 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:28 +0930] "GET /login?next=/admin/security HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:29 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:29 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:33 +0930] "POST /login?next=/admin/security HTTP/1.0" 403 9325 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:33 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:05:33 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:12:35 +0930] "POST /login?next=/admin/security HTTP/1.0" 403 9325 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:12:35 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:12:35 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:12:38 +0930] "POST /login?next=/admin/security HTTP/1.0" 403 9325 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:12:39 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:12:39 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:12:58 +0930] "POST /login?next=/admin/security HTTP/1.0" 403 9325 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:13:00 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:13:00 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:13:04 +0930] "POST /login?next=/admin/security HTTP/1.0" 403 9325 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:13:04 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:13:04 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/admin/security" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:19:34 +0930] "GET / HTTP/1.0" 302 213 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:19:34 +0930] "GET /login?next=/ HTTP/1.0" 200 8846 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:19:36 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:19:37 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:19:57 +0930] "POST /login?next=/ HTTP/1.0" 403 9325 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:19:57 +0930] "GET /favicon.ico HTTP/1.0" 302 235 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:19:58 +0930] "GET /login?next=/favicon.ico HTTP/1.0" 200 8846 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:14 +0930] "POST /login?next=/ HTTP/1.0" 302 189 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:14 +0930] "GET / HTTP/1.0" 200 10631 "https://artnarrator.com/login?next=/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:15 +0930] "GET /favicon.ico HTTP/1.0" 404 568 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:23 +0930] "GET /upload HTTP/1.0" 200 9627 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:50 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:50 +0930] "GET /artworks HTTP/1.0" 200 18398 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:50 +0930] "GET /artworks HTTP/1.0" 200 18244 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:59 +0930] "POST /delete-artwork/artwork-rjc-0482-by-robin-custance-rjc-rjc-0482 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:25:59 +0930] "GET /artworks HTTP/1.0" 200 17113 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:03 +0930] "POST /delete-artwork/artwork-rjc-0445-by-robin-custance-rjc-rjc-0445 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:03 +0930] "GET /artworks HTTP/1.0" 200 15772 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:06 +0930] "POST /delete-artwork/artwork-rjc-0447-by-robin-custance-rjc-rjc-0447 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:06 +0930] "GET /artworks HTTP/1.0" 200 14431 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:09 +0930] "POST /delete-artwork/artwork-rjc-0450-by-robin-custance-rjc-rjc-0450 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:09 +0930] "GET /artworks HTTP/1.0" 200 13090 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:12 +0930] "POST /delete-artwork/artwork-rjc-0449-by-robin-custance-rjc-rjc-0449 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:12 +0930] "GET /artworks HTTP/1.0" 200 11749 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:15 +0930] "POST /delete-artwork/artwork-rjc-0452-by-robin-custance-rjc-rjc-0452 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:15 +0930] "GET /artworks HTTP/1.0" 200 10408 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:18 +0930] "POST /delete-artwork/artwork-rjc-0454-by-robin-custance-rjc-rjc-0454 HTTP/1.0" 302 205 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:19 +0930] "GET /artworks HTTP/1.0" 200 9058 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:26:34 +0930] "GET /upload HTTP/1.0" 200 9627 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:27:00 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:27:00 +0930] "GET /artworks HTTP/1.0" 200 10352 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:27:01 +0930] "GET /artworks HTTP/1.0" 200 10198 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:35:53 +0930] "GET / HTTP/1.0" 302 213 "http://artnarrator.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:18:35:54 +0930] "GET /login?next=/ HTTP/1.0" 200 8846 "https://artnarrator.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
127.0.0.1 - - [17/Aug/2025:18:46:55 +0930] "GET / HTTP/1.0" 200 10631 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:46:57 +0930] "GET /upload HTTP/1.0" 200 9627 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:47:27 +0930] "POST /upload HTTP/1.0" 302 205 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:47:27 +0930] "GET /artworks HTTP/1.0" 200 11707 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:47:28 +0930] "GET /artworks HTTP/1.0" 200 11553 "https://artnarrator.com/upload" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:48:02 +0930] "GET /admin/ HTTP/1.0" 200 8862 "https://artnarrator.com/artworks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:48:06 +0930] "GET /admin/users HTTP/1.0" 200 9973 "https://artnarrator.com/admin/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:48:27 +0930] "GET /admin/security HTTP/1.0" 200 9501 "https://artnarrator.com/admin/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
127.0.0.1 - - [17/Aug/2025:18:48:35 +0930] "GET /upload HTTP/1.0" 200 9627 "https://artnarrator.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
```


---
## composites-workflow.log
---
**Path:** `logs/composites-workflow.log`
**Updated:** `2025-08-17 18:47:25.484604073 +0930`
```
2025-08-14 21:05:04,823 [ERROR] Page not found (404): http://artnarrator.com/static/js/main.141b0494.js
2025-08-14 21:05:22,723 [ERROR] Page not found (404): http://artnarrator.com/static/js/2.ca066a4b.chunk.js
2025-08-14 21:05:23,028 [ERROR] Page not found (404): http://artnarrator.com/static/js/main.e85f7a37.js
2025-08-15 02:06:12,520 [WARNING] Failed login attempt for username: 'robbie'.
2025-08-15 02:06:27,232 [INFO] Registered new session 8933270f-8230-4c1e-a89c-7b3bb18beb50 for user 'robbie'.
2025-08-15 02:06:27,239 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-15 02:06:27,524 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-15 02:09:00,562 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-15 11:55:07,911 [INFO] Registered new session 6bf33a72-8b33-4048-8e55-a79b7faf9bc3 for user 'robbie'.
2025-08-15 11:55:07,918 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-15 11:55:10,219 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-15 12:19:22,433 [WARNING] Attempted to touch an invalid or expired session '6bf33a72-8b33-4048-8e55-a79b7faf9bc3' for user 'robbie'.
2025-08-15 12:19:35,195 [INFO] Registered new session c5545851-5b39-4212-9661-fc599fda5c01 for user 'robbie'.
2025-08-15 12:19:35,202 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-15 12:19:45,810 [INFO] Initiating deletion for artwork: 'cassowary-blue-symphony-art-by-robin-custance-RJC-0297'
2025-08-15 12:19:45,812 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/cassowary-blue-symphony-art-by-robin-custance-RJC-0297
2025-08-15 12:19:45,812 [INFO] Successfully completed deletion for artwork: 'cassowary-blue-symphony-art-by-robin-custance-RJC-0297'
2025-08-15 14:17:31,394 [WARNING] Attempted to touch an invalid or expired session 'c5545851-5b39-4212-9661-fc599fda5c01' for user 'robbie'.
2025-08-15 14:17:46,046 [INFO] Registered new session 3aaeb253-8b84-4a23-97ab-4e6557710caa for user 'robbie'.
2025-08-15 14:17:46,054 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-15 16:07:55,130 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-15 16:15:00,454 [INFO] Cleaned up expired sessions from registry.
2025-08-15 16:29:01,591 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-15 16:47:14,617 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-15 16:47:58,730 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-15 17:06:04,558 [INFO] Determined aspect ratio for Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134.jpg: 4x5
2025-08-15 17:06:10,939 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/great-barrier-reef-coral-patterns-generate-an-aboriginal-dot-painting-of-the-great-barrier-reef-focu-2-314944e7/Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134.jpg provider=openai
2025-08-15 17:06:10,939 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/great-barrier-reef-coral-patterns-generate-an-aboriginal-dot-painting-of-the-great-barrier-reef-focu-2-314944e7/Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134.jpg --json-output
2025-08-15 17:06:42,416 [ERROR] Error running analysis for Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134.jpg: Composite generation failed (-9)
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 467, in analyze_artwork_route
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 247, in _generate_composites
    raise RuntimeError(f"Composite generation failed ({result.returncode})")
RuntimeError: Composite generation failed (-9)
2025-08-15 17:16:26,506 [INFO] Initiating deletion for artwork: 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'
2025-08-15 17:16:26,506 [WARNING] Could not find folder for 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'. It may have been already deleted.
2025-08-15 17:16:26,507 [INFO] Removed 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134' from master-artwork-paths.json
2025-08-15 17:16:26,507 [INFO] Successfully completed deletion for artwork: 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'
2025-08-15 17:16:30,227 [INFO] Initiating deletion for artwork: 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'
2025-08-15 17:16:30,228 [WARNING] Could not find folder for 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'. It may have been already deleted.
2025-08-15 17:16:30,228 [INFO] Successfully completed deletion for artwork: 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'
2025-08-15 17:16:34,987 [INFO] Initiating deletion for artwork: 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'
2025-08-15 17:16:34,987 [WARNING] Could not find folder for 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'. It may have been already deleted.
2025-08-15 17:16:34,988 [INFO] Successfully completed deletion for artwork: 'Great Barrier Reef Coral Patterns Generate An Aboriginal Dot Painting Of The Great Barrier Reef Focu 2-423b5134'
2025-08-15 17:18:07,892 [INFO] Determined aspect ratio for Fern Gully With Creek Flow Generate An Aboriginal Dot Painting Of A Fern Gully With A Small Creek Ru 1-c83b26c7.jpg: 4x5
2025-08-15 17:18:11,929 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/fern-gully-with-creek-flow-generate-an-aboriginal-dot-painting-of-a-fern-gully-with-a-small-creek-ru-1-e058a168/Fern Gully With Creek Flow Generate An Aboriginal Dot Painting Of A Fern Gully With A Small Creek Ru 1-c83b26c7.jpg provider=openai
2025-08-15 17:18:11,929 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/fern-gully-with-creek-flow-generate-an-aboriginal-dot-painting-of-a-fern-gully-with-a-small-creek-ru-1-e058a168/Fern Gully With Creek Flow Generate An Aboriginal Dot Painting Of A Fern Gully With A Small Creek Ru 1-c83b26c7.jpg --json-output
2025-08-15 17:18:52,444 [INFO] Cleaned up unanalysed source folder: /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/fern-gully-with-creek-flow-generate-an-aboriginal-dot-painting-of-a-fern-gully-with-a-small-creek-ru-1-e058a168
2025-08-15 17:37:07,284 [ERROR] Could not write to session registry file at logs/session_registry.json: [Errno 2] No such file or directory: 'logs/session_registry.tmp' -> 'logs/session_registry.json'
2025-08-15 18:23:58,662 [INFO] Assigned new SKU: RJC-00311. Tracker file updated.
2025-08-15 18:24:02,102 [INFO] Determined aspect ratio for RJC-00311-original.jpg: 4x5
2025-08-15 18:24:23,190 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/RJC-00311/RJC-00311-analyse.jpg provider=openai
2025-08-15 18:24:23,190 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/RJC-00311/RJC-00311-analyse.jpg --json-output
2025-08-16 13:26:48,473 [INFO] Cleaned up expired sessions from registry.
2025-08-16 13:26:48,473 [WARNING] Attempted to touch an invalid or expired session '3aaeb253-8b84-4a23-97ab-4e6557710caa' for user 'robbie'.
2025-08-16 13:27:04,215 [INFO] Registered new session 96687d21-d1bf-478d-bbb4-edda46c283d3 for user 'robbie'.
2025-08-16 13:27:04,222 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-16 13:27:04,958 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-16 13:27:07,869 [ERROR] BuildError (missing endpoint): Could not build url for endpoint 'artwork.analyze_artwork' with values ['aspect', 'filename']. Did you mean 'artwork.analyze_artwork_route' instead?
2025-08-16 13:27:18,239 [INFO] Initiating deletion for artwork: 'RJC-00311'
2025-08-16 13:27:18,243 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/RJC-00311
2025-08-16 13:27:18,244 [INFO] Removed 'RJC-00311' from master-artwork-paths.json
2025-08-16 13:27:18,244 [INFO] Successfully completed deletion for artwork: 'RJC-00311'
2025-08-16 13:27:21,895 [INFO] Initiating deletion for artwork: 'aboriginal-dot-fern-gully-creek-by-robin-custance-RJC-0310'
2025-08-16 13:27:21,900 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/aboriginal-dot-fern-gully-creek-by-robin-custance-RJC-0310
2025-08-16 13:27:21,900 [INFO] Successfully completed deletion for artwork: 'aboriginal-dot-fern-gully-creek-by-robin-custance-RJC-0310'
2025-08-16 13:27:42,235 [INFO] Assigned new SKU: RJC-00312. Tracker file updated.
2025-08-16 13:27:42,276 [INFO] VIPS: selected loader is image source
2025-08-16 13:27:42,276 [INFO] VIPS: input size is 11520 x 14400
2025-08-16 13:27:42,276 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-16 13:27:42,276 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-16 13:27:42,277 [INFO] VIPS: converting to processing space srgb
2025-08-16 13:27:42,277 [INFO] VIPS: residual reducev by 0.416667
2025-08-16 13:27:42,277 [INFO] VIPS: reducev: 15 point mask
2025-08-16 13:27:42,279 [INFO] VIPS: reducev: using vector path
2025-08-16 13:27:42,279 [INFO] VIPS: reducev sequential line cache
2025-08-16 13:27:42,279 [INFO] VIPS: residual reduceh by 0.416667
2025-08-16 13:27:42,279 [INFO] VIPS: reduceh: 15 point mask
2025-08-16 13:27:42,280 [INFO] VIPS: converting to output space srgb
2025-08-16 13:27:45,447 [INFO] Determined aspect ratio for RJC-00312-original.jpg: 4x5
2025-08-16 13:27:50,039 [ERROR] Page not found (404): http://artnarrator.com/analyze/4x5/RJC-00312.jpg
2025-08-16 13:40:24,611 [ERROR] Page not found (404): http://artnarrator.com/analyze/4x5/RJC-00312.jpg
2025-08-16 13:43:42,478 [INFO] Assigned new SKU: RJC-00313. Tracker file updated.
2025-08-16 13:43:42,511 [INFO] VIPS: selected loader is image source
2025-08-16 13:43:42,511 [INFO] VIPS: input size is 11520 x 14400
2025-08-16 13:43:42,511 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-16 13:43:42,511 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-16 13:43:42,511 [INFO] VIPS: converting to processing space srgb
2025-08-16 13:43:42,512 [INFO] VIPS: residual reducev by 0.416667
2025-08-16 13:43:42,512 [INFO] VIPS: reducev: 15 point mask
2025-08-16 13:43:42,513 [INFO] VIPS: reducev: using vector path
2025-08-16 13:43:42,513 [INFO] VIPS: reducev sequential line cache
2025-08-16 13:43:42,513 [INFO] VIPS: residual reduceh by 0.416667
2025-08-16 13:43:42,513 [INFO] VIPS: reduceh: 15 point mask
2025-08-16 13:43:42,514 [INFO] VIPS: converting to output space srgb
2025-08-16 13:43:45,642 [INFO] Determined aspect ratio for RJC-00313-original.jpg: 4x5
2025-08-16 13:43:50,052 [ERROR] Page not found (404): http://artnarrator.com/analyze/4x5/RJC-00313.jpg
2025-08-16 14:10:58,687 [INFO] Assigned new SKU: RJC-00314. Tracker file updated.
2025-08-16 14:11:00,924 [INFO] VIPS: selected loader is image source
2025-08-16 14:11:00,924 [INFO] VIPS: input size is 11520 x 14400
2025-08-16 14:11:00,924 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-16 14:11:00,924 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-16 14:11:00,924 [INFO] VIPS: converting to processing space srgb
2025-08-16 14:11:00,925 [INFO] VIPS: residual reducev by 0.263889
2025-08-16 14:11:00,925 [INFO] VIPS: reducev: 23 point mask
2025-08-16 14:11:00,927 [INFO] VIPS: reducev: using vector path
2025-08-16 14:11:00,927 [INFO] VIPS: reducev sequential line cache
2025-08-16 14:11:00,927 [INFO] VIPS: residual reduceh by 0.263889
2025-08-16 14:11:00,927 [INFO] VIPS: reduceh: 23 point mask
2025-08-16 14:11:00,928 [INFO] VIPS: converting to output space srgb
2025-08-16 14:11:04,202 [ERROR] Page not found (404): http://artnarrator.com/unanalysed-img/RJC-00314/RJC-00314-thumb.jpg
2025-08-16 14:11:10,209 [ERROR] Page not found (404): http://artnarrator.com/analyze/4x5/RJC-00314.jpg
2025-08-16 14:11:16,588 [ERROR] Page not found (404): http://artnarrator.com/analyze/4x5/RJC-00313.jpg
2025-08-16 14:11:16,588 [ERROR] Could not write to session registry file at logs/session_registry.json: [Errno 2] No such file or directory: 'logs/session_registry.tmp' -> 'logs/session_registry.json'
2025-08-16 14:11:23,211 [ERROR] Page not found (404): http://artnarrator.com/unanalysed-img/RJC-00314/RJC-00314-thumb.jpg
2025-08-16 14:25:23,341 [INFO] Initiating deletion for artwork: 'artwork-rjc-99999-by-robin-custance-rjc-rjc-99999'
2025-08-16 14:25:23,342 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-99999-by-robin-custance-rjc-rjc-99999
2025-08-16 14:25:23,342 [INFO] No OUTPUT_JSON configured; nothing to remove for artwork-rjc-99999-by-robin-custance-rjc-rjc-99999
2025-08-16 14:25:23,342 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-99999-by-robin-custance-rjc-rjc-99999'
2025-08-16 14:58:43,501 [WARNING] Attempted to touch an invalid or expired session '96687d21-d1bf-478d-bbb4-edda46c283d3' for user 'robbie'.
2025-08-16 14:58:57,215 [INFO] Registered new session b2b32c39-6167-42c0-af38-772c546e41c1 for user 'robbie'.
2025-08-16 14:58:57,224 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-16 14:59:07,385 [INFO] Initiating deletion for artwork: 'artwork-rjc-test00-by-robin-custance-rjc-rjc-test00'
2025-08-16 14:59:07,387 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-test00-by-robin-custance-rjc-rjc-test00
2025-08-16 14:59:07,388 [INFO] No OUTPUT_JSON configured; nothing to remove for artwork-rjc-test00-by-robin-custance-rjc-rjc-test00
2025-08-16 14:59:07,388 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-test00-by-robin-custance-rjc-rjc-test00'
2025-08-16 14:59:38,334 [INFO] Assigned new SKU: RJC-00325. Tracker file updated.
2025-08-16 14:59:40,533 [INFO] VIPS: selected loader is image source
2025-08-16 14:59:40,536 [INFO] VIPS: input size is 11520 x 14400
2025-08-16 14:59:40,536 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-16 14:59:40,537 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-16 14:59:40,537 [INFO] VIPS: converting to processing space srgb
2025-08-16 14:59:40,537 [INFO] VIPS: residual reducev by 0.263889
2025-08-16 14:59:40,538 [INFO] VIPS: reducev: 23 point mask
2025-08-16 14:59:40,544 [INFO] VIPS: reducev: using vector path
2025-08-16 14:59:40,544 [INFO] VIPS: reducev sequential line cache
2025-08-16 14:59:40,545 [INFO] VIPS: residual reduceh by 0.263889
2025-08-16 14:59:40,545 [INFO] VIPS: reduceh: 23 point mask
2025-08-16 14:59:40,545 [INFO] VIPS: converting to output space srgb
2025-08-16 14:59:43,908 [ERROR] Page not found (404): http://artnarrator.com/unanalysed-img/RJC-00325/RJC-00325-thumb.jpg
2025-08-16 15:00:50,138 [INFO] Assigned new SKU: RJC-00326. Tracker file updated.
2025-08-16 15:00:52,167 [INFO] VIPS: selected loader is image source
2025-08-16 15:00:52,167 [INFO] VIPS: input size is 11520 x 14400
2025-08-16 15:00:52,167 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-16 15:00:52,167 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-16 15:00:52,168 [INFO] VIPS: converting to processing space srgb
2025-08-16 15:00:52,168 [INFO] VIPS: residual reducev by 0.263889
2025-08-16 15:00:52,168 [INFO] VIPS: reducev: 23 point mask
2025-08-16 15:00:52,170 [INFO] VIPS: reducev: using vector path
2025-08-16 15:00:52,170 [INFO] VIPS: reducev sequential line cache
2025-08-16 15:00:52,170 [INFO] VIPS: residual reduceh by 0.263889
2025-08-16 15:00:52,170 [INFO] VIPS: reduceh: 23 point mask
2025-08-16 15:00:52,171 [INFO] VIPS: converting to output space srgb
2025-08-16 15:00:55,295 [ERROR] Page not found (404): http://artnarrator.com/unanalysed-img/RJC-00326/RJC-00326-thumb.jpg
2025-08-16 15:01:31,183 [ERROR] Page not found (404): http://artnarrator.com/unanalysed/RJC-00326/RJC-00326-thumb.jpg
2025-08-16 17:28:27,360 [WARNING] Attempted to touch an invalid or expired session 'b2b32c39-6167-42c0-af38-772c546e41c1' for user 'robbie'.
2025-08-16 17:35:20,094 [ERROR] Page not found (404): http://localhost/static/art-processing/processed-artwork/RJC-00326-original.jpg
2025-08-16 18:19:05,768 [INFO] Registered new session 752a2f6c-0340-4fef-984c-407ff9fb8eb9 for user 'robbie'.
2025-08-16 18:19:05,775 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-16 18:25:01,879 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-16 18:28:52,591 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-16 18:31:23,589 [INFO] Assigned new SKU: RJC-00376. Tracker file updated.
2025-08-16 18:31:25,788 [INFO] VIPS: selected loader is image source
2025-08-16 18:31:25,788 [INFO] VIPS: input size is 11520 x 14400
2025-08-16 18:31:25,788 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-16 18:31:25,789 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-16 18:31:25,789 [INFO] VIPS: converting to processing space srgb
2025-08-16 18:31:25,789 [INFO] VIPS: residual reducev by 0.263889
2025-08-16 18:31:25,789 [INFO] VIPS: reducev: 23 point mask
2025-08-16 18:31:25,791 [INFO] VIPS: reducev: using vector path
2025-08-16 18:31:25,791 [INFO] VIPS: reducev sequential line cache
2025-08-16 18:31:25,791 [INFO] VIPS: residual reduceh by 0.263889
2025-08-16 18:31:25,791 [INFO] VIPS: reduceh: 23 point mask
2025-08-16 18:31:25,792 [INFO] VIPS: converting to output space srgb
2025-08-16 18:31:39,874 [INFO] Initiating deletion for artwork: 'artwork-rjc-00376-by-robin-custance-rjc-rjc-00376'
2025-08-16 18:31:39,883 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-00376-by-robin-custance-rjc-rjc-00376
2025-08-16 18:31:39,883 [INFO] No OUTPUT_JSON configured; nothing to remove for artwork-rjc-00376-by-robin-custance-rjc-rjc-00376
2025-08-16 18:31:39,883 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-00376-by-robin-custance-rjc-rjc-00376'
2025-08-16 18:31:47,885 [INFO] Initiating deletion for artwork: 'artwork-rjc-0338-by-robin-custance-rjc-rjc-0338'
2025-08-16 18:31:47,885 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0338-by-robin-custance-rjc-rjc-0338
2025-08-16 18:31:47,886 [INFO] No OUTPUT_JSON configured; nothing to remove for artwork-rjc-0338-by-robin-custance-rjc-rjc-0338
2025-08-16 18:31:47,886 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0338-by-robin-custance-rjc-rjc-0338'
2025-08-16 18:31:51,146 [INFO] Initiating deletion for artwork: 'artwork-rjc-0341-by-robin-custance-rjc-rjc-0341'
2025-08-16 18:31:51,147 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0341-by-robin-custance-rjc-rjc-0341
2025-08-16 18:31:51,147 [INFO] No OUTPUT_JSON configured; nothing to remove for artwork-rjc-0341-by-robin-custance-rjc-rjc-0341
2025-08-16 18:31:51,147 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0341-by-robin-custance-rjc-rjc-0341'
2025-08-16 18:31:54,654 [INFO] Initiating deletion for artwork: 'artwork-rjc-0342-by-robin-custance-rjc-rjc-0342'
2025-08-16 18:31:54,655 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0342-by-robin-custance-rjc-rjc-0342
2025-08-16 18:31:54,655 [INFO] No OUTPUT_JSON configured; nothing to remove for artwork-rjc-0342-by-robin-custance-rjc-rjc-0342
2025-08-16 18:31:54,655 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0342-by-robin-custance-rjc-rjc-0342'
2025-08-16 20:42:29,382 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg provider=openai
2025-08-16 20:42:29,382 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg --json-output
2025-08-16 20:42:29,579 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0412-by-robin-custance-rjc-rjc-0412
2025-08-16 20:42:29,619 [ERROR] Composite generation subprocess failed; continuing without blocking analysis response
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 627, in analyze_artwork_by_filename
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 268, in _generate_composites
    raise RuntimeError(f"Composite generation failed ({result.returncode}): {result.stderr.strip()}")
RuntimeError: Composite generation failed (1): Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'
2025-08-16 20:42:58,438 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg provider=openai
2025-08-16 20:42:58,438 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg --json-output
2025-08-16 20:42:58,608 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0413-by-robin-custance-rjc-rjc-0413
2025-08-16 20:42:58,667 [ERROR] Composite generation subprocess failed; continuing without blocking analysis response
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 627, in analyze_artwork_by_filename
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 268, in _generate_composites
    raise RuntimeError(f"Composite generation failed ({result.returncode}): {result.stderr.strip()}")
RuntimeError: Composite generation failed (1): Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'
2025-08-16 20:48:38,102 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg provider=openai
2025-08-16 20:48:38,102 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg --json-output
2025-08-16 20:48:38,103 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/cassowary-test-01-test-run
2025-08-16 20:49:15,514 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg provider=openai
2025-08-16 20:49:15,515 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg --json-output
2025-08-16 20:49:15,767 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0419-by-robin-custance-rjc-rjc-0419
2025-08-16 20:49:15,827 [ERROR] Composite generation subprocess failed; continuing without blocking analysis response
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 627, in analyze_artwork_by_filename
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 268, in _generate_composites
    raise RuntimeError(f"Composite generation failed ({result.returncode}): {result.stderr.strip()}")
RuntimeError: Composite generation failed (1): Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'
2025-08-16 20:50:19,499 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg provider=openai
2025-08-16 20:50:19,499 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg --json-output
2025-08-16 20:50:19,718 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0420-by-robin-custance-rjc-rjc-0420
2025-08-16 20:50:19,759 [ERROR] Composite generation subprocess failed; continuing without blocking analysis response
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 627, in analyze_artwork_by_filename
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 268, in _generate_composites
    raise RuntimeError(f"Composite generation failed ({result.returncode}): {result.stderr.strip()}")
RuntimeError: Composite generation failed (1): Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'
2025-08-16 20:54:08,220 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg provider=openai
2025-08-16 20:54:08,220 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg --json-output
2025-08-16 20:54:08,427 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0426-by-robin-custance-rjc-rjc-0426
2025-08-16 20:54:08,468 [ERROR] Composite generation subprocess failed; continuing without blocking analysis response
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 646, in analyze_artwork_by_filename
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 268, in _generate_composites
    raise RuntimeError(f"Composite generation failed ({result.returncode}): {result.stderr.strip()}")
RuntimeError: Composite generation failed (1): Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'
2025-08-16 20:57:02,053 [WARNING] Attempted to touch an invalid or expired session '752a2f6c-0340-4fef-984c-407ff9fb8eb9' for user 'robbie'.
2025-08-16 21:00:06,040 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg provider=openai
2025-08-16 21:00:06,040 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg --json-output
2025-08-16 21:00:06,255 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0427-by-robin-custance-rjc-rjc-0427
2025-08-16 21:00:06,298 [ERROR] Composite generation subprocess failed; continuing without blocking analysis response
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 646, in analyze_artwork_by_filename
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 268, in _generate_composites
    raise RuntimeError(f"Composite generation failed ({result.returncode}): {result.stderr.strip()}")
RuntimeError: Composite generation failed (1): Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'
2025-08-16 21:07:10,270 [INFO] [DEBUG] _run_ai_analysis: img_path=/home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg provider=openai
2025-08-16 21:07:10,270 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /home/artnarrator/artnarrator.com/art-processing/unanalysed-artwork/cassowary-test-01-test-run/cassowary-test-01-test-run.jpg --json-output
2025-08-16 21:07:10,489 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0428-by-robin-custance-rjc-rjc-0428
2025-08-16 21:07:10,531 [ERROR] Composite generation subprocess failed; continuing without blocking analysis response
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 646, in analyze_artwork_by_filename
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 268, in _generate_composites
    raise RuntimeError(f"Composite generation failed ({result.returncode}): {result.stderr.strip()}")
RuntimeError: Composite generation failed (1): Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'
2025-08-17 12:43:19,987 [INFO] Cleaned up expired sessions from registry.
2025-08-17 12:43:19,988 [INFO] Registered new session 8baf8f74-9d27-414b-81ab-ccfc0ae2d159 for user 'robbie'.
2025-08-17 12:43:19,994 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 12:43:21,076 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-17 12:45:11,462 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:11,465 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:14,856 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:14,867 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:16,844 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:16,850 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:18,983 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:18,986 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:21,105 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:21,108 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:23,513 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:23,519 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:25,893 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:25,898 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:29,011 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:29,012 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:30,630 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:30,633 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:31,966 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:31,970 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:33,668 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:33,678 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:35,199 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:35,205 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:36,700 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:36,704 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:45:39,365 [INFO] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-08-17 12:45:39,369 [INFO] AI successfully rewrote text based on prompt.
2025-08-17 12:46:48,681 [ERROR] BuildError (missing endpoint): Could not build url for endpoint 'artwork.analyze_artwork' with values ['aspect', 'filename']. Did you mean 'artwork.analyze_artwork_route' instead?
2025-08-17 13:18:19,784 [INFO] Assigned new SKU: RJC-0429. Tracker file updated.
2025-08-17 13:18:21,891 [INFO] VIPS: selected loader is image source
2025-08-17 13:18:21,891 [INFO] VIPS: input size is 11520 x 14400
2025-08-17 13:18:21,891 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-17 13:18:21,892 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-17 13:18:21,892 [INFO] VIPS: converting to processing space srgb
2025-08-17 13:18:21,892 [INFO] VIPS: residual reducev by 0.263889
2025-08-17 13:18:21,892 [INFO] VIPS: reducev: 23 point mask
2025-08-17 13:18:21,894 [INFO] VIPS: reducev: using vector path
2025-08-17 13:18:21,894 [INFO] VIPS: reducev sequential line cache
2025-08-17 13:18:21,894 [INFO] VIPS: residual reduceh by 0.263889
2025-08-17 13:18:21,894 [INFO] VIPS: reduceh: 23 point mask
2025-08-17 13:18:21,895 [INFO] VIPS: converting to output space srgb
2025-08-17 13:21:20,900 [INFO] Initiating deletion for artwork: 'artwork-rjc-0429-by-robin-custance-rjc-rjc-0429'
2025-08-17 13:21:20,907 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0429-by-robin-custance-rjc-rjc-0429
2025-08-17 13:21:20,907 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0429-by-robin-custance-rjc-rjc-0429'
2025-08-17 13:54:41,765 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 13:54:41,767 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 13:54:42,018 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 13:54:42,722 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 13:54:43,862 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 13:54:44,491 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 13:54:47,155 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 13:54:47,186 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:54:47,281 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:54:47,409 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 13:54:47,412 [INFO] Removed session b71eda92-5227-490d-8534-4ab032c1c1ac for user 'robbie'.
2025-08-17 13:54:47,412 [INFO] Removed session e4d38d42-2807-4bf4-9709-e2a8107ecfd1 for user 'robbie'.
2025-08-17 13:54:47,506 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:54:47,512 [INFO] Registered new session 3f065e43-e8ff-4caa-9ab5-b371d1985716 for user 'viewer'.
2025-08-17 13:54:47,517 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 13:54:47,520 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 13:54:47,522 [INFO] Removed session 3f065e43-e8ff-4caa-9ab5-b371d1985716 for user 'viewer'.
2025-08-17 13:54:47,522 [INFO] User 'viewer' logged out and session '3f065e43-e8ff-4caa-9ab5-b371d1985716' was removed.
2025-08-17 13:54:47,615 [INFO] Registered new session 066b2354-db7a-4994-9f87-e718c078087c for user 'robbie'.
2025-08-17 13:54:47,620 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:47,663 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:54:47,758 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:54:47,784 [INFO] Removed session 066b2354-db7a-4994-9f87-e718c078087c for user 'robbie'.
2025-08-17 13:54:47,881 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:54:47,887 [INFO] Registered new session de5b425d-fa99-4de2-a66a-b60ab14bc16a for user 'robbie'.
2025-08-17 13:54:47,891 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:47,897 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 13:54:47,939 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:54:48,034 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:54:48,157 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 13:54:48,157 [INFO] Removed session de5b425d-fa99-4de2-a66a-b60ab14bc16a for user 'robbie'.
2025-08-17 13:54:48,251 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:54:48,258 [INFO] Registered new session c9e7ebe8-c47f-4c4b-9b2e-73a89db6367a for user 'robbie'.
2025-08-17 13:54:48,262 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:48,268 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 13:54:48,269 [INFO] Removed session c9e7ebe8-c47f-4c4b-9b2e-73a89db6367a for user 'robbie'.
2025-08-17 13:54:48,270 [INFO] User 'robbie' logged out and session 'c9e7ebe8-c47f-4c4b-9b2e-73a89db6367a' was removed.
2025-08-17 13:54:48,372 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 13:54:48,387 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-41/test_load_json_file_safe_missi0/missing.json
2025-08-17 13:54:48,388 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-41/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 13:54:48,390 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-41/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 13:54:48,488 [INFO] Registered new session cbfcb600-b564-4049-8802-8b6b972b6234 for user 'robbie'.
2025-08-17 13:54:48,493 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:48,520 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 13:54:48,524 [INFO] Removed session cbfcb600-b564-4049-8802-8b6b972b6234 for user 'robbie'.
2025-08-17 13:54:48,618 [INFO] Registered new session 7aa21db6-0f88-4191-b6a3-0fad2e600c17 for user 'robbie'.
2025-08-17 13:54:48,622 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:48,629 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 13:54:48,633 [INFO] Removed session 7aa21db6-0f88-4191-b6a3-0fad2e600c17 for user 'robbie'.
2025-08-17 13:54:48,726 [INFO] Registered new session 1b43e07a-f267-47a6-b8e1-c8aa72001520 for user 'robbie'.
2025-08-17 13:54:48,731 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:48,737 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 13:54:48,743 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-41/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 13:54:48,743 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-41/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 13:54:48,743 [ERROR] JSON decode error: Expecting value: line 1 column 1 (char 0)
2025-08-17 13:54:48,744 [ERROR] ❌ Error running analysis: AI analysis output could not be parsed.
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 252, in _run_ai_analysis
    return json.loads(result.stdout.strip())
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 255, in _run_ai_analysis
    raise RuntimeError("AI analysis output could not be parsed.") from e
RuntimeError: AI analysis output could not be parsed.
2025-08-17 13:54:48,882 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-41/art_processing_test0
2025-08-17 13:54:48,882 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 13:54:48,883 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-41/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 13:54:48,883 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 13:54:48,883 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-41/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-41/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:54:48,883 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 13:54:48,884 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-41/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-41/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:54:48,884 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 13:54:48,884 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-41/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-41/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:54:48,884 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 13:54:48,885 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-41/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 13:54:48,885 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 13:54:48,885 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 13:54:48,885 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-41/art_processing_test0
2025-08-17 13:54:48,894 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-41/test_move_and_registry0/registry.json
2025-08-17 13:54:48,894 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 13:54:48,992 [INFO] Registered new session aaec1f6d-c8f5-4733-99f7-c2cc08b0477e for user 'robbie'.
2025-08-17 13:54:48,997 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:49,688 [INFO] Sellbrite authentication succeeded
2025-08-17 13:54:51,227 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 13:54:51,228 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 13:54:51,228 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 13:54:51,229 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 13:54:51,229 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 13:54:51,229 [ERROR] Analysis script not found: no such file
2025-08-17 13:54:51,352 [INFO] Registered new session 5752927e-79fd-49a6-b282-3b5798d5f8a0 for user 'robbie'.
2025-08-17 13:54:51,356 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:51,465 [INFO] Registered new session 412323ed-d196-4f37-9cbe-58ace218625c for user 'robbie'.
2025-08-17 13:54:51,469 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:51,565 [INFO] Registered new session 4a667b24-5fdd-4349-8993-6725ec81285f for user 'robbie'.
2025-08-17 13:54:51,569 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:51,665 [INFO] Registered new session 7a840ab1-028b-445c-a7fe-a1730b9638ac for user 'robbie'.
2025-08-17 13:54:51,669 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:51,766 [INFO] Registered new session be6a85c0-8910-4aef-83ca-7145bdb2e7b5 for user 'robbie'.
2025-08-17 13:54:51,770 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:51,867 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 13:54:51,867 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 13:54:51,872 [INFO] Removed session 5752927e-79fd-49a6-b282-3b5798d5f8a0 for user 'robbie'.
2025-08-17 13:54:51,873 [INFO] User 'robbie' logged out and session '5752927e-79fd-49a6-b282-3b5798d5f8a0' was removed.
2025-08-17 13:54:51,968 [INFO] Registered new session 0d001b57-ecb8-409b-839a-de8d7af4c672 for user 'robbie'.
2025-08-17 13:54:51,972 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:54:51,980 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 13:54:51,980 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 13:54:51,982 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 13:54:51,985 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 13:54:52,124 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 13:54:52,128 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 13:54:52,129 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 13:54:52,130 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 13:54:52,141 [INFO] Assigned new SKU: RJC-0455. Tracker file updated.
2025-08-17 13:56:29,573 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 13:56:29,575 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 13:56:29,861 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 13:56:30,193 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 13:56:31,338 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 13:56:31,983 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 13:56:34,578 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 13:56:34,608 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:56:34,705 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:56:34,829 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 13:56:34,832 [INFO] Removed session 1b43e07a-f267-47a6-b8e1-c8aa72001520 for user 'robbie'.
2025-08-17 13:56:34,833 [INFO] Removed session aaec1f6d-c8f5-4733-99f7-c2cc08b0477e for user 'robbie'.
2025-08-17 13:56:34,926 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:56:34,933 [INFO] Registered new session 2c90d457-9d6c-451e-a249-0ee5386d6292 for user 'viewer'.
2025-08-17 13:56:34,938 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 13:56:34,941 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 13:56:34,943 [INFO] Removed session 2c90d457-9d6c-451e-a249-0ee5386d6292 for user 'viewer'.
2025-08-17 13:56:34,943 [INFO] User 'viewer' logged out and session '2c90d457-9d6c-451e-a249-0ee5386d6292' was removed.
2025-08-17 13:56:35,043 [INFO] Registered new session 3c16f3b7-8c49-494c-bb72-9e4619fa21e1 for user 'robbie'.
2025-08-17 13:56:35,047 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:35,091 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:56:35,186 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:56:35,214 [INFO] Removed session 3c16f3b7-8c49-494c-bb72-9e4619fa21e1 for user 'robbie'.
2025-08-17 13:56:35,313 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:56:35,319 [INFO] Registered new session 30b65dde-7659-474b-b4d2-1a1160b36bbe for user 'robbie'.
2025-08-17 13:56:35,323 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:35,329 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 13:56:35,375 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:56:35,473 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:56:35,593 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 13:56:35,594 [INFO] Removed session 30b65dde-7659-474b-b4d2-1a1160b36bbe for user 'robbie'.
2025-08-17 13:56:35,689 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:56:35,696 [INFO] Registered new session 36337121-a0b3-4b1e-adc4-1c15f46a642c for user 'robbie'.
2025-08-17 13:56:35,700 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:35,706 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 13:56:35,708 [INFO] Removed session 36337121-a0b3-4b1e-adc4-1c15f46a642c for user 'robbie'.
2025-08-17 13:56:35,708 [INFO] User 'robbie' logged out and session '36337121-a0b3-4b1e-adc4-1c15f46a642c' was removed.
2025-08-17 13:56:35,802 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 13:56:35,817 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-42/test_load_json_file_safe_missi0/missing.json
2025-08-17 13:56:35,819 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-42/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 13:56:35,820 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-42/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 13:56:35,924 [INFO] Registered new session d93bea13-7ae1-4ccc-8475-f2fc5f425539 for user 'robbie'.
2025-08-17 13:56:35,929 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:35,958 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 13:56:35,962 [INFO] Removed session d93bea13-7ae1-4ccc-8475-f2fc5f425539 for user 'robbie'.
2025-08-17 13:56:36,057 [INFO] Registered new session 6a636c24-87b6-4ac5-809d-56ae29077096 for user 'robbie'.
2025-08-17 13:56:36,062 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:36,068 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 13:56:36,072 [INFO] Removed session 6a636c24-87b6-4ac5-809d-56ae29077096 for user 'robbie'.
2025-08-17 13:56:36,193 [INFO] Registered new session 143e1762-8018-4147-ab50-4723c40b59dd for user 'robbie'.
2025-08-17 13:56:36,197 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:36,204 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 13:56:36,211 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-42/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 13:56:36,211 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-42/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 13:56:36,212 [ERROR] JSON decode error: Expecting value: line 1 column 1 (char 0)
2025-08-17 13:56:36,212 [ERROR] ❌ Error running analysis: AI analysis output could not be parsed.
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 252, in _run_ai_analysis
    return json.loads(result.stdout.strip())
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 255, in _run_ai_analysis
    raise RuntimeError("AI analysis output could not be parsed.") from e
RuntimeError: AI analysis output could not be parsed.
2025-08-17 13:56:36,355 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-42/art_processing_test0
2025-08-17 13:56:36,356 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 13:56:36,356 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-42/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 13:56:36,356 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 13:56:36,357 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-42/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-42/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:56:36,357 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 13:56:36,357 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-42/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-42/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:56:36,357 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 13:56:36,358 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-42/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-42/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:56:36,358 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 13:56:36,358 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-42/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 13:56:36,358 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 13:56:36,358 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 13:56:36,359 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-42/art_processing_test0
2025-08-17 13:56:36,368 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-42/test_move_and_registry0/registry.json
2025-08-17 13:56:36,369 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 13:56:36,500 [INFO] Registered new session 64843237-bdea-4338-ac99-daaabaa8d731 for user 'robbie'.
2025-08-17 13:56:36,505 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:37,206 [INFO] Sellbrite authentication succeeded
2025-08-17 13:56:38,719 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 13:56:38,719 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 13:56:38,719 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 13:56:38,721 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 13:56:38,721 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 13:56:38,721 [ERROR] Analysis script not found: no such file
2025-08-17 13:56:38,845 [INFO] Registered new session f2aae9de-e859-4198-9a5a-58c27a2d30c0 for user 'robbie'.
2025-08-17 13:56:38,850 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:38,966 [INFO] Registered new session aec708d5-4be5-4846-ad24-9ad9a24f32c7 for user 'robbie'.
2025-08-17 13:56:38,970 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:39,067 [INFO] Registered new session 97f216b3-9e68-4718-9bce-57e51506204e for user 'robbie'.
2025-08-17 13:56:39,070 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:39,168 [INFO] Registered new session a5261316-8404-41ac-9a00-5996a928e376 for user 'robbie'.
2025-08-17 13:56:39,172 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:39,270 [INFO] Registered new session 03f77c3f-c83c-4ee7-ab7c-6712aaf9532c for user 'robbie'.
2025-08-17 13:56:39,273 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:39,370 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 13:56:39,370 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 13:56:39,376 [INFO] Removed session f2aae9de-e859-4198-9a5a-58c27a2d30c0 for user 'robbie'.
2025-08-17 13:56:39,376 [INFO] User 'robbie' logged out and session 'f2aae9de-e859-4198-9a5a-58c27a2d30c0' was removed.
2025-08-17 13:56:39,472 [INFO] Registered new session b77e0aee-b1b1-443a-89a6-179d18a332e4 for user 'robbie'.
2025-08-17 13:56:39,475 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:56:39,483 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 13:56:39,483 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 13:56:39,485 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 13:56:39,488 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 13:56:39,631 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 13:56:39,636 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 13:56:39,637 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 13:56:39,637 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 13:56:39,648 [INFO] Assigned new SKU: RJC-0456. Tracker file updated.
2025-08-17 13:58:57,332 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 13:58:57,333 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 13:58:57,640 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 13:58:57,998 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 13:58:59,147 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 13:58:59,776 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 13:59:02,446 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 13:59:02,477 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:59:02,574 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:59:02,696 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 13:59:02,698 [INFO] Removed session 143e1762-8018-4147-ab50-4723c40b59dd for user 'robbie'.
2025-08-17 13:59:02,699 [INFO] Removed session 64843237-bdea-4338-ac99-daaabaa8d731 for user 'robbie'.
2025-08-17 13:59:02,797 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:59:02,803 [INFO] Registered new session cc9c972e-dde6-41b9-afff-1f59f54beaf3 for user 'viewer'.
2025-08-17 13:59:02,808 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 13:59:02,812 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 13:59:02,814 [INFO] Removed session cc9c972e-dde6-41b9-afff-1f59f54beaf3 for user 'viewer'.
2025-08-17 13:59:02,814 [INFO] User 'viewer' logged out and session 'cc9c972e-dde6-41b9-afff-1f59f54beaf3' was removed.
2025-08-17 13:59:02,908 [INFO] Registered new session cb1d9467-467b-43c1-8426-92a438a33adf for user 'robbie'.
2025-08-17 13:59:02,913 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:02,957 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:59:03,052 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:59:03,078 [INFO] Removed session cb1d9467-467b-43c1-8426-92a438a33adf for user 'robbie'.
2025-08-17 13:59:03,173 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:59:03,179 [INFO] Registered new session 4c0ae352-0082-47bc-9a40-203691aa0bbb for user 'robbie'.
2025-08-17 13:59:03,183 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:03,189 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 13:59:03,233 [INFO] Users table is empty. Creating default admin user.
2025-08-17 13:59:03,328 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 13:59:03,454 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 13:59:03,454 [INFO] Removed session 4c0ae352-0082-47bc-9a40-203691aa0bbb for user 'robbie'.
2025-08-17 13:59:03,551 [INFO] No site settings found in database; creating new default record.
2025-08-17 13:59:03,559 [INFO] Registered new session 5d96f6a5-11e3-4750-8c63-78933418a4ed for user 'robbie'.
2025-08-17 13:59:03,563 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:03,569 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 13:59:03,571 [INFO] Removed session 5d96f6a5-11e3-4750-8c63-78933418a4ed for user 'robbie'.
2025-08-17 13:59:03,571 [INFO] User 'robbie' logged out and session '5d96f6a5-11e3-4750-8c63-78933418a4ed' was removed.
2025-08-17 13:59:03,665 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 13:59:03,680 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-43/test_load_json_file_safe_missi0/missing.json
2025-08-17 13:59:03,682 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-43/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 13:59:03,684 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-43/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 13:59:03,784 [INFO] Registered new session d75c6530-5b1d-447f-b6b4-549ca6fcab42 for user 'robbie'.
2025-08-17 13:59:03,788 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:03,816 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 13:59:03,820 [INFO] Removed session d75c6530-5b1d-447f-b6b4-549ca6fcab42 for user 'robbie'.
2025-08-17 13:59:03,915 [INFO] Registered new session 6c88ddf4-2693-4333-bac0-9b3af1d41748 for user 'robbie'.
2025-08-17 13:59:03,919 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:03,926 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 13:59:03,930 [INFO] Removed session 6c88ddf4-2693-4333-bac0-9b3af1d41748 for user 'robbie'.
2025-08-17 13:59:04,030 [INFO] Registered new session 313446fa-6ea6-4c30-8fc9-e3344e4da255 for user 'robbie'.
2025-08-17 13:59:04,035 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:04,043 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 13:59:04,171 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-43/art_processing_test0
2025-08-17 13:59:04,172 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 13:59:04,172 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-43/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 13:59:04,173 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 13:59:04,173 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-43/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-43/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:59:04,173 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 13:59:04,174 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-43/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-43/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:59:04,174 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 13:59:04,174 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-43/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-43/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 13:59:04,174 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 13:59:04,174 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-43/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 13:59:04,174 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 13:59:04,175 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 13:59:04,175 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-43/art_processing_test0
2025-08-17 13:59:04,184 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-43/test_move_and_registry0/registry.json
2025-08-17 13:59:04,184 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 13:59:04,311 [INFO] Registered new session b3f6acb9-4c43-4303-9353-807eaef9635a for user 'robbie'.
2025-08-17 13:59:04,316 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:04,986 [INFO] Sellbrite authentication succeeded
2025-08-17 13:59:06,515 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 13:59:06,515 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 13:59:06,515 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 13:59:06,516 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 13:59:06,516 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 13:59:06,517 [ERROR] Analysis script not found: no such file
2025-08-17 13:59:06,640 [INFO] Registered new session 0684487e-40d6-4d27-8090-4247d09a6049 for user 'robbie'.
2025-08-17 13:59:06,645 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:06,755 [INFO] Registered new session 0ca4d13a-5d3a-4144-bba4-ea7fce7b44d3 for user 'robbie'.
2025-08-17 13:59:06,759 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:06,865 [INFO] Registered new session 6d420010-8f4c-45fe-b908-1b87148126c7 for user 'robbie'.
2025-08-17 13:59:06,869 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:06,968 [INFO] Registered new session 8c1bc8b4-6f86-4540-9012-0be21092d64f for user 'robbie'.
2025-08-17 13:59:06,973 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:07,071 [INFO] Registered new session ca738d64-fa43-4f71-8dae-96100c807d7c for user 'robbie'.
2025-08-17 13:59:07,075 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:07,172 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 13:59:07,172 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 13:59:07,177 [INFO] Removed session 0684487e-40d6-4d27-8090-4247d09a6049 for user 'robbie'.
2025-08-17 13:59:07,178 [INFO] User 'robbie' logged out and session '0684487e-40d6-4d27-8090-4247d09a6049' was removed.
2025-08-17 13:59:07,273 [INFO] Registered new session aebb0856-219e-44ff-9494-078969f8033c for user 'robbie'.
2025-08-17 13:59:07,277 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 13:59:07,285 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 13:59:07,286 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 13:59:07,288 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 13:59:07,291 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 13:59:07,432 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 13:59:07,437 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 13:59:07,437 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 13:59:07,438 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 13:59:07,449 [INFO] Assigned new SKU: RJC-0457. Tracker file updated.
2025-08-17 14:05:06,731 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:05:06,732 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:05:07,015 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:05:07,354 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:05:08,489 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:05:09,123 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:05:11,818 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:05:11,849 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:05:11,944 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:05:12,068 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:05:12,071 [INFO] Removed session 313446fa-6ea6-4c30-8fc9-e3344e4da255 for user 'robbie'.
2025-08-17 14:05:12,072 [INFO] Removed session b3f6acb9-4c43-4303-9353-807eaef9635a for user 'robbie'.
2025-08-17 14:05:12,167 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:05:12,174 [INFO] Registered new session 273c1726-2313-4e67-82cb-9d45ed50f86a for user 'viewer'.
2025-08-17 14:05:12,179 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:05:12,182 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:05:12,184 [INFO] Removed session 273c1726-2313-4e67-82cb-9d45ed50f86a for user 'viewer'.
2025-08-17 14:05:12,184 [INFO] User 'viewer' logged out and session '273c1726-2313-4e67-82cb-9d45ed50f86a' was removed.
2025-08-17 14:05:12,278 [INFO] Registered new session 399a6c11-d4d4-4ffd-b026-82cc6b6d26b7 for user 'robbie'.
2025-08-17 14:05:12,282 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:12,328 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:05:12,425 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:05:12,453 [INFO] Removed session 399a6c11-d4d4-4ffd-b026-82cc6b6d26b7 for user 'robbie'.
2025-08-17 14:05:12,550 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:05:12,556 [INFO] Registered new session 698982ae-8466-490a-b689-627c47676aba for user 'robbie'.
2025-08-17 14:05:12,561 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:12,567 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:05:12,612 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:05:12,708 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:05:12,829 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:05:12,830 [INFO] Removed session 698982ae-8466-490a-b689-627c47676aba for user 'robbie'.
2025-08-17 14:05:12,926 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:05:12,933 [INFO] Registered new session 1faa82b7-ae74-441b-b49e-1c0e2e85ca28 for user 'robbie'.
2025-08-17 14:05:12,937 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:12,943 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:05:12,945 [INFO] Removed session 1faa82b7-ae74-441b-b49e-1c0e2e85ca28 for user 'robbie'.
2025-08-17 14:05:12,945 [INFO] User 'robbie' logged out and session '1faa82b7-ae74-441b-b49e-1c0e2e85ca28' was removed.
2025-08-17 14:05:13,040 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:05:13,055 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-44/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:05:13,057 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-44/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:05:13,059 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-44/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:05:13,158 [INFO] Registered new session fdeeaf88-bcdc-4d23-94ab-8cfc40ef29f8 for user 'robbie'.
2025-08-17 14:05:13,163 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:13,190 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:05:13,195 [INFO] Removed session fdeeaf88-bcdc-4d23-94ab-8cfc40ef29f8 for user 'robbie'.
2025-08-17 14:05:13,289 [INFO] Registered new session 744a64e1-cbdf-4cec-aaf6-16636621cbce for user 'robbie'.
2025-08-17 14:05:13,294 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:13,300 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:05:13,304 [INFO] Removed session 744a64e1-cbdf-4cec-aaf6-16636621cbce for user 'robbie'.
2025-08-17 14:05:13,399 [INFO] Registered new session 496cadaa-bb7f-4135-ad4b-0318469445c5 for user 'robbie'.
2025-08-17 14:05:13,403 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:13,409 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:05:13,415 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-44/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:05:13,415 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-44/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:05:13,415 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-44/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:05:13,416 [ERROR] Composite generation subprocess failed; continuing without blocking analysis response
Traceback (most recent call last):
  File "/usr/lib/python3.11/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/conftest.py", line 92, in communicate
    img_path = Path(self.args[0][2])
                    ~~~~~~~~~~~~^^^
IndexError: list index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 646, in analyze_artwork_by_filename
    _generate_composites(uuid.uuid4().hex)
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 262, in _generate_composites
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=config.BASE_DIR, timeout=600)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/subprocess.py", line 566, in run
    process.kill()
    ^^^^^^^^^^^^
AttributeError: '_DummyPopen' object has no attribute 'kill'
2025-08-17 14:05:13,552 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-44/art_processing_test0
2025-08-17 14:05:13,552 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:05:13,553 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-44/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:05:13,553 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:05:13,554 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-44/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-44/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:05:13,554 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:05:13,554 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-44/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-44/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:05:13,554 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:05:13,555 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-44/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-44/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:05:13,555 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:05:13,555 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-44/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:05:13,555 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:05:13,555 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:05:13,555 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-44/art_processing_test0
2025-08-17 14:05:13,564 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-44/test_move_and_registry0/registry.json
2025-08-17 14:05:13,565 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:05:13,666 [INFO] Registered new session 31e33033-504f-4549-85ca-bf4af0e34d6d for user 'robbie'.
2025-08-17 14:05:13,671 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:14,379 [INFO] Sellbrite authentication succeeded
2025-08-17 14:05:15,907 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:05:15,907 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:05:15,907 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:05:15,909 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:05:15,909 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:05:15,909 [ERROR] Analysis script not found: no such file
2025-08-17 14:05:16,059 [INFO] Registered new session 5a501b4b-99c6-42b6-996c-e304f3028d77 for user 'robbie'.
2025-08-17 14:05:16,063 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:16,174 [INFO] Registered new session 07b083ae-0ec2-4200-a8f5-943e97b7e3b1 for user 'robbie'.
2025-08-17 14:05:16,177 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:16,273 [INFO] Registered new session 162d9671-32c4-4dd9-8f9f-e1ee2bd1d3a2 for user 'robbie'.
2025-08-17 14:05:16,277 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:16,373 [INFO] Registered new session a8bd6880-571b-4f58-a0c7-884a8de9e54e for user 'robbie'.
2025-08-17 14:05:16,377 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:16,474 [INFO] Registered new session 7be2cb74-39e5-4e72-8018-58c00a2dbdf9 for user 'robbie'.
2025-08-17 14:05:16,478 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:16,574 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:05:16,574 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:05:16,580 [INFO] Removed session 5a501b4b-99c6-42b6-996c-e304f3028d77 for user 'robbie'.
2025-08-17 14:05:16,580 [INFO] User 'robbie' logged out and session '5a501b4b-99c6-42b6-996c-e304f3028d77' was removed.
2025-08-17 14:05:16,675 [INFO] Registered new session a628c0a9-5ad8-4117-b615-41902f421f66 for user 'robbie'.
2025-08-17 14:05:16,679 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:05:16,687 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:05:16,687 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:05:16,689 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:05:16,692 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:05:16,834 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:05:16,839 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:05:16,840 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:05:16,841 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:05:16,852 [INFO] Assigned new SKU: RJC-0458. Tracker file updated.
2025-08-17 14:06:31,806 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:06:31,807 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:06:32,095 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:06:32,397 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:06:33,533 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:06:34,180 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:06:36,786 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:06:36,815 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:06:36,911 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:06:37,031 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:06:37,034 [INFO] Removed session 496cadaa-bb7f-4135-ad4b-0318469445c5 for user 'robbie'.
2025-08-17 14:06:37,034 [INFO] Removed session 31e33033-504f-4549-85ca-bf4af0e34d6d for user 'robbie'.
2025-08-17 14:06:37,128 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:06:37,135 [INFO] Registered new session 2b031d74-abe9-4299-80f7-7d698c126575 for user 'viewer'.
2025-08-17 14:06:37,140 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:06:37,143 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:06:37,145 [INFO] Removed session 2b031d74-abe9-4299-80f7-7d698c126575 for user 'viewer'.
2025-08-17 14:06:37,146 [INFO] User 'viewer' logged out and session '2b031d74-abe9-4299-80f7-7d698c126575' was removed.
2025-08-17 14:06:37,240 [INFO] Registered new session 86db55b0-13ec-4590-b813-d38b1987e8fa for user 'robbie'.
2025-08-17 14:06:37,244 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:37,286 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:06:37,381 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:06:37,408 [INFO] Removed session 86db55b0-13ec-4590-b813-d38b1987e8fa for user 'robbie'.
2025-08-17 14:06:37,503 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:06:37,509 [INFO] Registered new session 215862af-23b9-4291-9bf0-62fe8680497d for user 'robbie'.
2025-08-17 14:06:37,513 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:37,518 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:06:37,561 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:06:37,657 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:06:37,788 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:06:37,789 [INFO] Removed session 215862af-23b9-4291-9bf0-62fe8680497d for user 'robbie'.
2025-08-17 14:06:37,883 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:06:37,890 [INFO] Registered new session d54bb873-70e0-49d7-9015-d1cb9d87ae5c for user 'robbie'.
2025-08-17 14:06:37,894 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:37,901 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:06:37,902 [INFO] Removed session d54bb873-70e0-49d7-9015-d1cb9d87ae5c for user 'robbie'.
2025-08-17 14:06:37,903 [INFO] User 'robbie' logged out and session 'd54bb873-70e0-49d7-9015-d1cb9d87ae5c' was removed.
2025-08-17 14:06:37,996 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:06:38,012 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-45/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:06:38,014 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-45/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:06:38,016 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-45/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:06:38,114 [INFO] Registered new session 64e7fa65-0b22-46ed-9c6e-1ddd59742532 for user 'robbie'.
2025-08-17 14:06:38,118 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:38,146 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:06:38,151 [INFO] Removed session 64e7fa65-0b22-46ed-9c6e-1ddd59742532 for user 'robbie'.
2025-08-17 14:06:38,245 [INFO] Registered new session d3ab13ff-79fa-426d-97d3-ab825201449e for user 'robbie'.
2025-08-17 14:06:38,250 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:38,256 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:06:38,260 [INFO] Removed session d3ab13ff-79fa-426d-97d3-ab825201449e for user 'robbie'.
2025-08-17 14:06:38,353 [INFO] Registered new session b5e59432-4ae2-4885-a725-aa8e95255e12 for user 'robbie'.
2025-08-17 14:06:38,358 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:38,364 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:06:38,370 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-45/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:06:38,370 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-45/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:06:38,371 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-45/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:06:38,508 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-45/art_processing_test0
2025-08-17 14:06:38,508 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:06:38,509 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-45/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:06:38,509 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:06:38,509 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-45/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-45/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:06:38,510 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:06:38,510 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-45/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-45/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:06:38,510 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:06:38,510 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-45/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-45/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:06:38,511 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:06:38,511 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-45/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:06:38,511 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:06:38,511 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:06:38,511 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-45/art_processing_test0
2025-08-17 14:06:38,520 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-45/test_move_and_registry0/registry.json
2025-08-17 14:06:38,520 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:06:38,621 [INFO] Registered new session e0579035-9a0f-4062-bfed-69b4883914d7 for user 'robbie'.
2025-08-17 14:06:38,627 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:39,335 [INFO] Sellbrite authentication succeeded
2025-08-17 14:06:40,840 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:06:40,840 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:06:40,840 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:06:40,841 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:06:40,841 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:06:40,842 [ERROR] Analysis script not found: no such file
2025-08-17 14:06:40,966 [INFO] Registered new session ff626c01-c214-4f9c-bd7e-1879d3a013e5 for user 'robbie'.
2025-08-17 14:06:40,970 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:41,078 [INFO] Registered new session 213a877f-6cb1-4690-a220-43a840b97c83 for user 'robbie'.
2025-08-17 14:06:41,082 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:41,179 [INFO] Registered new session 24283301-8052-468f-932d-b30c100b3de9 for user 'robbie'.
2025-08-17 14:06:41,182 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:41,278 [INFO] Registered new session 8c43e776-33db-46e8-af72-71f99c3668c5 for user 'robbie'.
2025-08-17 14:06:41,282 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:41,379 [INFO] Registered new session 9eefe083-9207-4dee-87ee-baf96b068922 for user 'robbie'.
2025-08-17 14:06:41,383 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:41,478 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:06:41,478 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:06:41,483 [INFO] Removed session ff626c01-c214-4f9c-bd7e-1879d3a013e5 for user 'robbie'.
2025-08-17 14:06:41,484 [INFO] User 'robbie' logged out and session 'ff626c01-c214-4f9c-bd7e-1879d3a013e5' was removed.
2025-08-17 14:06:41,579 [INFO] Registered new session dd64a8f3-8f3d-414b-b4ef-47d453932881 for user 'robbie'.
2025-08-17 14:06:41,583 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:06:41,590 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:06:41,591 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:06:41,592 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:06:41,595 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:06:41,739 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:06:41,744 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:06:41,744 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:06:41,745 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:06:41,756 [INFO] Assigned new SKU: RJC-0459. Tracker file updated.
2025-08-17 14:08:11,496 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:08:11,498 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:08:11,806 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:08:12,116 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:08:13,261 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:08:13,909 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:08:16,567 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:08:16,596 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:08:16,695 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:08:16,816 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:08:16,819 [INFO] Removed session b5e59432-4ae2-4885-a725-aa8e95255e12 for user 'robbie'.
2025-08-17 14:08:16,819 [INFO] Removed session e0579035-9a0f-4062-bfed-69b4883914d7 for user 'robbie'.
2025-08-17 14:08:16,914 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:08:16,921 [INFO] Registered new session d7871bac-90cf-4445-a4f7-835582a99fdc for user 'viewer'.
2025-08-17 14:08:16,926 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:08:16,929 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:08:16,931 [INFO] Removed session d7871bac-90cf-4445-a4f7-835582a99fdc for user 'viewer'.
2025-08-17 14:08:16,931 [INFO] User 'viewer' logged out and session 'd7871bac-90cf-4445-a4f7-835582a99fdc' was removed.
2025-08-17 14:08:17,026 [INFO] Registered new session 68310586-5781-48d9-9ee0-ac346fb41c07 for user 'robbie'.
2025-08-17 14:08:17,030 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:17,073 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:08:17,168 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:08:17,195 [INFO] Removed session 68310586-5781-48d9-9ee0-ac346fb41c07 for user 'robbie'.
2025-08-17 14:08:17,292 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:08:17,298 [INFO] Registered new session b72c5864-eb56-49ab-9224-5520e604cb9d for user 'robbie'.
2025-08-17 14:08:17,302 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:17,308 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:08:17,351 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:08:17,448 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:08:17,569 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:08:17,570 [INFO] Removed session b72c5864-eb56-49ab-9224-5520e604cb9d for user 'robbie'.
2025-08-17 14:08:17,664 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:08:17,671 [INFO] Registered new session 8d971e45-7944-4d65-9204-6d60fd10e722 for user 'robbie'.
2025-08-17 14:08:17,674 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:17,680 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:08:17,681 [INFO] Removed session 8d971e45-7944-4d65-9204-6d60fd10e722 for user 'robbie'.
2025-08-17 14:08:17,682 [INFO] User 'robbie' logged out and session '8d971e45-7944-4d65-9204-6d60fd10e722' was removed.
2025-08-17 14:08:17,775 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:08:17,791 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-46/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:08:17,793 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-46/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:08:17,794 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-46/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:08:17,893 [INFO] Registered new session b705af37-71a6-45c0-b523-73f3f4716a92 for user 'robbie'.
2025-08-17 14:08:17,897 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:17,924 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:08:17,928 [INFO] Removed session b705af37-71a6-45c0-b523-73f3f4716a92 for user 'robbie'.
2025-08-17 14:08:18,022 [INFO] Registered new session b4e6fb54-7cc5-4aa4-8420-45bf7ab120b2 for user 'robbie'.
2025-08-17 14:08:18,026 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:18,033 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:08:18,036 [INFO] Removed session b4e6fb54-7cc5-4aa4-8420-45bf7ab120b2 for user 'robbie'.
2025-08-17 14:08:18,132 [INFO] Registered new session bfb0b042-4606-4925-8558-f3bee7baf3c5 for user 'robbie'.
2025-08-17 14:08:18,136 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:18,142 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:08:18,149 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-46/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:08:18,149 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-46/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:08:18,149 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-46/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:08:18,286 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-46/art_processing_test0
2025-08-17 14:08:18,287 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:08:18,287 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-46/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:08:18,288 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:08:18,288 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-46/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-46/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:08:18,288 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:08:18,288 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-46/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-46/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:08:18,289 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:08:18,289 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-46/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-46/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:08:18,289 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:08:18,289 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-46/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:08:18,289 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:08:18,289 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:08:18,290 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-46/art_processing_test0
2025-08-17 14:08:18,300 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-46/test_move_and_registry0/registry.json
2025-08-17 14:08:18,300 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:08:18,399 [INFO] Registered new session 1fa63459-4344-4333-b5d8-376b9513ffd8 for user 'robbie'.
2025-08-17 14:08:18,404 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:19,077 [INFO] Sellbrite authentication succeeded
2025-08-17 14:08:20,579 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:08:20,579 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:08:20,579 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:08:20,581 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:08:20,581 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:08:20,581 [ERROR] Analysis script not found: no such file
2025-08-17 14:08:20,716 [INFO] Registered new session 052da9fe-dfcb-4871-a035-0e0c56e578d8 for user 'robbie'.
2025-08-17 14:08:20,721 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:20,832 [INFO] Registered new session 285db272-9ebc-46fe-958f-29c8af6f5b50 for user 'robbie'.
2025-08-17 14:08:20,835 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:20,933 [INFO] Registered new session 30bfe93f-87ca-4cfd-bcb6-c8d43013e241 for user 'robbie'.
2025-08-17 14:08:20,936 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:21,034 [INFO] Registered new session 9ef53600-2b60-4d5a-8fbc-2e9d0af38764 for user 'robbie'.
2025-08-17 14:08:21,038 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:21,136 [INFO] Registered new session 5d66b165-e84e-47e2-bf91-fa77c7b7b72f for user 'robbie'.
2025-08-17 14:08:21,141 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:21,240 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:08:21,240 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:08:21,245 [INFO] Removed session 052da9fe-dfcb-4871-a035-0e0c56e578d8 for user 'robbie'.
2025-08-17 14:08:21,246 [INFO] User 'robbie' logged out and session '052da9fe-dfcb-4871-a035-0e0c56e578d8' was removed.
2025-08-17 14:08:21,343 [INFO] Registered new session 922f0901-282a-404c-8d8b-f0d39c1ab791 for user 'robbie'.
2025-08-17 14:08:21,347 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:08:21,355 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:08:21,355 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:08:21,357 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:08:21,360 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:08:21,499 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:08:21,504 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:08:21,505 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:08:21,506 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:08:21,518 [INFO] Assigned new SKU: RJC-0460. Tracker file updated.
2025-08-17 14:10:39,670 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:10:39,672 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:10:40,136 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:10:40,448 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:10:41,588 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:10:42,212 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:10:44,876 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:10:44,906 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:10:45,002 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:10:45,123 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:10:45,126 [INFO] Removed session bfb0b042-4606-4925-8558-f3bee7baf3c5 for user 'robbie'.
2025-08-17 14:10:45,126 [INFO] Removed session 1fa63459-4344-4333-b5d8-376b9513ffd8 for user 'robbie'.
2025-08-17 14:10:45,220 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:10:45,226 [INFO] Registered new session ce6a3509-a47a-4d28-a614-20f3010fc40d for user 'viewer'.
2025-08-17 14:10:45,231 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:10:45,234 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:10:45,236 [INFO] Removed session ce6a3509-a47a-4d28-a614-20f3010fc40d for user 'viewer'.
2025-08-17 14:10:45,236 [INFO] User 'viewer' logged out and session 'ce6a3509-a47a-4d28-a614-20f3010fc40d' was removed.
2025-08-17 14:10:45,329 [INFO] Registered new session 48571a68-6877-4274-9942-2141c5a6d7e4 for user 'robbie'.
2025-08-17 14:10:45,333 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:45,378 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:10:45,473 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:10:45,501 [INFO] Removed session 48571a68-6877-4274-9942-2141c5a6d7e4 for user 'robbie'.
2025-08-17 14:10:45,596 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:10:45,603 [INFO] Registered new session d7eeadd6-dff6-471f-8a35-895a9cf2b28d for user 'robbie'.
2025-08-17 14:10:45,607 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:45,614 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:10:45,659 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:10:45,755 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:10:45,875 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:10:45,876 [INFO] Removed session d7eeadd6-dff6-471f-8a35-895a9cf2b28d for user 'robbie'.
2025-08-17 14:10:45,969 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:10:45,977 [INFO] Registered new session c12a4c9c-a32d-4f1f-9f7d-7bf465041c0e for user 'robbie'.
2025-08-17 14:10:45,981 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:45,987 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:10:45,989 [INFO] Removed session c12a4c9c-a32d-4f1f-9f7d-7bf465041c0e for user 'robbie'.
2025-08-17 14:10:45,989 [INFO] User 'robbie' logged out and session 'c12a4c9c-a32d-4f1f-9f7d-7bf465041c0e' was removed.
2025-08-17 14:10:46,082 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:10:46,098 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-47/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:10:46,100 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-47/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:10:46,102 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-47/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:10:46,202 [INFO] Registered new session c021d4ea-add3-41b0-8faf-cbef3167824c for user 'robbie'.
2025-08-17 14:10:46,207 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:46,234 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:10:46,238 [INFO] Removed session c021d4ea-add3-41b0-8faf-cbef3167824c for user 'robbie'.
2025-08-17 14:10:46,332 [INFO] Registered new session 1278ac59-ec72-4e72-abde-027bb0540c56 for user 'robbie'.
2025-08-17 14:10:46,337 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:46,344 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:10:46,348 [INFO] Removed session 1278ac59-ec72-4e72-abde-027bb0540c56 for user 'robbie'.
2025-08-17 14:10:46,441 [INFO] Registered new session 76a46ff1-137c-419d-a564-ac041c800289 for user 'robbie'.
2025-08-17 14:10:46,445 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:46,453 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:10:46,459 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-47/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:10:46,459 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-47/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:10:46,460 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-47/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:10:46,597 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-47/art_processing_test0
2025-08-17 14:10:46,598 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:10:46,598 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-47/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:10:46,598 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:10:46,599 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-47/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-47/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:10:46,599 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:10:46,599 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-47/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-47/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:10:46,599 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:10:46,600 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-47/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-47/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:10:46,600 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:10:46,600 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-47/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:10:46,600 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:10:46,600 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:10:46,601 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-47/art_processing_test0
2025-08-17 14:10:46,610 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-47/test_move_and_registry0/registry.json
2025-08-17 14:10:46,610 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:10:46,708 [INFO] Registered new session 7a42b291-39b7-4ad9-a2e8-91682e215a0e for user 'robbie'.
2025-08-17 14:10:46,713 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:47,377 [INFO] Sellbrite authentication succeeded
2025-08-17 14:10:48,885 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:10:48,885 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:10:48,885 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:10:48,887 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:10:48,887 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:10:48,887 [ERROR] Analysis script not found: no such file
2025-08-17 14:10:49,011 [INFO] Registered new session d12ea850-9de0-4538-9fdb-3218fd684535 for user 'robbie'.
2025-08-17 14:10:49,015 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:49,124 [INFO] Registered new session 6388ceea-5933-4556-a75a-fab7e24dc8d9 for user 'robbie'.
2025-08-17 14:10:49,129 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:49,226 [INFO] Registered new session d2d9c935-21dd-4256-84f6-240aac67c83b for user 'robbie'.
2025-08-17 14:10:49,230 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:49,328 [INFO] Registered new session 70635563-af5b-4018-bc64-d1241692a679 for user 'robbie'.
2025-08-17 14:10:49,332 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:49,430 [INFO] Registered new session 76e566a6-e7e8-4ce7-86ea-c88a099601e9 for user 'robbie'.
2025-08-17 14:10:49,435 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:49,536 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:10:49,536 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:10:49,541 [INFO] Removed session d12ea850-9de0-4538-9fdb-3218fd684535 for user 'robbie'.
2025-08-17 14:10:49,542 [INFO] User 'robbie' logged out and session 'd12ea850-9de0-4538-9fdb-3218fd684535' was removed.
2025-08-17 14:10:49,639 [INFO] Registered new session 80397178-a7ed-4634-b9d6-db56a23088e4 for user 'robbie'.
2025-08-17 14:10:49,643 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:10:49,651 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:10:49,651 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:10:49,653 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:10:49,656 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:10:49,800 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:10:49,805 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:10:49,805 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:10:49,806 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:10:49,817 [INFO] Assigned new SKU: RJC-0461. Tracker file updated.
2025-08-17 14:14:24,683 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:14:24,685 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:14:25,029 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:14:25,345 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:14:26,485 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:14:27,115 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:14:29,747 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:14:29,779 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:14:29,876 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:14:29,997 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:14:30,000 [INFO] Removed session 76a46ff1-137c-419d-a564-ac041c800289 for user 'robbie'.
2025-08-17 14:14:30,000 [INFO] Removed session 7a42b291-39b7-4ad9-a2e8-91682e215a0e for user 'robbie'.
2025-08-17 14:14:30,095 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:14:30,102 [INFO] Registered new session 6692ace6-a5ca-494e-91c8-b95462e5c3a7 for user 'viewer'.
2025-08-17 14:14:30,107 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:14:30,110 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:14:30,112 [INFO] Removed session 6692ace6-a5ca-494e-91c8-b95462e5c3a7 for user 'viewer'.
2025-08-17 14:14:30,112 [INFO] User 'viewer' logged out and session '6692ace6-a5ca-494e-91c8-b95462e5c3a7' was removed.
2025-08-17 14:14:30,205 [INFO] Registered new session 2aa1bfc7-1c49-45b7-beab-d35d123ea2f4 for user 'robbie'.
2025-08-17 14:14:30,210 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:30,254 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:14:30,350 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:14:30,377 [INFO] Removed session 2aa1bfc7-1c49-45b7-beab-d35d123ea2f4 for user 'robbie'.
2025-08-17 14:14:30,473 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:14:30,479 [INFO] Registered new session 784e8c2d-3a83-4ae6-ad47-f38f60f36d06 for user 'robbie'.
2025-08-17 14:14:30,483 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:30,489 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:14:30,533 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:14:30,630 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:14:30,750 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:14:30,751 [INFO] Removed session 784e8c2d-3a83-4ae6-ad47-f38f60f36d06 for user 'robbie'.
2025-08-17 14:14:30,855 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:14:30,862 [INFO] Registered new session f6ca4dcb-b7fd-4296-a843-40bded402bbf for user 'robbie'.
2025-08-17 14:14:30,866 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:30,872 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:14:30,874 [INFO] Removed session f6ca4dcb-b7fd-4296-a843-40bded402bbf for user 'robbie'.
2025-08-17 14:14:30,874 [INFO] User 'robbie' logged out and session 'f6ca4dcb-b7fd-4296-a843-40bded402bbf' was removed.
2025-08-17 14:14:30,967 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:14:30,983 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-48/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:14:30,984 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-48/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:14:30,986 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-48/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:14:31,084 [INFO] Registered new session 710158bb-0731-4dc6-accf-9bfa5332937a for user 'robbie'.
2025-08-17 14:14:31,089 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:31,116 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:14:31,120 [INFO] Removed session 710158bb-0731-4dc6-accf-9bfa5332937a for user 'robbie'.
2025-08-17 14:14:31,214 [INFO] Registered new session 78d8a91e-d8c6-4934-b959-1117a1248707 for user 'robbie'.
2025-08-17 14:14:31,219 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:31,226 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:14:31,229 [INFO] Removed session 78d8a91e-d8c6-4934-b959-1117a1248707 for user 'robbie'.
2025-08-17 14:14:31,323 [INFO] Registered new session 28da021d-7c7c-4ff1-8054-ae6f50bc9ac7 for user 'robbie'.
2025-08-17 14:14:31,328 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:31,335 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:14:31,341 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-48/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:14:31,341 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-48/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:14:31,342 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-48/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:14:31,477 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-48/art_processing_test0
2025-08-17 14:14:31,478 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:14:31,478 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-48/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:14:31,478 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:14:31,479 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-48/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-48/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:14:31,479 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:14:31,479 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-48/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-48/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:14:31,480 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:14:31,480 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-48/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-48/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:14:31,480 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:14:31,480 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-48/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:14:31,480 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:14:31,480 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:14:31,481 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-48/art_processing_test0
2025-08-17 14:14:31,490 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-48/test_move_and_registry0/registry.json
2025-08-17 14:14:31,490 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:14:31,608 [INFO] Registered new session 601fed3e-18c8-4582-bca2-36910bd5a865 for user 'robbie'.
2025-08-17 14:14:31,615 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:32,314 [INFO] Sellbrite authentication succeeded
2025-08-17 14:14:33,827 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:14:33,827 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:14:33,827 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:14:33,829 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:14:33,829 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:14:33,829 [ERROR] Analysis script not found: no such file
2025-08-17 14:14:33,952 [INFO] Registered new session 1d967f8e-b5bf-4d5b-914e-5d5509b2a0f1 for user 'robbie'.
2025-08-17 14:14:33,957 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:34,066 [INFO] Registered new session de2bd71a-0237-4533-85a8-45edbd2ecf2b for user 'robbie'.
2025-08-17 14:14:34,070 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:34,166 [INFO] Registered new session 41a1a489-5554-4545-ad12-79168775c5e3 for user 'robbie'.
2025-08-17 14:14:34,170 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:34,267 [INFO] Registered new session e6f6ab04-2a48-44d0-88d6-b4097dfa5b04 for user 'robbie'.
2025-08-17 14:14:34,271 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:34,369 [INFO] Registered new session 5251dd62-d5b9-4474-b8be-014f16ff1f6e for user 'robbie'.
2025-08-17 14:14:34,373 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:34,470 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:14:34,470 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:14:34,476 [INFO] Removed session 1d967f8e-b5bf-4d5b-914e-5d5509b2a0f1 for user 'robbie'.
2025-08-17 14:14:34,476 [INFO] User 'robbie' logged out and session '1d967f8e-b5bf-4d5b-914e-5d5509b2a0f1' was removed.
2025-08-17 14:14:34,573 [INFO] Registered new session 3a7e552a-d548-46cb-81c1-26008ac19a4c for user 'robbie'.
2025-08-17 14:14:34,576 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:14:34,584 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:14:34,585 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:14:34,586 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:14:34,589 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:14:34,738 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:14:34,743 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:14:34,744 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:14:34,745 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:14:34,756 [INFO] Assigned new SKU: RJC-0462. Tracker file updated.
2025-08-17 14:15:42,476 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:15:42,477 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:15:42,784 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:15:43,133 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:15:44,272 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:15:44,897 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:15:47,571 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:15:47,603 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:15:47,700 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:15:47,822 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:15:47,825 [INFO] Removed session 28da021d-7c7c-4ff1-8054-ae6f50bc9ac7 for user 'robbie'.
2025-08-17 14:15:47,825 [INFO] Removed session 601fed3e-18c8-4582-bca2-36910bd5a865 for user 'robbie'.
2025-08-17 14:15:47,920 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:15:47,927 [INFO] Registered new session 52ae6137-da52-446c-bfdd-68618b956227 for user 'viewer'.
2025-08-17 14:15:47,932 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:15:47,935 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:15:47,937 [INFO] Removed session 52ae6137-da52-446c-bfdd-68618b956227 for user 'viewer'.
2025-08-17 14:15:47,937 [INFO] User 'viewer' logged out and session '52ae6137-da52-446c-bfdd-68618b956227' was removed.
2025-08-17 14:15:48,031 [INFO] Registered new session df9d98b8-28d6-45eb-b1aa-008d25021cb5 for user 'robbie'.
2025-08-17 14:15:48,035 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:48,079 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:15:48,175 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:15:48,203 [INFO] Removed session df9d98b8-28d6-45eb-b1aa-008d25021cb5 for user 'robbie'.
2025-08-17 14:15:48,299 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:15:48,305 [INFO] Registered new session 62a345e3-6c1e-4c48-9736-7a4f5f8c951b for user 'robbie'.
2025-08-17 14:15:48,309 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:48,315 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:15:48,358 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:15:48,455 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:15:48,580 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:15:48,580 [INFO] Removed session 62a345e3-6c1e-4c48-9736-7a4f5f8c951b for user 'robbie'.
2025-08-17 14:15:48,675 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:15:48,682 [INFO] Registered new session 3508405a-d33e-4d90-b613-523c96e9ac69 for user 'robbie'.
2025-08-17 14:15:48,687 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:48,693 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:15:48,695 [INFO] Removed session 3508405a-d33e-4d90-b613-523c96e9ac69 for user 'robbie'.
2025-08-17 14:15:48,695 [INFO] User 'robbie' logged out and session '3508405a-d33e-4d90-b613-523c96e9ac69' was removed.
2025-08-17 14:15:48,790 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:15:48,805 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-49/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:15:48,807 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-49/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:15:48,808 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-49/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:15:48,907 [INFO] Registered new session 52a751d9-f931-4bf9-93c0-99ef3487562f for user 'robbie'.
2025-08-17 14:15:48,911 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:48,939 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:15:48,943 [INFO] Removed session 52a751d9-f931-4bf9-93c0-99ef3487562f for user 'robbie'.
2025-08-17 14:15:49,037 [INFO] Registered new session 48490a60-51d9-4e12-ad15-3a078e25f987 for user 'robbie'.
2025-08-17 14:15:49,042 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:49,049 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:15:49,052 [INFO] Removed session 48490a60-51d9-4e12-ad15-3a078e25f987 for user 'robbie'.
2025-08-17 14:15:49,147 [INFO] Registered new session 1c08449f-bab7-442a-9159-cf568d806434 for user 'robbie'.
2025-08-17 14:15:49,152 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:49,158 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:15:49,166 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-49/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:15:49,166 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-49/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:15:49,166 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-49/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:15:49,303 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-49/art_processing_test0
2025-08-17 14:15:49,303 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:15:49,304 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-49/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:15:49,304 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:15:49,305 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-49/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-49/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:15:49,305 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:15:49,305 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-49/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-49/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:15:49,306 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:15:49,306 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-49/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-49/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:15:49,306 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:15:49,306 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-49/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:15:49,306 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:15:49,306 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:15:49,307 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-49/art_processing_test0
2025-08-17 14:15:49,316 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-49/test_move_and_registry0/registry.json
2025-08-17 14:15:49,316 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:15:49,439 [INFO] Registered new session 5a153319-02f1-43d6-af05-6be4ff6998ae for user 'robbie'.
2025-08-17 14:15:49,444 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:50,130 [INFO] Sellbrite authentication succeeded
2025-08-17 14:15:51,624 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:15:51,625 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:15:51,625 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:15:51,626 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:15:51,626 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:15:51,626 [ERROR] Analysis script not found: no such file
2025-08-17 14:15:51,758 [INFO] Registered new session d8dab32c-dd88-47c2-958b-0fc3b2671d68 for user 'robbie'.
2025-08-17 14:15:51,763 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:51,875 [INFO] Registered new session c910183f-72ef-45e3-ac41-5c7452831968 for user 'robbie'.
2025-08-17 14:15:51,879 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:51,976 [INFO] Registered new session e0ccad23-a02b-40a0-8be7-db158f7f2baf for user 'robbie'.
2025-08-17 14:15:51,979 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:52,076 [INFO] Registered new session b206e34c-be8f-46bd-9881-d42e239f720c for user 'robbie'.
2025-08-17 14:15:52,080 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:52,178 [INFO] Registered new session 4fa63c1f-cf83-4953-a340-54956e26689e for user 'robbie'.
2025-08-17 14:15:52,182 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:52,282 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:15:52,282 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:15:52,287 [INFO] Removed session d8dab32c-dd88-47c2-958b-0fc3b2671d68 for user 'robbie'.
2025-08-17 14:15:52,288 [INFO] User 'robbie' logged out and session 'd8dab32c-dd88-47c2-958b-0fc3b2671d68' was removed.
2025-08-17 14:15:52,384 [INFO] Registered new session a380f262-4309-41d4-b16c-dcf9d1fcf0b1 for user 'robbie'.
2025-08-17 14:15:52,388 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:15:52,395 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:15:52,395 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:15:52,397 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:15:52,400 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:15:52,536 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:15:52,541 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:15:52,541 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:15:52,542 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:15:52,554 [INFO] Assigned new SKU: RJC-0463. Tracker file updated.
2025-08-17 14:25:45,355 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:25:45,356 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:25:45,681 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:25:45,969 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:25:47,127 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:25:47,756 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:25:50,391 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:25:50,421 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:25:50,517 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:25:50,640 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:25:50,643 [INFO] Removed session 1c08449f-bab7-442a-9159-cf568d806434 for user 'robbie'.
2025-08-17 14:25:50,644 [INFO] Removed session 5a153319-02f1-43d6-af05-6be4ff6998ae for user 'robbie'.
2025-08-17 14:25:50,739 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:25:50,746 [INFO] Registered new session c244dc3e-ca06-4217-a64c-5ec951506f89 for user 'viewer'.
2025-08-17 14:25:50,751 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:25:50,754 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:25:50,756 [INFO] Removed session c244dc3e-ca06-4217-a64c-5ec951506f89 for user 'viewer'.
2025-08-17 14:25:50,756 [INFO] User 'viewer' logged out and session 'c244dc3e-ca06-4217-a64c-5ec951506f89' was removed.
2025-08-17 14:25:50,849 [INFO] Registered new session 1878bd7e-2752-4976-a3de-f9cc2e99bc39 for user 'robbie'.
2025-08-17 14:25:50,854 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:50,899 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:25:50,995 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:25:51,024 [INFO] Removed session 1878bd7e-2752-4976-a3de-f9cc2e99bc39 for user 'robbie'.
2025-08-17 14:25:51,123 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:25:51,129 [INFO] Registered new session 3b938f17-c4b6-4e07-98c8-ef1881f1b948 for user 'robbie'.
2025-08-17 14:25:51,133 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:51,139 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:25:51,183 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:25:51,280 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:25:51,402 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:25:51,403 [INFO] Removed session 3b938f17-c4b6-4e07-98c8-ef1881f1b948 for user 'robbie'.
2025-08-17 14:25:51,497 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:25:51,504 [INFO] Registered new session ccc870f6-699c-4b62-ab39-a20da9a63d17 for user 'robbie'.
2025-08-17 14:25:51,509 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:51,515 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:25:51,516 [INFO] Removed session ccc870f6-699c-4b62-ab39-a20da9a63d17 for user 'robbie'.
2025-08-17 14:25:51,517 [INFO] User 'robbie' logged out and session 'ccc870f6-699c-4b62-ab39-a20da9a63d17' was removed.
2025-08-17 14:25:51,610 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:25:51,626 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-50/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:25:51,627 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-50/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:25:51,629 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-50/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:25:51,727 [INFO] Registered new session 2adee4d4-dc04-4275-9e4e-a55827429b32 for user 'robbie'.
2025-08-17 14:25:51,731 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:51,758 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:25:51,762 [INFO] Removed session 2adee4d4-dc04-4275-9e4e-a55827429b32 for user 'robbie'.
2025-08-17 14:25:51,857 [INFO] Registered new session 77af45cf-7a46-42bd-b2d8-0287e67a2d18 for user 'robbie'.
2025-08-17 14:25:51,862 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:51,869 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:25:51,873 [INFO] Removed session 77af45cf-7a46-42bd-b2d8-0287e67a2d18 for user 'robbie'.
2025-08-17 14:25:51,968 [INFO] Registered new session bfad9032-28ed-4e62-83ef-0581da501a23 for user 'robbie'.
2025-08-17 14:25:51,972 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:51,979 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:25:51,985 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-50/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:25:51,985 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-50/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:25:51,986 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-50/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:25:52,122 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-50/art_processing_test0
2025-08-17 14:25:52,123 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:25:52,123 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-50/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:25:52,123 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:25:52,124 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-50/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-50/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:25:52,124 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:25:52,124 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-50/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-50/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:25:52,124 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:25:52,125 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-50/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-50/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:25:52,125 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:25:52,125 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-50/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:25:52,125 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:25:52,125 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:25:52,126 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-50/art_processing_test0
2025-08-17 14:25:52,135 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-50/test_move_and_registry0/registry.json
2025-08-17 14:25:52,135 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:25:52,255 [INFO] Registered new session 5e968e79-ff11-4429-8914-24f4d053860b for user 'robbie'.
2025-08-17 14:25:52,260 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:52,968 [INFO] Sellbrite authentication succeeded
2025-08-17 14:25:54,481 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:25:54,481 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:25:54,481 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:25:54,482 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:25:54,482 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:25:54,483 [ERROR] Analysis script not found: no such file
2025-08-17 14:25:54,607 [INFO] Registered new session 5cb4585b-36cb-46c5-9f75-beb135fdddfc for user 'robbie'.
2025-08-17 14:25:54,611 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:54,721 [INFO] Registered new session 2dbdbc39-d87e-417f-92f6-5c90a65f842c for user 'robbie'.
2025-08-17 14:25:54,725 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:54,822 [INFO] Registered new session 52f33169-43c3-4710-9b0d-2cb8525eb684 for user 'robbie'.
2025-08-17 14:25:54,826 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:54,923 [INFO] Registered new session 7b64ae11-caee-4fc1-9fec-b8293bc1ffcb for user 'robbie'.
2025-08-17 14:25:54,927 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:55,035 [INFO] Registered new session 50b3e28b-7e09-4acc-801e-fc0731222722 for user 'robbie'.
2025-08-17 14:25:55,039 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:55,137 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:25:55,137 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:25:55,143 [INFO] Removed session 5cb4585b-36cb-46c5-9f75-beb135fdddfc for user 'robbie'.
2025-08-17 14:25:55,143 [INFO] User 'robbie' logged out and session '5cb4585b-36cb-46c5-9f75-beb135fdddfc' was removed.
2025-08-17 14:25:55,239 [INFO] Registered new session 39af17aa-e1a4-45fa-a018-1eeade65b702 for user 'robbie'.
2025-08-17 14:25:55,243 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:25:55,250 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:25:55,251 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:25:55,252 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:25:55,255 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:25:55,392 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:25:55,396 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:25:55,397 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:25:55,398 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:25:55,409 [INFO] Assigned new SKU: RJC-0464. Tracker file updated.
2025-08-17 14:29:37,115 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:29:37,116 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:29:37,349 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:29:37,655 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:29:38,805 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:29:39,434 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:29:42,084 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:29:42,114 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:29:42,210 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:29:42,332 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:29:42,334 [INFO] Removed session bfad9032-28ed-4e62-83ef-0581da501a23 for user 'robbie'.
2025-08-17 14:29:42,335 [INFO] Removed session 5e968e79-ff11-4429-8914-24f4d053860b for user 'robbie'.
2025-08-17 14:29:42,430 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:29:42,436 [INFO] Registered new session a0ec720a-13ce-4dd8-85cc-37c719467872 for user 'viewer'.
2025-08-17 14:29:42,441 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:29:42,444 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:29:42,446 [INFO] Removed session a0ec720a-13ce-4dd8-85cc-37c719467872 for user 'viewer'.
2025-08-17 14:29:42,446 [INFO] User 'viewer' logged out and session 'a0ec720a-13ce-4dd8-85cc-37c719467872' was removed.
2025-08-17 14:29:42,541 [INFO] Registered new session 03dc81a7-0318-4bdb-9c69-fd01657217c6 for user 'robbie'.
2025-08-17 14:29:42,545 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:42,588 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:29:42,683 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:29:42,709 [INFO] Removed session 03dc81a7-0318-4bdb-9c69-fd01657217c6 for user 'robbie'.
2025-08-17 14:29:42,806 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:29:42,813 [INFO] Registered new session 034af057-54c2-42df-9f8d-e83637c4b5f9 for user 'robbie'.
2025-08-17 14:29:42,817 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:42,824 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:29:42,867 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:29:42,962 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:29:43,084 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:29:43,084 [INFO] Removed session 034af057-54c2-42df-9f8d-e83637c4b5f9 for user 'robbie'.
2025-08-17 14:29:43,178 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:29:43,185 [INFO] Registered new session 633d5406-54a9-4878-b590-10276cb83b35 for user 'robbie'.
2025-08-17 14:29:43,190 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:43,196 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:29:43,197 [INFO] Removed session 633d5406-54a9-4878-b590-10276cb83b35 for user 'robbie'.
2025-08-17 14:29:43,198 [INFO] User 'robbie' logged out and session '633d5406-54a9-4878-b590-10276cb83b35' was removed.
2025-08-17 14:29:43,291 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:29:43,307 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-51/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:29:43,308 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-51/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:29:43,310 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-51/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:29:43,409 [INFO] Registered new session 4d5c4dd4-696b-4c58-8020-f7be63512954 for user 'robbie'.
2025-08-17 14:29:43,414 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:43,441 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:29:43,445 [INFO] Removed session 4d5c4dd4-696b-4c58-8020-f7be63512954 for user 'robbie'.
2025-08-17 14:29:43,540 [INFO] Registered new session da8243c4-6cff-4acc-bc0d-0ae95d0158eb for user 'robbie'.
2025-08-17 14:29:43,544 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:43,551 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:29:43,554 [INFO] Removed session da8243c4-6cff-4acc-bc0d-0ae95d0158eb for user 'robbie'.
2025-08-17 14:29:43,648 [INFO] Registered new session 034e8884-d751-4595-98cf-970e7c4ac1b7 for user 'robbie'.
2025-08-17 14:29:43,652 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:43,658 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:29:43,664 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-51/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:29:43,664 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-51/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:29:43,665 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-51/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:29:43,804 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-51/art_processing_test0
2025-08-17 14:29:43,804 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:29:43,805 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-51/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:29:43,805 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:29:43,805 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-51/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-51/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:29:43,805 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:29:43,806 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-51/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-51/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:29:43,806 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:29:43,806 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-51/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-51/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:29:43,806 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:29:43,806 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-51/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:29:43,807 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:29:43,807 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:29:43,807 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-51/art_processing_test0
2025-08-17 14:29:43,816 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-51/test_move_and_registry0/registry.json
2025-08-17 14:29:43,816 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:29:43,939 [INFO] Registered new session a2c41f78-1e58-4dc1-b0a2-a28cd199982a for user 'robbie'.
2025-08-17 14:29:43,944 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:44,617 [INFO] Sellbrite authentication succeeded
2025-08-17 14:29:46,130 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:29:46,130 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:29:46,130 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:29:46,132 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:29:46,132 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:29:46,132 [ERROR] Analysis script not found: no such file
2025-08-17 14:29:46,254 [INFO] Registered new session 7bd3b3a9-5ee5-48b6-a11e-e759e5ed3216 for user 'robbie'.
2025-08-17 14:29:46,259 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:46,368 [INFO] Registered new session 7773e104-81aa-4674-9200-5f96d618d802 for user 'robbie'.
2025-08-17 14:29:46,372 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:46,467 [INFO] Registered new session f2c7a846-ada6-46db-bb39-0bb57591bc18 for user 'robbie'.
2025-08-17 14:29:46,471 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:46,570 [INFO] Registered new session 89e57e46-7044-4e70-84b3-4f559d50df98 for user 'robbie'.
2025-08-17 14:29:46,574 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:46,671 [INFO] Registered new session 38c2b383-e2d8-4cd2-81c5-dc0c438bfe69 for user 'robbie'.
2025-08-17 14:29:46,674 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:46,772 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:29:46,772 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:29:46,777 [INFO] Removed session 7bd3b3a9-5ee5-48b6-a11e-e759e5ed3216 for user 'robbie'.
2025-08-17 14:29:46,778 [INFO] User 'robbie' logged out and session '7bd3b3a9-5ee5-48b6-a11e-e759e5ed3216' was removed.
2025-08-17 14:29:46,873 [INFO] Registered new session 7d02812b-81fa-402f-a147-f9566feb2a79 for user 'robbie'.
2025-08-17 14:29:46,877 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:29:46,884 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:29:46,884 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:29:46,886 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:29:46,889 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:29:47,026 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:29:47,031 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:29:47,031 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:29:47,032 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:29:47,043 [INFO] Assigned new SKU: RJC-0465. Tracker file updated.
2025-08-17 14:33:09,262 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:33:09,263 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:33:09,551 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:33:09,892 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:33:11,043 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:33:11,683 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:33:14,295 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:33:14,325 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:33:14,420 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:33:14,543 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:33:14,546 [INFO] Removed session 034e8884-d751-4595-98cf-970e7c4ac1b7 for user 'robbie'.
2025-08-17 14:33:14,546 [INFO] Removed session a2c41f78-1e58-4dc1-b0a2-a28cd199982a for user 'robbie'.
2025-08-17 14:33:14,640 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:33:14,647 [INFO] Registered new session 07752198-b9c2-4a96-b946-90b38c19a8ee for user 'viewer'.
2025-08-17 14:33:14,652 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:33:14,655 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:33:14,657 [INFO] Removed session 07752198-b9c2-4a96-b946-90b38c19a8ee for user 'viewer'.
2025-08-17 14:33:14,658 [INFO] User 'viewer' logged out and session '07752198-b9c2-4a96-b946-90b38c19a8ee' was removed.
2025-08-17 14:33:14,752 [INFO] Registered new session b4b411cd-038a-4277-a8bf-646cb62be408 for user 'robbie'.
2025-08-17 14:33:14,757 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:14,800 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:33:14,898 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:33:14,925 [INFO] Removed session b4b411cd-038a-4277-a8bf-646cb62be408 for user 'robbie'.
2025-08-17 14:33:15,021 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:33:15,027 [INFO] Registered new session 7ba9d970-fb6a-44b5-a056-84364e135bdd for user 'robbie'.
2025-08-17 14:33:15,031 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:15,037 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:33:15,081 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:33:15,177 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:33:15,297 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:33:15,298 [INFO] Removed session 7ba9d970-fb6a-44b5-a056-84364e135bdd for user 'robbie'.
2025-08-17 14:33:15,391 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:33:15,399 [INFO] Registered new session c9402bb6-cf76-4db2-b19b-6f679bf10664 for user 'robbie'.
2025-08-17 14:33:15,403 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:15,409 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:33:15,410 [INFO] Removed session c9402bb6-cf76-4db2-b19b-6f679bf10664 for user 'robbie'.
2025-08-17 14:33:15,411 [INFO] User 'robbie' logged out and session 'c9402bb6-cf76-4db2-b19b-6f679bf10664' was removed.
2025-08-17 14:33:15,503 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:33:15,519 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-52/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:33:15,521 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-52/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:33:15,522 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-52/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:33:15,619 [INFO] Registered new session 3b7cfdb4-2bed-4e0a-97b2-cf5a4e3d47dd for user 'robbie'.
2025-08-17 14:33:15,623 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:15,651 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:33:15,655 [INFO] Removed session 3b7cfdb4-2bed-4e0a-97b2-cf5a4e3d47dd for user 'robbie'.
2025-08-17 14:33:15,747 [INFO] Registered new session 44a90a12-a437-4312-a183-f63238356bbe for user 'robbie'.
2025-08-17 14:33:15,752 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:15,758 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:33:15,762 [INFO] Removed session 44a90a12-a437-4312-a183-f63238356bbe for user 'robbie'.
2025-08-17 14:33:15,856 [INFO] Registered new session ef1ec7d6-5b2b-4591-af78-be23ddca471b for user 'robbie'.
2025-08-17 14:33:15,861 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:15,867 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:33:15,873 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-52/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:33:15,874 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-52/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:33:15,874 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-52/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:33:16,049 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-52/art_processing_test0
2025-08-17 14:33:16,049 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:33:16,050 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-52/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:33:16,050 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:33:16,050 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-52/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-52/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:33:16,051 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:33:16,051 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-52/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-52/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:33:16,051 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:33:16,051 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-52/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-52/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:33:16,052 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:33:16,052 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-52/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:33:16,052 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:33:16,052 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:33:16,052 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-52/art_processing_test0
2025-08-17 14:33:16,062 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-52/test_move_and_registry0/registry.json
2025-08-17 14:33:16,063 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:33:16,162 [INFO] Registered new session 29b1c29c-bae6-4afb-9f90-b32297214d56 for user 'robbie'.
2025-08-17 14:33:16,166 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:16,833 [INFO] Sellbrite authentication succeeded
2025-08-17 14:33:18,360 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:33:18,360 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:33:18,360 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:33:18,362 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:33:18,362 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:33:18,362 [ERROR] Analysis script not found: no such file
2025-08-17 14:33:18,487 [INFO] Registered new session efd6101f-66ad-4ba1-81f1-a092b02034de for user 'robbie'.
2025-08-17 14:33:18,491 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:18,601 [INFO] Registered new session b90f7611-6a2b-4ee8-8674-4d4274ad55ca for user 'robbie'.
2025-08-17 14:33:18,605 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:18,703 [INFO] Registered new session 4be550ac-4278-4ca2-bdba-b8c4c619195e for user 'robbie'.
2025-08-17 14:33:18,707 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:18,803 [INFO] Registered new session 3dea23a5-4099-469b-bb52-e8e50e272a27 for user 'robbie'.
2025-08-17 14:33:18,807 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:18,918 [INFO] Registered new session 6c77875f-0820-41d7-bc3c-ea9b10910678 for user 'robbie'.
2025-08-17 14:33:18,922 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:19,021 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:33:19,021 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:33:19,027 [INFO] Removed session efd6101f-66ad-4ba1-81f1-a092b02034de for user 'robbie'.
2025-08-17 14:33:19,027 [INFO] User 'robbie' logged out and session 'efd6101f-66ad-4ba1-81f1-a092b02034de' was removed.
2025-08-17 14:33:19,123 [INFO] Registered new session 3d3948b1-f5c3-4148-91d6-ae1fbcd4d072 for user 'robbie'.
2025-08-17 14:33:19,127 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:33:19,134 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:33:19,135 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:33:19,136 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:33:19,139 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:33:19,282 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:33:19,287 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:33:19,287 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:33:19,288 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:33:19,299 [INFO] Assigned new SKU: RJC-0466. Tracker file updated.
2025-08-17 14:36:05,511 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:36:05,512 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:36:05,863 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:36:06,739 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:36:07,879 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:36:08,604 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:36:11,295 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:36:11,324 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:36:11,418 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:36:11,539 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:36:11,542 [INFO] Removed session ef1ec7d6-5b2b-4591-af78-be23ddca471b for user 'robbie'.
2025-08-17 14:36:11,542 [INFO] Removed session 29b1c29c-bae6-4afb-9f90-b32297214d56 for user 'robbie'.
2025-08-17 14:36:11,635 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:36:11,642 [INFO] Registered new session e7a20109-5b31-478f-9688-2c5437b87cc9 for user 'viewer'.
2025-08-17 14:36:11,646 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:36:11,649 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:36:11,651 [INFO] Removed session e7a20109-5b31-478f-9688-2c5437b87cc9 for user 'viewer'.
2025-08-17 14:36:11,652 [INFO] User 'viewer' logged out and session 'e7a20109-5b31-478f-9688-2c5437b87cc9' was removed.
2025-08-17 14:36:11,744 [INFO] Registered new session 464eee12-c0b1-4a86-87c0-469f8607ccb9 for user 'robbie'.
2025-08-17 14:36:11,749 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:11,792 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:36:11,887 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:36:11,914 [INFO] Removed session 464eee12-c0b1-4a86-87c0-469f8607ccb9 for user 'robbie'.
2025-08-17 14:36:12,008 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:36:12,014 [INFO] Registered new session d0f25ec7-b011-4b56-a7dc-4108be19eef7 for user 'robbie'.
2025-08-17 14:36:12,018 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:12,023 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:36:12,065 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:36:12,161 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:36:12,281 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:36:12,282 [INFO] Removed session d0f25ec7-b011-4b56-a7dc-4108be19eef7 for user 'robbie'.
2025-08-17 14:36:12,374 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:36:12,381 [INFO] Registered new session a6a5c84c-1c4a-4d4a-8712-d7ce1ca509e2 for user 'robbie'.
2025-08-17 14:36:12,385 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:12,391 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:36:12,393 [INFO] Removed session a6a5c84c-1c4a-4d4a-8712-d7ce1ca509e2 for user 'robbie'.
2025-08-17 14:36:12,393 [INFO] User 'robbie' logged out and session 'a6a5c84c-1c4a-4d4a-8712-d7ce1ca509e2' was removed.
2025-08-17 14:36:12,485 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:36:12,500 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-53/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:36:12,502 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-53/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:36:12,504 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-53/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:36:12,601 [INFO] Registered new session 165c19ab-e1a3-40e9-9057-495dbb53777a for user 'robbie'.
2025-08-17 14:36:12,605 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:12,633 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:36:12,637 [INFO] Removed session 165c19ab-e1a3-40e9-9057-495dbb53777a for user 'robbie'.
2025-08-17 14:36:12,731 [INFO] Registered new session 26ae9893-2c97-4de6-a8ea-e6bbf06a4720 for user 'robbie'.
2025-08-17 14:36:12,735 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:12,742 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:36:12,745 [INFO] Removed session 26ae9893-2c97-4de6-a8ea-e6bbf06a4720 for user 'robbie'.
2025-08-17 14:36:12,839 [INFO] Registered new session e09d6121-dce1-47c4-9b22-29e15f4b2975 for user 'robbie'.
2025-08-17 14:36:12,843 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:12,849 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:36:12,855 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-53/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:36:12,855 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-53/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:36:12,856 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-53/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:36:12,993 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-53/art_processing_test0
2025-08-17 14:36:12,993 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:36:12,994 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-53/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:36:12,994 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:36:12,994 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-53/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-53/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:36:12,994 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:36:12,995 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-53/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-53/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:36:12,995 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:36:12,995 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-53/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-53/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:36:12,995 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:36:12,996 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-53/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:36:12,996 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:36:12,996 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:36:12,996 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-53/art_processing_test0
2025-08-17 14:36:13,005 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-53/test_move_and_registry0/registry.json
2025-08-17 14:36:13,006 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:36:13,104 [INFO] Registered new session 20123230-395d-41e2-b29a-814e2373c581 for user 'robbie'.
2025-08-17 14:36:13,108 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:13,823 [INFO] Sellbrite authentication succeeded
2025-08-17 14:36:15,332 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:36:15,332 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:36:15,333 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:36:15,334 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:36:15,334 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:36:15,334 [ERROR] Analysis script not found: no such file
2025-08-17 14:36:15,456 [INFO] Registered new session 10d60bd7-1f90-47aa-85bf-c9b90fc84201 for user 'robbie'.
2025-08-17 14:36:15,460 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:15,567 [INFO] Registered new session d83eb16a-b6e3-4a4f-b7b0-247d9d99c69f for user 'robbie'.
2025-08-17 14:36:15,571 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:15,666 [INFO] Registered new session 91e9b179-b5fb-4c2a-be1a-31d995b6b43c for user 'robbie'.
2025-08-17 14:36:15,670 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:15,765 [INFO] Registered new session e67b8042-748d-495d-af6b-3da37122d868 for user 'robbie'.
2025-08-17 14:36:15,769 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:15,867 [INFO] Registered new session 8dd8ffcf-94c9-4913-91b1-b9d2d20ed9f3 for user 'robbie'.
2025-08-17 14:36:15,871 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:15,995 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:36:15,995 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:36:16,002 [INFO] Removed session 10d60bd7-1f90-47aa-85bf-c9b90fc84201 for user 'robbie'.
2025-08-17 14:36:16,003 [INFO] User 'robbie' logged out and session '10d60bd7-1f90-47aa-85bf-c9b90fc84201' was removed.
2025-08-17 14:36:16,100 [INFO] Registered new session 5920e604-381c-464b-a782-c6dbf71b0ff4 for user 'robbie'.
2025-08-17 14:36:16,104 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:36:16,111 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:36:16,112 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:36:16,113 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:36:16,116 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:36:16,253 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:36:16,258 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:36:16,258 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:36:16,259 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:36:16,269 [INFO] Assigned new SKU: RJC-0467. Tracker file updated.
2025-08-17 14:37:37,442 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:37:37,443 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:37:37,758 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:37:38,149 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:37:39,304 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:37:40,026 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:37:42,670 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:37:42,700 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:37:42,797 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:37:42,920 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:37:42,923 [INFO] Removed session e09d6121-dce1-47c4-9b22-29e15f4b2975 for user 'robbie'.
2025-08-17 14:37:42,924 [INFO] Removed session 20123230-395d-41e2-b29a-814e2373c581 for user 'robbie'.
2025-08-17 14:37:43,019 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:37:43,025 [INFO] Registered new session 13eb6026-0537-48f6-b2a3-d867ab210beb for user 'viewer'.
2025-08-17 14:37:43,030 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:37:43,033 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:37:43,035 [INFO] Removed session 13eb6026-0537-48f6-b2a3-d867ab210beb for user 'viewer'.
2025-08-17 14:37:43,035 [INFO] User 'viewer' logged out and session '13eb6026-0537-48f6-b2a3-d867ab210beb' was removed.
2025-08-17 14:37:43,128 [INFO] Registered new session e020fa86-f9f2-49da-9c22-939e966d0f20 for user 'robbie'.
2025-08-17 14:37:43,132 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:43,178 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:37:43,274 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:37:43,299 [INFO] Removed session e020fa86-f9f2-49da-9c22-939e966d0f20 for user 'robbie'.
2025-08-17 14:37:43,395 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:37:43,401 [INFO] Registered new session a4dba59a-89fc-4ee8-b3d7-6309bcc8963a for user 'robbie'.
2025-08-17 14:37:43,405 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:43,411 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:37:43,455 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:37:43,551 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:37:43,672 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:37:43,673 [INFO] Removed session a4dba59a-89fc-4ee8-b3d7-6309bcc8963a for user 'robbie'.
2025-08-17 14:37:43,767 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:37:43,775 [INFO] Registered new session 8d1cdf26-2058-43e0-9333-14428417c604 for user 'robbie'.
2025-08-17 14:37:43,779 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:43,785 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:37:43,787 [INFO] Removed session 8d1cdf26-2058-43e0-9333-14428417c604 for user 'robbie'.
2025-08-17 14:37:43,787 [INFO] User 'robbie' logged out and session '8d1cdf26-2058-43e0-9333-14428417c604' was removed.
2025-08-17 14:37:43,881 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:37:43,896 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-54/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:37:43,898 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-54/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:37:43,900 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-54/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:37:44,000 [INFO] Registered new session d5dfcc71-e86a-4dbc-b9ef-8cccc11fe49a for user 'robbie'.
2025-08-17 14:37:44,004 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:44,033 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:37:44,037 [INFO] Removed session d5dfcc71-e86a-4dbc-b9ef-8cccc11fe49a for user 'robbie'.
2025-08-17 14:37:44,132 [INFO] Registered new session 7726303d-4cd7-4214-88d1-bc28e5f0a6b2 for user 'robbie'.
2025-08-17 14:37:44,136 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:44,143 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:37:44,147 [INFO] Removed session 7726303d-4cd7-4214-88d1-bc28e5f0a6b2 for user 'robbie'.
2025-08-17 14:37:44,241 [INFO] Registered new session 402a07cd-4eba-425e-b54a-987e4931a9b3 for user 'robbie'.
2025-08-17 14:37:44,245 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:44,251 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:37:44,347 [INFO] Registered new session ab5e857d-0968-464c-b9b6-ff64c89b1603 for user 'robbie'.
2025-08-17 14:37:44,352 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:44,361 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-54/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:37:44,361 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-54/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:37:44,362 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-54/art_processing0/processed-artwork/cassowary-test-01
2025-08-17 14:37:44,545 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-54/art_processing_test0
2025-08-17 14:37:44,545 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:37:44,546 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-54/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:37:44,546 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:37:44,546 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-54/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-54/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:37:44,547 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:37:44,547 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-54/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-54/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:37:44,547 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:37:44,547 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-54/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-54/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:37:44,547 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:37:44,548 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-54/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:37:44,548 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:37:44,548 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:37:44,548 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-54/art_processing_test0
2025-08-17 14:37:44,557 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-54/test_move_and_registry0/registry.json
2025-08-17 14:37:44,557 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:37:44,656 [INFO] Registered new session 94b79eec-0eb4-470b-9615-b94fb3b1eded for user 'robbie'.
2025-08-17 14:37:44,661 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:45,326 [INFO] Sellbrite authentication succeeded
2025-08-17 14:37:46,844 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:37:46,844 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:37:46,845 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:37:46,846 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:37:46,846 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:37:46,846 [ERROR] Analysis script not found: no such file
2025-08-17 14:37:46,970 [INFO] Registered new session 80157d25-0092-4c48-a5a9-32fe78921ae6 for user 'robbie'.
2025-08-17 14:37:46,974 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:47,087 [INFO] Registered new session 6f55ebdc-a4d6-4696-a7b6-f27bf4108d98 for user 'robbie'.
2025-08-17 14:37:47,091 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:47,188 [INFO] Registered new session 76d9eec1-1dd7-41a4-9ebd-4384497c7e6d for user 'robbie'.
2025-08-17 14:37:47,192 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:47,289 [INFO] Registered new session 34847857-aa4a-4679-bf96-c57010011630 for user 'robbie'.
2025-08-17 14:37:47,293 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:47,393 [INFO] Registered new session e652118f-2604-48ab-84c1-44b38841903f for user 'robbie'.
2025-08-17 14:37:47,397 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:47,494 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:37:47,494 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:37:47,500 [INFO] Removed session 80157d25-0092-4c48-a5a9-32fe78921ae6 for user 'robbie'.
2025-08-17 14:37:47,500 [INFO] User 'robbie' logged out and session '80157d25-0092-4c48-a5a9-32fe78921ae6' was removed.
2025-08-17 14:37:47,596 [INFO] Registered new session b5aa3ff0-b619-45cc-8682-70bb702fe2b3 for user 'robbie'.
2025-08-17 14:37:47,600 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:37:47,608 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:37:47,608 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:37:47,610 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:37:47,613 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:37:47,753 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:37:47,758 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:37:47,759 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:37:47,760 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:37:47,857 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:37:47,857 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:37:47,864 [INFO] Assigned new SKU: RJC-0468. Tracker file updated.
2025-08-17 14:39:03,596 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:39:03,598 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:39:03,906 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:39:04,234 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:39:05,382 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:39:06,010 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:39:08,644 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:39:08,674 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:39:08,769 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:39:08,891 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:39:08,894 [INFO] Removed session 402a07cd-4eba-425e-b54a-987e4931a9b3 for user 'robbie'.
2025-08-17 14:39:08,894 [INFO] Removed session ab5e857d-0968-464c-b9b6-ff64c89b1603 for user 'robbie'.
2025-08-17 14:39:08,895 [INFO] Removed session 94b79eec-0eb4-470b-9615-b94fb3b1eded for user 'robbie'.
2025-08-17 14:39:08,988 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:39:08,994 [INFO] Registered new session f51845c7-4f33-45cf-a2de-250f062efa5a for user 'viewer'.
2025-08-17 14:39:08,999 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:39:09,002 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:39:09,003 [INFO] Removed session f51845c7-4f33-45cf-a2de-250f062efa5a for user 'viewer'.
2025-08-17 14:39:09,004 [INFO] User 'viewer' logged out and session 'f51845c7-4f33-45cf-a2de-250f062efa5a' was removed.
2025-08-17 14:39:09,096 [INFO] Registered new session f0b16eec-4bf9-4639-9196-9f7aa0361df0 for user 'robbie'.
2025-08-17 14:39:09,100 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:09,142 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:39:09,237 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:39:09,264 [INFO] Removed session f0b16eec-4bf9-4639-9196-9f7aa0361df0 for user 'robbie'.
2025-08-17 14:39:09,358 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:39:09,364 [INFO] Registered new session fd508b1c-3744-46b5-b457-4f9c24faaae3 for user 'robbie'.
2025-08-17 14:39:09,369 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:09,375 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:39:09,416 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:39:09,511 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:39:09,631 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:39:09,632 [INFO] Removed session fd508b1c-3744-46b5-b457-4f9c24faaae3 for user 'robbie'.
2025-08-17 14:39:09,726 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:39:09,733 [INFO] Registered new session 8e44018f-3447-4f0f-aa05-a9332f48728b for user 'robbie'.
2025-08-17 14:39:09,737 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:09,743 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:39:09,745 [INFO] Removed session 8e44018f-3447-4f0f-aa05-a9332f48728b for user 'robbie'.
2025-08-17 14:39:09,745 [INFO] User 'robbie' logged out and session '8e44018f-3447-4f0f-aa05-a9332f48728b' was removed.
2025-08-17 14:39:09,840 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:39:09,856 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-55/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:39:09,857 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-55/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:39:09,859 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-55/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:39:09,958 [INFO] Registered new session 1ecb007d-ddf6-487e-bb1f-0177cfaa8fd5 for user 'robbie'.
2025-08-17 14:39:09,962 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:09,990 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:39:09,994 [INFO] Removed session 1ecb007d-ddf6-487e-bb1f-0177cfaa8fd5 for user 'robbie'.
2025-08-17 14:39:10,088 [INFO] Registered new session 8e16aacc-1ece-45b4-9ba0-1d8f1cbd8486 for user 'robbie'.
2025-08-17 14:39:10,092 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:10,099 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:39:10,103 [INFO] Removed session 8e16aacc-1ece-45b4-9ba0-1d8f1cbd8486 for user 'robbie'.
2025-08-17 14:39:10,198 [INFO] Registered new session cb2018a8-4452-4478-b44a-299b00c3f947 for user 'robbie'.
2025-08-17 14:39:10,202 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:10,208 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:39:10,306 [INFO] Registered new session 5e39f97e-93a0-4a40-bb97-502c46e53625 for user 'robbie'.
2025-08-17 14:39:10,310 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:10,315 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-55/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:39:10,315 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-55/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:39:10,316 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-55/art_processing0/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 14:39:10,710 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-55/art_processing_test0
2025-08-17 14:39:10,711 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:39:10,711 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-55/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:39:10,711 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:39:10,712 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-55/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-55/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:39:10,712 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:39:10,713 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-55/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-55/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:39:10,713 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:39:10,713 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-55/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-55/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:39:10,713 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:39:10,713 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-55/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:39:10,713 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:39:10,713 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:39:10,714 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-55/art_processing_test0
2025-08-17 14:39:10,723 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-55/test_move_and_registry0/registry.json
2025-08-17 14:39:10,723 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:39:10,824 [INFO] Registered new session 92dea1ac-b5f3-4a43-bf50-c6e7518df976 for user 'robbie'.
2025-08-17 14:39:10,828 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:11,535 [INFO] Sellbrite authentication succeeded
2025-08-17 14:39:13,058 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:39:13,058 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:39:13,058 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:39:13,059 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:39:13,060 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:39:13,060 [ERROR] Analysis script not found: no such file
2025-08-17 14:39:13,195 [INFO] Registered new session 65182fef-603e-47c0-9d26-a73e243ad38c for user 'robbie'.
2025-08-17 14:39:13,199 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:13,308 [INFO] Registered new session b845d0c0-7f04-4da1-99a8-bf0634f42a2c for user 'robbie'.
2025-08-17 14:39:13,311 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:13,407 [INFO] Registered new session 28f99a75-4b61-43a1-9e3b-21210532889c for user 'robbie'.
2025-08-17 14:39:13,411 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:13,507 [INFO] Registered new session 0377190c-40e6-4200-acd5-e079a7959318 for user 'robbie'.
2025-08-17 14:39:13,511 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:13,609 [INFO] Registered new session 66c2ca60-c3b3-453c-a40e-55d6c31cbdf4 for user 'robbie'.
2025-08-17 14:39:13,613 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:13,749 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:39:13,750 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:39:13,758 [INFO] Removed session 65182fef-603e-47c0-9d26-a73e243ad38c for user 'robbie'.
2025-08-17 14:39:13,758 [INFO] User 'robbie' logged out and session '65182fef-603e-47c0-9d26-a73e243ad38c' was removed.
2025-08-17 14:39:13,939 [INFO] Registered new session 9c2542d2-657f-4b0d-9463-293547c927ef for user 'robbie'.
2025-08-17 14:39:13,944 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:13,955 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:39:13,956 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:39:13,958 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:39:13,962 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:39:13,974 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:39:13,981 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:39:13,982 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:39:13,983 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:39:14,170 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:39:14,171 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:39:14,193 [INFO] Assigned new SKU: RJC-0469. Tracker file updated.
2025-08-17 14:39:40,237 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:39:40,238 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:39:40,496 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:39:40,885 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:39:42,024 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:39:42,651 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:39:45,377 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:39:45,408 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:39:45,503 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:39:45,626 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:39:45,629 [INFO] Removed session cb2018a8-4452-4478-b44a-299b00c3f947 for user 'robbie'.
2025-08-17 14:39:45,629 [INFO] Removed session 5e39f97e-93a0-4a40-bb97-502c46e53625 for user 'robbie'.
2025-08-17 14:39:45,630 [INFO] Removed session 92dea1ac-b5f3-4a43-bf50-c6e7518df976 for user 'robbie'.
2025-08-17 14:39:45,724 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:39:45,731 [INFO] Registered new session d998edbb-53be-4a58-9368-fef76d2a3f6c for user 'viewer'.
2025-08-17 14:39:45,736 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:39:45,739 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:39:45,741 [INFO] Removed session d998edbb-53be-4a58-9368-fef76d2a3f6c for user 'viewer'.
2025-08-17 14:39:45,741 [INFO] User 'viewer' logged out and session 'd998edbb-53be-4a58-9368-fef76d2a3f6c' was removed.
2025-08-17 14:39:45,834 [INFO] Registered new session a5608357-e87c-4bf9-8251-9f91d5c6ddd0 for user 'robbie'.
2025-08-17 14:39:45,838 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:45,882 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:39:45,977 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:39:46,004 [INFO] Removed session a5608357-e87c-4bf9-8251-9f91d5c6ddd0 for user 'robbie'.
2025-08-17 14:39:46,099 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:39:46,105 [INFO] Registered new session 3bfc8cad-1fe2-4779-99a0-5848bba8e2b3 for user 'robbie'.
2025-08-17 14:39:46,110 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:46,116 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:39:46,159 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:39:46,257 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:39:46,378 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:39:46,379 [INFO] Removed session 3bfc8cad-1fe2-4779-99a0-5848bba8e2b3 for user 'robbie'.
2025-08-17 14:39:46,473 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:39:46,481 [INFO] Registered new session addf97d1-02be-4837-a67a-082a90ded3e6 for user 'robbie'.
2025-08-17 14:39:46,485 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:46,491 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:39:46,493 [INFO] Removed session addf97d1-02be-4837-a67a-082a90ded3e6 for user 'robbie'.
2025-08-17 14:39:46,493 [INFO] User 'robbie' logged out and session 'addf97d1-02be-4837-a67a-082a90ded3e6' was removed.
2025-08-17 14:39:46,586 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:39:46,602 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-56/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:39:46,604 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-56/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:39:46,605 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-56/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:39:46,705 [INFO] Registered new session 8d379def-455d-4cc0-b03d-c774e23a9208 for user 'robbie'.
2025-08-17 14:39:46,709 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:46,739 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:39:46,743 [INFO] Removed session 8d379def-455d-4cc0-b03d-c774e23a9208 for user 'robbie'.
2025-08-17 14:39:46,838 [INFO] Registered new session ed4613f8-3b4b-4b20-bf78-59184642ba48 for user 'robbie'.
2025-08-17 14:39:46,843 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:46,850 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:39:46,854 [INFO] Removed session ed4613f8-3b4b-4b20-bf78-59184642ba48 for user 'robbie'.
2025-08-17 14:39:46,950 [INFO] Registered new session 20f8043d-829a-4466-a565-41f021939de3 for user 'robbie'.
2025-08-17 14:39:46,954 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:46,960 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:39:47,060 [INFO] Registered new session 95b2b7ee-63ca-4dca-99ec-eb9c0a18006f for user 'robbie'.
2025-08-17 14:39:47,064 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:47,070 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-56/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:39:47,070 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-56/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:39:47,071 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-56/art_processing0/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 14:39:47,495 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-56/art_processing_test0
2025-08-17 14:39:47,495 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:39:47,496 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-56/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:39:47,496 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:39:47,496 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-56/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-56/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:39:47,497 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:39:47,497 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-56/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-56/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:39:47,497 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:39:47,497 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-56/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-56/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:39:47,498 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:39:47,498 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-56/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:39:47,498 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:39:47,498 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:39:47,498 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-56/art_processing_test0
2025-08-17 14:39:47,507 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-56/test_move_and_registry0/registry.json
2025-08-17 14:39:47,508 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:39:47,610 [INFO] Registered new session 27994231-d56c-4001-836b-fe66883a7145 for user 'robbie'.
2025-08-17 14:39:47,614 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:48,294 [INFO] Sellbrite authentication succeeded
2025-08-17 14:39:49,840 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:39:49,840 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:39:49,840 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:39:49,841 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:39:49,842 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:39:49,842 [ERROR] Analysis script not found: no such file
2025-08-17 14:39:49,966 [INFO] Registered new session cd35c095-63bb-41b7-8124-2f5836917938 for user 'robbie'.
2025-08-17 14:39:49,971 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:50,080 [INFO] Registered new session 00e6b820-1350-4e40-8baa-afb329b78a4e for user 'robbie'.
2025-08-17 14:39:50,084 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:50,181 [INFO] Registered new session 0c3511a5-3d79-4be7-a619-f8d076421aa1 for user 'robbie'.
2025-08-17 14:39:50,185 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:50,282 [INFO] Registered new session eecc8c92-a635-4438-aa01-47ad7058883b for user 'robbie'.
2025-08-17 14:39:50,286 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:50,383 [INFO] Registered new session 1513e090-8ba9-4110-b0dc-1b1f05f66529 for user 'robbie'.
2025-08-17 14:39:50,387 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:50,483 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:39:50,483 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:39:50,489 [INFO] Removed session cd35c095-63bb-41b7-8124-2f5836917938 for user 'robbie'.
2025-08-17 14:39:50,489 [INFO] User 'robbie' logged out and session 'cd35c095-63bb-41b7-8124-2f5836917938' was removed.
2025-08-17 14:39:50,585 [INFO] Registered new session cfab1cc5-7d9e-47f0-95bb-3faa409b07f3 for user 'robbie'.
2025-08-17 14:39:50,589 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:39:50,597 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:39:50,597 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:39:50,599 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:39:50,602 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:39:50,609 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:39:50,613 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:39:50,614 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:39:50,615 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:39:50,720 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:39:50,720 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:39:50,727 [INFO] Assigned new SKU: RJC-0470. Tracker file updated.
2025-08-17 14:41:08,664 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:41:08,666 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:41:08,934 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:41:09,271 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:41:10,436 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:41:11,081 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:41:13,755 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:41:13,786 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:41:13,880 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:41:14,000 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:41:14,002 [INFO] Removed session 20f8043d-829a-4466-a565-41f021939de3 for user 'robbie'.
2025-08-17 14:41:14,003 [INFO] Removed session 95b2b7ee-63ca-4dca-99ec-eb9c0a18006f for user 'robbie'.
2025-08-17 14:41:14,003 [INFO] Removed session 27994231-d56c-4001-836b-fe66883a7145 for user 'robbie'.
2025-08-17 14:41:14,097 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:41:14,103 [INFO] Registered new session a48b2f50-3c13-490d-aa0b-147e813bb99d for user 'viewer'.
2025-08-17 14:41:14,107 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:41:14,110 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:41:14,112 [INFO] Removed session a48b2f50-3c13-490d-aa0b-147e813bb99d for user 'viewer'.
2025-08-17 14:41:14,113 [INFO] User 'viewer' logged out and session 'a48b2f50-3c13-490d-aa0b-147e813bb99d' was removed.
2025-08-17 14:41:14,205 [INFO] Registered new session d7153393-496d-4f43-b651-3a31bcea27fe for user 'robbie'.
2025-08-17 14:41:14,209 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:14,252 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:41:14,347 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:41:14,372 [INFO] Removed session d7153393-496d-4f43-b651-3a31bcea27fe for user 'robbie'.
2025-08-17 14:41:14,468 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:41:14,474 [INFO] Registered new session cce80bad-635a-4db3-a958-0222a0855ace for user 'robbie'.
2025-08-17 14:41:14,479 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:14,485 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:41:14,531 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:41:14,626 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:41:14,747 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:41:14,747 [INFO] Removed session cce80bad-635a-4db3-a958-0222a0855ace for user 'robbie'.
2025-08-17 14:41:14,841 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:41:14,849 [INFO] Registered new session fe787068-25e8-41e3-959a-6b95b3d2dda9 for user 'robbie'.
2025-08-17 14:41:14,853 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:14,859 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:41:14,861 [INFO] Removed session fe787068-25e8-41e3-959a-6b95b3d2dda9 for user 'robbie'.
2025-08-17 14:41:14,861 [INFO] User 'robbie' logged out and session 'fe787068-25e8-41e3-959a-6b95b3d2dda9' was removed.
2025-08-17 14:41:14,955 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:41:14,970 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-57/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:41:14,972 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-57/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:41:14,973 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-57/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:41:15,071 [INFO] Registered new session 957bf2f7-149e-4a12-8e1b-57b5c5a5f34f for user 'robbie'.
2025-08-17 14:41:15,075 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:15,102 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:41:15,106 [INFO] Removed session 957bf2f7-149e-4a12-8e1b-57b5c5a5f34f for user 'robbie'.
2025-08-17 14:41:15,201 [INFO] Registered new session 7345d39e-e6b9-4188-90aa-e8570e6927f1 for user 'robbie'.
2025-08-17 14:41:15,205 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:15,212 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:41:15,215 [INFO] Removed session 7345d39e-e6b9-4188-90aa-e8570e6927f1 for user 'robbie'.
2025-08-17 14:41:15,308 [INFO] Registered new session 361f662b-c956-4583-8625-538483c6adc3 for user 'robbie'.
2025-08-17 14:41:15,312 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:15,320 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:41:15,417 [INFO] Registered new session fde21f7f-a67d-449f-af2b-c90920784245 for user 'robbie'.
2025-08-17 14:41:15,422 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:15,428 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-57/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:41:15,428 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-57/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:41:15,428 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-57/art_processing0/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 14:41:15,431 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 14:41:15,464 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-57/art_processing_test0
2025-08-17 14:41:15,465 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:41:15,465 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-57/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:41:15,465 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:41:15,466 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-57/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-57/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:41:15,466 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:41:15,466 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-57/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-57/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:41:15,466 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:41:15,467 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-57/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-57/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:41:15,467 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:41:15,467 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-57/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:41:15,467 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:41:15,467 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:41:15,468 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-57/art_processing_test0
2025-08-17 14:41:15,478 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-57/test_move_and_registry0/registry.json
2025-08-17 14:41:15,478 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:41:15,577 [INFO] Registered new session 8172f4d4-9d79-475b-a455-9e29f5a5c4da for user 'robbie'.
2025-08-17 14:41:15,582 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:16,270 [INFO] Sellbrite authentication succeeded
2025-08-17 14:41:17,751 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:41:17,751 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:41:17,751 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:41:17,753 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:41:17,753 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:41:17,753 [ERROR] Analysis script not found: no such file
2025-08-17 14:41:17,889 [INFO] Registered new session 2271be7a-46ce-4e4c-b151-dd84577a27a3 for user 'robbie'.
2025-08-17 14:41:17,893 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:18,002 [INFO] Registered new session 6e5010fc-e6b2-4134-aca8-68dc323bce70 for user 'robbie'.
2025-08-17 14:41:18,006 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:18,102 [INFO] Registered new session 53827ea0-a303-431c-bb6a-cfce4f64f5ef for user 'robbie'.
2025-08-17 14:41:18,106 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:18,201 [INFO] Registered new session a1909e4e-62c4-4e05-b818-f694495438ee for user 'robbie'.
2025-08-17 14:41:18,205 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:18,301 [INFO] Registered new session 3a5470a9-fb99-4fa0-a31b-3f62163d50d7 for user 'robbie'.
2025-08-17 14:41:18,305 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:18,400 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:41:18,400 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:41:18,405 [INFO] Removed session 2271be7a-46ce-4e4c-b151-dd84577a27a3 for user 'robbie'.
2025-08-17 14:41:18,406 [INFO] User 'robbie' logged out and session '2271be7a-46ce-4e4c-b151-dd84577a27a3' was removed.
2025-08-17 14:41:18,501 [INFO] Registered new session 1d78b40f-3e86-4d66-b3e7-8bc02a9c4eda for user 'robbie'.
2025-08-17 14:41:18,505 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:41:18,512 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:41:18,512 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:41:18,514 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:41:18,517 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:41:18,730 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:41:18,741 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:41:18,742 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:41:18,746 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:41:19,126 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:41:19,126 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:41:19,145 [INFO] Assigned new SKU: RJC-0471. Tracker file updated.
2025-08-17 14:44:13,885 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:44:13,887 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:44:14,187 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:44:14,487 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:44:15,628 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:44:16,266 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:44:18,911 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:44:18,941 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:44:19,038 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:44:19,159 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:44:19,162 [INFO] Removed session 361f662b-c956-4583-8625-538483c6adc3 for user 'robbie'.
2025-08-17 14:44:19,162 [INFO] Removed session fde21f7f-a67d-449f-af2b-c90920784245 for user 'robbie'.
2025-08-17 14:44:19,163 [INFO] Removed session 8172f4d4-9d79-475b-a455-9e29f5a5c4da for user 'robbie'.
2025-08-17 14:44:19,257 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:44:19,263 [INFO] Registered new session 8c58e366-eadb-45b2-b6b7-6e853b77859e for user 'viewer'.
2025-08-17 14:44:19,268 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:44:19,271 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:44:19,273 [INFO] Removed session 8c58e366-eadb-45b2-b6b7-6e853b77859e for user 'viewer'.
2025-08-17 14:44:19,273 [INFO] User 'viewer' logged out and session '8c58e366-eadb-45b2-b6b7-6e853b77859e' was removed.
2025-08-17 14:44:19,367 [INFO] Registered new session d408bbe2-ef4f-4b5b-9c09-84936fc0d079 for user 'robbie'.
2025-08-17 14:44:19,371 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:19,413 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:44:19,509 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:44:19,536 [INFO] Removed session d408bbe2-ef4f-4b5b-9c09-84936fc0d079 for user 'robbie'.
2025-08-17 14:44:19,633 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:44:19,640 [INFO] Registered new session 2056ae38-5380-4f8a-a0d6-3b0b96dcef21 for user 'robbie'.
2025-08-17 14:44:19,644 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:19,650 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:44:19,696 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:44:19,794 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:44:19,916 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:44:19,916 [INFO] Removed session 2056ae38-5380-4f8a-a0d6-3b0b96dcef21 for user 'robbie'.
2025-08-17 14:44:20,010 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:44:20,017 [INFO] Registered new session 76838327-73b1-459c-9ecc-7f02f17398c4 for user 'robbie'.
2025-08-17 14:44:20,022 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:20,027 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:44:20,029 [INFO] Removed session 76838327-73b1-459c-9ecc-7f02f17398c4 for user 'robbie'.
2025-08-17 14:44:20,029 [INFO] User 'robbie' logged out and session '76838327-73b1-459c-9ecc-7f02f17398c4' was removed.
2025-08-17 14:44:20,128 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:44:20,155 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-58/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:44:20,157 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-58/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:44:20,160 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-58/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:44:20,267 [INFO] Registered new session 83c6abe0-3f30-4aa3-8a81-76446bb0b94a for user 'robbie'.
2025-08-17 14:44:20,272 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:20,314 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:44:20,318 [INFO] Removed session 83c6abe0-3f30-4aa3-8a81-76446bb0b94a for user 'robbie'.
2025-08-17 14:44:20,413 [INFO] Registered new session 0d7296ca-52a0-4359-a6d4-1944dd7db96a for user 'robbie'.
2025-08-17 14:44:20,417 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:20,424 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:44:20,427 [INFO] Removed session 0d7296ca-52a0-4359-a6d4-1944dd7db96a for user 'robbie'.
2025-08-17 14:44:20,529 [INFO] Registered new session 919be188-5b8a-4d1a-8e70-68b783ba0ecd for user 'robbie'.
2025-08-17 14:44:20,534 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:20,540 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:44:20,642 [INFO] Registered new session 3a5ed5fe-818b-4aa8-a966-fdcf2f4b1a44 for user 'robbie'.
2025-08-17 14:44:20,646 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:20,652 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-58/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:44:20,652 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-58/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:44:20,653 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-58/art_processing0/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 14:44:20,655 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 14:44:20,688 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-58/art_processing_test0
2025-08-17 14:44:20,689 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:44:20,689 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-58/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:44:20,689 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:44:20,690 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-58/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-58/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:44:20,690 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:44:20,690 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-58/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-58/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:44:20,690 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:44:20,691 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-58/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-58/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:44:20,691 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:44:20,691 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-58/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:44:20,691 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:44:20,691 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:44:20,692 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-58/art_processing_test0
2025-08-17 14:44:20,701 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-58/test_move_and_registry0/registry.json
2025-08-17 14:44:20,702 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:44:20,800 [INFO] Registered new session 77fb0fe5-8291-47f5-ac5c-7ea603c8fd15 for user 'robbie'.
2025-08-17 14:44:20,805 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:21,472 [INFO] Sellbrite authentication succeeded
2025-08-17 14:44:22,964 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:44:22,965 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:44:22,965 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:44:22,966 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:44:22,966 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:44:22,966 [ERROR] Analysis script not found: no such file
2025-08-17 14:44:23,090 [INFO] Registered new session 2b630b8c-0400-444b-a55f-9162b4b938e5 for user 'robbie'.
2025-08-17 14:44:23,095 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:23,204 [INFO] Registered new session 7cd36881-2b5c-4d23-8b44-0fcdaf44d182 for user 'robbie'.
2025-08-17 14:44:23,208 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:23,304 [INFO] Registered new session 5c5b690e-565e-4d53-8bf0-276132eb4ae8 for user 'robbie'.
2025-08-17 14:44:23,308 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:23,404 [INFO] Registered new session 65fe6034-ec3e-48a8-90ee-28ffad53e5c7 for user 'robbie'.
2025-08-17 14:44:23,408 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:23,505 [INFO] Registered new session e7483499-03f6-4f90-b9c3-99568f4bf42d for user 'robbie'.
2025-08-17 14:44:23,508 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:23,605 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:44:23,605 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:44:23,610 [INFO] Removed session 2b630b8c-0400-444b-a55f-9162b4b938e5 for user 'robbie'.
2025-08-17 14:44:23,611 [INFO] User 'robbie' logged out and session '2b630b8c-0400-444b-a55f-9162b4b938e5' was removed.
2025-08-17 14:44:23,706 [INFO] Registered new session a13a23dc-7a0c-4a02-ae97-698f53b1002d for user 'robbie'.
2025-08-17 14:44:23,711 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:44:23,718 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:44:23,718 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:44:23,720 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:44:23,723 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:44:23,860 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:44:23,865 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:44:23,866 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:44:23,867 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:44:23,965 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:44:23,965 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:44:23,972 [INFO] Assigned new SKU: RJC-0472. Tracker file updated.
2025-08-17 14:47:16,641 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:47:16,642 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:47:16,914 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:47:17,183 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:47:18,328 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:47:18,968 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:47:21,709 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:47:21,741 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:47:21,836 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:47:21,959 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:47:21,961 [INFO] Removed session 919be188-5b8a-4d1a-8e70-68b783ba0ecd for user 'robbie'.
2025-08-17 14:47:21,962 [INFO] Removed session 3a5ed5fe-818b-4aa8-a966-fdcf2f4b1a44 for user 'robbie'.
2025-08-17 14:47:21,962 [INFO] Removed session 77fb0fe5-8291-47f5-ac5c-7ea603c8fd15 for user 'robbie'.
2025-08-17 14:47:22,057 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:47:22,063 [INFO] Registered new session 23279625-a0a5-4b08-b96b-5e26fecf0f59 for user 'viewer'.
2025-08-17 14:47:22,068 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:47:22,071 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:47:22,073 [INFO] Removed session 23279625-a0a5-4b08-b96b-5e26fecf0f59 for user 'viewer'.
2025-08-17 14:47:22,074 [INFO] User 'viewer' logged out and session '23279625-a0a5-4b08-b96b-5e26fecf0f59' was removed.
2025-08-17 14:47:22,167 [INFO] Registered new session ac96ab6c-57ed-4cd5-917f-3bf17f674195 for user 'robbie'.
2025-08-17 14:47:22,171 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:22,215 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:47:22,310 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:47:22,338 [INFO] Removed session ac96ab6c-57ed-4cd5-917f-3bf17f674195 for user 'robbie'.
2025-08-17 14:47:22,433 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:47:22,439 [INFO] Registered new session f164c5c1-570b-491d-a6ec-58b4c4288a22 for user 'robbie'.
2025-08-17 14:47:22,444 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:22,450 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:47:22,493 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:47:22,589 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:47:22,711 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:47:22,711 [INFO] Removed session f164c5c1-570b-491d-a6ec-58b4c4288a22 for user 'robbie'.
2025-08-17 14:47:22,806 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:47:22,814 [INFO] Registered new session f9811ec9-b3eb-4111-90b8-23d6bcca602d for user 'robbie'.
2025-08-17 14:47:22,818 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:22,824 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:47:22,826 [INFO] Removed session f9811ec9-b3eb-4111-90b8-23d6bcca602d for user 'robbie'.
2025-08-17 14:47:22,826 [INFO] User 'robbie' logged out and session 'f9811ec9-b3eb-4111-90b8-23d6bcca602d' was removed.
2025-08-17 14:47:22,920 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:47:22,935 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-59/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:47:22,936 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-59/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:47:22,938 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-59/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:47:23,037 [INFO] Registered new session 00c75c04-5aa0-42bb-b73e-3326483a26a0 for user 'robbie'.
2025-08-17 14:47:23,041 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:23,070 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:47:23,074 [INFO] Removed session 00c75c04-5aa0-42bb-b73e-3326483a26a0 for user 'robbie'.
2025-08-17 14:47:23,168 [INFO] Registered new session bba4b64d-4ee1-4d0d-a8f4-9577ebedc4a4 for user 'robbie'.
2025-08-17 14:47:23,172 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:23,179 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:47:23,183 [INFO] Removed session bba4b64d-4ee1-4d0d-a8f4-9577ebedc4a4 for user 'robbie'.
2025-08-17 14:47:23,298 [INFO] Registered new session c310065b-eaf2-4070-83ad-d8df25ad9b30 for user 'robbie'.
2025-08-17 14:47:23,303 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:23,310 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:47:23,421 [INFO] Registered new session 68f90019-f773-491f-a611-9f6011df9fba for user 'robbie'.
2025-08-17 14:47:23,426 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:23,431 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-59/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:47:23,431 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-59/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:47:23,432 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-59/art_processing0/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 14:47:23,435 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 14:47:23,475 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-59/art_processing_test0
2025-08-17 14:47:23,476 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:47:23,476 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-59/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:47:23,476 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:47:23,477 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-59/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-59/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:47:23,477 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:47:23,478 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-59/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-59/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:47:23,478 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:47:23,478 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-59/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-59/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:47:23,478 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:47:23,478 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-59/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:47:23,478 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:47:23,479 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:47:23,479 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-59/art_processing_test0
2025-08-17 14:47:23,489 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-59/test_move_and_registry0/registry.json
2025-08-17 14:47:23,489 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:47:23,587 [INFO] Registered new session 33960dd6-4b7e-4dc9-96fd-b44cc2f70172 for user 'robbie'.
2025-08-17 14:47:23,592 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:24,263 [INFO] Sellbrite authentication succeeded
2025-08-17 14:47:25,738 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:47:25,738 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:47:25,738 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:47:25,740 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:47:25,740 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:47:25,740 [ERROR] Analysis script not found: no such file
2025-08-17 14:47:25,864 [INFO] Registered new session f47bd34c-a88a-475b-b277-913b1cb4002b for user 'robbie'.
2025-08-17 14:47:25,869 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:25,980 [INFO] Registered new session 50099bbf-b9e1-4181-ad45-3973bc62b36b for user 'robbie'.
2025-08-17 14:47:25,984 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:26,079 [INFO] Registered new session f526301e-9331-4414-a6e4-9e6b053fe7a3 for user 'robbie'.
2025-08-17 14:47:26,083 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:26,180 [INFO] Registered new session 0776a130-b639-4e67-b8da-9b2fcc709155 for user 'robbie'.
2025-08-17 14:47:26,184 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:26,280 [INFO] Registered new session 4d870799-7c79-4f7c-878e-0e33c8e576e2 for user 'robbie'.
2025-08-17 14:47:26,283 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:26,379 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:47:26,379 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:47:26,385 [INFO] Removed session f47bd34c-a88a-475b-b277-913b1cb4002b for user 'robbie'.
2025-08-17 14:47:26,385 [INFO] User 'robbie' logged out and session 'f47bd34c-a88a-475b-b277-913b1cb4002b' was removed.
2025-08-17 14:47:26,481 [INFO] Registered new session 3295747d-091c-4785-be9c-01521995421a for user 'robbie'.
2025-08-17 14:47:26,485 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:47:26,492 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:47:26,493 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:47:26,494 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:47:26,497 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:47:26,636 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:47:26,641 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:47:26,642 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:47:26,643 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:47:26,741 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:47:26,741 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:47:26,748 [INFO] Assigned new SKU: RJC-0473. Tracker file updated.
2025-08-17 14:52:59,617 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:52:59,618 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:52:59,992 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:53:00,304 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:53:01,446 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:53:02,070 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:53:04,776 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:53:04,809 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:53:04,906 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:53:05,029 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:53:05,031 [INFO] Removed session c310065b-eaf2-4070-83ad-d8df25ad9b30 for user 'robbie'.
2025-08-17 14:53:05,032 [INFO] Removed session 68f90019-f773-491f-a611-9f6011df9fba for user 'robbie'.
2025-08-17 14:53:05,032 [INFO] Removed session 33960dd6-4b7e-4dc9-96fd-b44cc2f70172 for user 'robbie'.
2025-08-17 14:53:05,127 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:53:05,133 [INFO] Registered new session bae13b37-c5c5-4719-b15e-fef81227afcb for user 'viewer'.
2025-08-17 14:53:05,138 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:53:05,141 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:53:05,144 [INFO] Removed session bae13b37-c5c5-4719-b15e-fef81227afcb for user 'viewer'.
2025-08-17 14:53:05,144 [INFO] User 'viewer' logged out and session 'bae13b37-c5c5-4719-b15e-fef81227afcb' was removed.
2025-08-17 14:53:05,238 [INFO] Registered new session 32f5e1f0-84df-4e46-90ac-947cf27428f3 for user 'robbie'.
2025-08-17 14:53:05,242 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:05,284 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:53:05,379 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:53:05,406 [INFO] Removed session 32f5e1f0-84df-4e46-90ac-947cf27428f3 for user 'robbie'.
2025-08-17 14:53:05,501 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:53:05,507 [INFO] Registered new session 8296572e-9f03-44a4-ae3a-ad549f4cba8c for user 'robbie'.
2025-08-17 14:53:05,512 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:05,517 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:53:05,561 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:53:05,656 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:53:05,777 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:53:05,777 [INFO] Removed session 8296572e-9f03-44a4-ae3a-ad549f4cba8c for user 'robbie'.
2025-08-17 14:53:05,872 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:53:05,879 [INFO] Registered new session eeb9c398-0bba-40e7-a57e-899c35a350b3 for user 'robbie'.
2025-08-17 14:53:05,884 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:05,890 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:53:05,891 [INFO] Removed session eeb9c398-0bba-40e7-a57e-899c35a350b3 for user 'robbie'.
2025-08-17 14:53:05,892 [INFO] User 'robbie' logged out and session 'eeb9c398-0bba-40e7-a57e-899c35a350b3' was removed.
2025-08-17 14:53:05,985 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:53:06,002 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-60/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:53:06,005 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-60/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:53:06,007 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-60/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:53:06,113 [INFO] Registered new session 40a202fa-ddb4-42ee-b61b-f401fb89c25d for user 'robbie'.
2025-08-17 14:53:06,117 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:06,146 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:53:06,150 [INFO] Removed session 40a202fa-ddb4-42ee-b61b-f401fb89c25d for user 'robbie'.
2025-08-17 14:53:06,245 [INFO] Registered new session cfce263d-12a3-4e06-8b67-47033349c48a for user 'robbie'.
2025-08-17 14:53:06,250 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:06,257 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:53:06,260 [INFO] Removed session cfce263d-12a3-4e06-8b67-47033349c48a for user 'robbie'.
2025-08-17 14:53:06,354 [INFO] Registered new session c4a508ab-73ed-4593-b5b9-8e5d48260584 for user 'robbie'.
2025-08-17 14:53:06,359 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:06,365 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:53:06,463 [INFO] Registered new session cbd0b659-fceb-4ca7-91ff-146f5bc6f889 for user 'robbie'.
2025-08-17 14:53:06,468 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:06,473 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-60/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:53:06,474 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-60/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:53:06,474 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-60/art_processing0/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 14:53:06,477 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 14:53:06,510 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-60/art_processing_test0
2025-08-17 14:53:06,510 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:53:06,511 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-60/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:53:06,511 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:53:06,511 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-60/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-60/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:53:06,511 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:53:06,512 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-60/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-60/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:53:06,512 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:53:06,512 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-60/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-60/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:53:06,513 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:53:06,513 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-60/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:53:06,513 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:53:06,513 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:53:06,513 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-60/art_processing_test0
2025-08-17 14:53:06,522 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-60/test_move_and_registry0/registry.json
2025-08-17 14:53:06,522 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:53:06,621 [INFO] Registered new session 15c969ec-9bd1-4633-b1c4-0d8724457447 for user 'robbie'.
2025-08-17 14:53:06,625 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:07,301 [INFO] Sellbrite authentication succeeded
2025-08-17 14:53:08,797 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:53:08,798 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:53:08,798 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:53:08,799 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:53:08,799 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:53:08,799 [ERROR] Analysis script not found: no such file
2025-08-17 14:53:08,931 [INFO] Registered new session 6c3c2736-4c6a-49ef-a742-2a98c82bb9c3 for user 'robbie'.
2025-08-17 14:53:08,936 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:09,047 [INFO] Registered new session 9be5539a-6b44-4b63-bab4-e95b5766ae22 for user 'robbie'.
2025-08-17 14:53:09,051 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:09,147 [INFO] Registered new session 208018c3-728c-4d8a-81ce-e00eb88042c9 for user 'robbie'.
2025-08-17 14:53:09,151 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:09,247 [INFO] Registered new session ca7a5053-d8dc-4b85-ab70-f9de529bc7ca for user 'robbie'.
2025-08-17 14:53:09,252 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:09,348 [INFO] Registered new session 24f2bcaf-4456-4a91-8d7c-d4f707144a06 for user 'robbie'.
2025-08-17 14:53:09,352 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:09,447 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:53:09,448 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:53:09,453 [INFO] Removed session 6c3c2736-4c6a-49ef-a742-2a98c82bb9c3 for user 'robbie'.
2025-08-17 14:53:09,454 [INFO] User 'robbie' logged out and session '6c3c2736-4c6a-49ef-a742-2a98c82bb9c3' was removed.
2025-08-17 14:53:09,551 [INFO] Registered new session 24a97b8b-30c7-4e53-8e4c-6bb4b40418d2 for user 'robbie'.
2025-08-17 14:53:09,555 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:53:09,562 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:53:09,562 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:53:09,564 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:53:09,566 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:53:09,704 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:53:09,709 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:53:09,710 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:53:09,711 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:53:09,809 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:53:09,809 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:53:09,816 [INFO] Assigned new SKU: RJC-0474. Tracker file updated.
2025-08-17 14:59:10,003 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 14:59:10,004 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 14:59:10,328 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:59:10,613 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 14:59:11,769 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 14:59:12,403 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 14:59:15,065 [ERROR] ❌ SMTP                 FAILED. AuthenticationError. Check username/password.
2025-08-17 14:59:15,103 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:59:15,247 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:59:15,435 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:59:15,438 [INFO] Removed session c4a508ab-73ed-4593-b5b9-8e5d48260584 for user 'robbie'.
2025-08-17 14:59:15,439 [INFO] Removed session cbd0b659-fceb-4ca7-91ff-146f5bc6f889 for user 'robbie'.
2025-08-17 14:59:15,440 [INFO] Removed session 15c969ec-9bd1-4633-b1c4-0d8724457447 for user 'robbie'.
2025-08-17 14:59:15,581 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:59:15,589 [INFO] Registered new session 4ce4bf74-cb8a-4a56-b06a-1c6db39d68a6 for user 'viewer'.
2025-08-17 14:59:15,595 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 14:59:15,599 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 14:59:15,602 [INFO] Removed session 4ce4bf74-cb8a-4a56-b06a-1c6db39d68a6 for user 'viewer'.
2025-08-17 14:59:15,603 [INFO] User 'viewer' logged out and session '4ce4bf74-cb8a-4a56-b06a-1c6db39d68a6' was removed.
2025-08-17 14:59:15,749 [INFO] Registered new session ba39c89f-4fb1-407e-bab3-4e3fd86b42ac for user 'robbie'.
2025-08-17 14:59:15,754 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:15,814 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:59:15,952 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:59:16,006 [INFO] Removed session ba39c89f-4fb1-407e-bab3-4e3fd86b42ac for user 'robbie'.
2025-08-17 14:59:16,137 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:59:16,144 [INFO] Registered new session a9c8097f-4f39-4c41-b87f-7e45a4e72dc9 for user 'robbie'.
2025-08-17 14:59:16,149 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:16,157 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 14:59:16,215 [INFO] Users table is empty. Creating default admin user.
2025-08-17 14:59:16,346 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 14:59:16,522 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 14:59:16,522 [INFO] Removed session a9c8097f-4f39-4c41-b87f-7e45a4e72dc9 for user 'robbie'.
2025-08-17 14:59:16,647 [INFO] No site settings found in database; creating new default record.
2025-08-17 14:59:16,655 [INFO] Registered new session 74c64883-f445-4bba-809f-a46c58772813 for user 'robbie'.
2025-08-17 14:59:16,660 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:16,667 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 14:59:16,670 [INFO] Removed session 74c64883-f445-4bba-809f-a46c58772813 for user 'robbie'.
2025-08-17 14:59:16,670 [INFO] User 'robbie' logged out and session '74c64883-f445-4bba-809f-a46c58772813' was removed.
2025-08-17 14:59:16,794 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 14:59:16,816 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-61/test_load_json_file_safe_missi0/missing.json
2025-08-17 14:59:16,818 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-61/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 14:59:16,821 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-61/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 14:59:16,958 [INFO] Registered new session 96c469f9-246f-424f-b7f0-6b11a67dcddb for user 'robbie'.
2025-08-17 14:59:16,963 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:17,007 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 14:59:17,022 [INFO] Removed session 96c469f9-246f-424f-b7f0-6b11a67dcddb for user 'robbie'.
2025-08-17 14:59:17,166 [INFO] Registered new session baf8fa84-741f-4bfd-8377-e8cb6be3f1bb for user 'robbie'.
2025-08-17 14:59:17,171 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:17,181 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 14:59:17,199 [INFO] Removed session baf8fa84-741f-4bfd-8377-e8cb6be3f1bb for user 'robbie'.
2025-08-17 14:59:17,346 [INFO] Registered new session 90c93ad5-d5dd-43a7-b4c6-c08ebe046a1c for user 'robbie'.
2025-08-17 14:59:17,350 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:17,359 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 14:59:17,518 [INFO] Registered new session 564cbfb8-14f7-4590-8227-abec68835327 for user 'robbie'.
2025-08-17 14:59:17,522 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:17,530 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-61/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 14:59:17,530 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-61/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 14:59:17,532 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-61/art_processing0/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 14:59:17,536 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 14:59:17,596 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-61/art_processing_test0
2025-08-17 14:59:17,597 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 14:59:17,598 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-61/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 14:59:17,598 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 14:59:17,599 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-61/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-61/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:59:17,599 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 14:59:17,599 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-61/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-61/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:59:17,600 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 14:59:17,600 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-61/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-61/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 14:59:17,600 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 14:59:17,601 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-61/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:59:17,601 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 14:59:17,601 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 14:59:17,602 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-61/art_processing_test0
2025-08-17 14:59:17,616 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-61/test_move_and_registry0/registry.json
2025-08-17 14:59:17,616 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 14:59:17,758 [INFO] Registered new session abfed19a-8a49-4721-b0d2-08da1fc553ad for user 'robbie'.
2025-08-17 14:59:17,762 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:18,461 [INFO] Sellbrite authentication succeeded
2025-08-17 14:59:19,967 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:59:19,967 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:59:19,967 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 14:59:19,968 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 14:59:19,968 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 14:59:19,968 [ERROR] Analysis script not found: no such file
2025-08-17 14:59:20,092 [INFO] Registered new session 2c6ba3ff-9f34-4985-93aa-071ab9989821 for user 'robbie'.
2025-08-17 14:59:20,096 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:20,206 [INFO] Registered new session 115f1ad2-dfb5-47b8-a3a0-e95af0bacd14 for user 'robbie'.
2025-08-17 14:59:20,210 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:20,306 [INFO] Registered new session 106e7fee-b9ac-4f60-aaba-0262cc6baf59 for user 'robbie'.
2025-08-17 14:59:20,309 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:20,406 [INFO] Registered new session 0e983f0d-fc1e-4265-94b5-7e5ef6ad0dcc for user 'robbie'.
2025-08-17 14:59:20,409 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:20,507 [INFO] Registered new session 9009fd7e-7576-49e1-ac70-8b81664233b8 for user 'robbie'.
2025-08-17 14:59:20,511 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:20,607 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:59:20,607 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:59:20,612 [INFO] Removed session 2c6ba3ff-9f34-4985-93aa-071ab9989821 for user 'robbie'.
2025-08-17 14:59:20,613 [INFO] User 'robbie' logged out and session '2c6ba3ff-9f34-4985-93aa-071ab9989821' was removed.
2025-08-17 14:59:20,707 [INFO] Registered new session f1653991-db84-440d-a5a6-a295ffa225c1 for user 'robbie'.
2025-08-17 14:59:20,711 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 14:59:20,718 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 14:59:20,719 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 14:59:20,720 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 14:59:20,723 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 14:59:20,855 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-61/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0081-by-robin-custance-rjc-rjc-0081
2025-08-17 14:59:20,856 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 14:59:20,860 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-61/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0082-by-robin-custance-rjc-rjc-0082
2025-08-17 14:59:20,861 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 14:59:20,862 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 14:59:20,863 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 14:59:20,867 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-61/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0085-by-robin-custance-rjc-rjc-0085
2025-08-17 14:59:20,960 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 14:59:20,961 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 14:59:20,967 [INFO] Assigned new SKU: RJC-0475. Tracker file updated.
2025-08-17 15:44:07,276 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 15:44:07,280 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 15:44:07,518 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 15:44:08,413 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 15:44:09,556 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 15:44:10,199 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 15:44:10,228 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:44:10,323 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:44:10,444 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 15:44:10,446 [INFO] Removed session 90c93ad5-d5dd-43a7-b4c6-c08ebe046a1c for user 'robbie'.
2025-08-17 15:44:10,447 [INFO] Removed session 564cbfb8-14f7-4590-8227-abec68835327 for user 'robbie'.
2025-08-17 15:44:10,447 [INFO] Removed session abfed19a-8a49-4721-b0d2-08da1fc553ad for user 'robbie'.
2025-08-17 15:44:10,542 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:44:10,548 [INFO] Registered new session 9032ad45-28af-4a95-9dee-1fc528d74f2a for user 'viewer'.
2025-08-17 15:44:10,553 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 15:44:10,556 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 15:44:10,558 [INFO] Removed session 9032ad45-28af-4a95-9dee-1fc528d74f2a for user 'viewer'.
2025-08-17 15:44:10,558 [INFO] User 'viewer' logged out and session '9032ad45-28af-4a95-9dee-1fc528d74f2a' was removed.
2025-08-17 15:44:10,660 [INFO] Registered new session 39918f04-10a0-4763-b030-e471fc3a2b8c for user 'robbie'.
2025-08-17 15:44:10,666 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:10,720 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:44:10,834 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:44:10,865 [INFO] Removed session 39918f04-10a0-4763-b030-e471fc3a2b8c for user 'robbie'.
2025-08-17 15:44:10,961 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:44:10,967 [INFO] Registered new session e8b61ffa-00a7-45bb-bcfd-a17bc0c24b86 for user 'robbie'.
2025-08-17 15:44:10,972 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:10,977 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 15:44:11,019 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:44:11,114 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:44:11,234 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 15:44:11,234 [INFO] Removed session e8b61ffa-00a7-45bb-bcfd-a17bc0c24b86 for user 'robbie'.
2025-08-17 15:44:11,329 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:44:11,336 [INFO] Registered new session a50fb403-646f-49f7-8cf8-721513076038 for user 'robbie'.
2025-08-17 15:44:11,340 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:11,346 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 15:44:11,347 [INFO] Removed session a50fb403-646f-49f7-8cf8-721513076038 for user 'robbie'.
2025-08-17 15:44:11,348 [INFO] User 'robbie' logged out and session 'a50fb403-646f-49f7-8cf8-721513076038' was removed.
2025-08-17 15:44:11,442 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 15:44:11,458 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-62/test_load_json_file_safe_missi0/missing.json
2025-08-17 15:44:11,460 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-62/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 15:44:11,462 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-62/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 15:44:11,560 [INFO] Registered new session 5b66c5b4-2273-4932-8236-fb48f2559d4e for user 'robbie'.
2025-08-17 15:44:11,564 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:11,594 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/dummy-artwork
2025-08-17 15:44:11,598 [INFO] Removed session 5b66c5b4-2273-4932-8236-fb48f2559d4e for user 'robbie'.
2025-08-17 15:44:11,691 [INFO] Registered new session 02d30c49-44e8-4499-8073-0aa3708eb569 for user 'robbie'.
2025-08-17 15:44:11,695 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:11,702 [INFO] Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/byte-art
2025-08-17 15:44:11,705 [INFO] Removed session 02d30c49-44e8-4499-8073-0aa3708eb569 for user 'robbie'.
2025-08-17 15:44:11,797 [INFO] Registered new session c895e53b-e560-4466-99bb-e27cd6a177d2 for user 'robbie'.
2025-08-17 15:44:11,802 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:11,808 [ERROR] ❌ Error running analysis: b'oops'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: b'oops'
2025-08-17 15:44:11,905 [INFO] Registered new session 674dfa48-3f55-4b76-9303-d8bd27191f9b for user 'robbie'.
2025-08-17 15:44:11,909 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:11,915 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-62/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 15:44:11,915 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-62/art_processing0/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 15:44:11,916 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-62/art_processing0/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 15:44:11,918 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 15:44:11,952 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-62/art_processing_test0
2025-08-17 15:44:11,953 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 15:44:11,953 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-62/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 15:44:11,953 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 15:44:11,954 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-62/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-62/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:44:11,954 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 15:44:11,954 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-62/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-62/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:44:11,954 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 15:44:11,955 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-62/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-62/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:44:11,955 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 15:44:11,955 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-62/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 15:44:11,955 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 15:44:11,955 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 15:44:11,956 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-62/art_processing_test0
2025-08-17 15:44:11,964 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-62/test_move_and_registry0/registry.json
2025-08-17 15:44:11,965 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 15:44:12,062 [INFO] Registered new session 5f45f3c6-1c75-40fc-905a-15f9705a8971 for user 'robbie'.
2025-08-17 15:44:12,067 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:12,755 [INFO] Sellbrite authentication succeeded
2025-08-17 15:44:14,407 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 15:44:14,407 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 15:44:14,407 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 15:44:14,408 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 15:44:14,409 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 15:44:14,409 [ERROR] Analysis script not found: no such file
2025-08-17 15:44:14,532 [INFO] Registered new session 913a1147-a5ed-4a14-8e76-d480c96d9b63 for user 'robbie'.
2025-08-17 15:44:14,536 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:14,644 [INFO] Registered new session de0451bb-dd2b-4b3d-bdea-e70d156b8618 for user 'robbie'.
2025-08-17 15:44:14,648 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:14,745 [INFO] Registered new session b9ff5ba4-1407-4b2d-8ed9-90f60d679607 for user 'robbie'.
2025-08-17 15:44:14,749 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:14,844 [INFO] Registered new session 33e2a2ca-6ace-419a-9e10-ddd65bb2d933 for user 'robbie'.
2025-08-17 15:44:14,848 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:14,947 [INFO] Registered new session 3bb9f3aa-c15a-4922-a9d6-ceb67faa2845 for user 'robbie'.
2025-08-17 15:44:14,950 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:15,046 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 15:44:15,046 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 15:44:15,051 [INFO] Removed session 913a1147-a5ed-4a14-8e76-d480c96d9b63 for user 'robbie'.
2025-08-17 15:44:15,051 [INFO] User 'robbie' logged out and session '913a1147-a5ed-4a14-8e76-d480c96d9b63' was removed.
2025-08-17 15:44:15,145 [INFO] Registered new session ee630ba3-35ce-4c35-9649-0966f3135c86 for user 'robbie'.
2025-08-17 15:44:15,149 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:44:15,157 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 15:44:15,157 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 15:44:15,159 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 15:44:15,161 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 15:44:15,295 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-62/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0081-by-robin-custance-rjc-rjc-0081
2025-08-17 15:44:15,295 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 15:44:15,300 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-62/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0082-by-robin-custance-rjc-rjc-0082
2025-08-17 15:44:15,301 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 15:44:15,301 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 15:44:15,302 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 15:44:15,306 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-62/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0085-by-robin-custance-rjc-rjc-0085
2025-08-17 15:44:15,399 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 15:44:15,399 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 15:44:15,406 [INFO] Assigned new SKU: RJC-0476. Tracker file updated.
2025-08-17 15:48:08,923 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 15:48:08,924 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 15:48:09,257 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 15:48:09,673 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 15:48:10,831 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 15:48:11,466 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 15:48:11,496 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:48:11,592 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:48:11,715 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 15:48:11,717 [INFO] Removed session c895e53b-e560-4466-99bb-e27cd6a177d2 for user 'robbie'.
2025-08-17 15:48:11,718 [INFO] Removed session 674dfa48-3f55-4b76-9303-d8bd27191f9b for user 'robbie'.
2025-08-17 15:48:11,718 [INFO] Removed session 5f45f3c6-1c75-40fc-905a-15f9705a8971 for user 'robbie'.
2025-08-17 15:48:11,814 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:48:11,821 [INFO] Registered new session ceba0a74-636d-4720-9184-f7acf9ddb096 for user 'viewer'.
2025-08-17 15:48:11,826 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 15:48:11,829 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 15:48:11,831 [INFO] Removed session ceba0a74-636d-4720-9184-f7acf9ddb096 for user 'viewer'.
2025-08-17 15:48:11,831 [INFO] User 'viewer' logged out and session 'ceba0a74-636d-4720-9184-f7acf9ddb096' was removed.
2025-08-17 15:48:11,928 [INFO] Registered new session 9fea1ff2-e17b-43f6-ae4b-4f0c51d632c4 for user 'robbie'.
2025-08-17 15:48:11,932 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:11,975 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:48:12,071 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:48:12,097 [INFO] Removed session 9fea1ff2-e17b-43f6-ae4b-4f0c51d632c4 for user 'robbie'.
2025-08-17 15:48:12,193 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:48:12,199 [INFO] Registered new session ed078dc7-1469-49ea-9926-af6aaaa36400 for user 'robbie'.
2025-08-17 15:48:12,203 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:12,209 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 15:48:12,253 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:48:12,348 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:48:12,468 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 15:48:12,469 [INFO] Removed session ed078dc7-1469-49ea-9926-af6aaaa36400 for user 'robbie'.
2025-08-17 15:48:12,564 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:48:12,571 [INFO] Registered new session 1814ba53-c25b-473e-b965-03023ec3c0ca for user 'robbie'.
2025-08-17 15:48:12,575 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:12,581 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 15:48:12,583 [INFO] Removed session 1814ba53-c25b-473e-b965-03023ec3c0ca for user 'robbie'.
2025-08-17 15:48:12,583 [INFO] User 'robbie' logged out and session '1814ba53-c25b-473e-b965-03023ec3c0ca' was removed.
2025-08-17 15:48:12,677 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 15:48:12,692 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-63/test_load_json_file_safe_missi0/missing.json
2025-08-17 15:48:12,694 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-63/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 15:48:12,695 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-63/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 15:48:12,793 [INFO] Registered new session 822f4f49-3956-489d-aefd-1249952dfa39 for user 'robbie'.
2025-08-17 15:48:12,798 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:12,826 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-63/art_processing0/processed-artwork/dummy-artwork
2025-08-17 15:48:12,921 [INFO] Registered new session fa33a18a-b9b3-42ab-911c-78eb19707054 for user 'robbie'.
2025-08-17 15:48:12,926 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:12,932 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-63/art_processing1/processed-artwork/byte-art
2025-08-17 15:48:13,028 [INFO] Registered new session d70c3879-e67e-4da0-9547-55b43a76c4b9 for user 'robbie'.
2025-08-17 15:48:13,033 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:13,038 [ERROR] ❌ Error running analysis: A critical analysis error
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: A critical analysis error
2025-08-17 15:48:13,136 [INFO] Registered new session 49a909c2-86fc-4a51-a9bb-526f55c02424 for user 'robbie'.
2025-08-17 15:48:13,140 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:13,145 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-63/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 15:48:13,145 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-63/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 15:48:13,146 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-63/art_processing3/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 15:48:13,149 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 15:48:13,181 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-63/art_processing_test0
2025-08-17 15:48:13,182 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 15:48:13,182 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-63/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 15:48:13,183 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 15:48:13,183 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-63/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-63/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:48:13,183 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 15:48:13,184 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-63/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-63/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:48:13,184 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 15:48:13,184 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-63/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-63/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:48:13,184 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 15:48:13,184 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-63/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 15:48:13,184 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 15:48:13,184 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 15:48:13,185 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-63/art_processing_test0
2025-08-17 15:48:13,193 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-63/test_move_and_registry0/registry.json
2025-08-17 15:48:13,194 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 15:48:13,294 [INFO] Registered new session e50e6ae0-80ac-48c7-87a6-5f08f00f0b2b for user 'robbie'.
2025-08-17 15:48:13,299 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:13,983 [INFO] Sellbrite authentication succeeded
2025-08-17 15:48:15,476 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 15:48:15,476 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 15:48:15,476 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 15:48:15,478 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 15:48:15,478 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 15:48:15,478 [ERROR] Analysis script not found: no such file
2025-08-17 15:48:15,601 [INFO] Registered new session b5491a77-6b16-461c-95a6-301958b0613a for user 'robbie'.
2025-08-17 15:48:15,605 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:15,715 [INFO] Registered new session 8398b8a3-7b78-4305-88c5-55cb91f32222 for user 'robbie'.
2025-08-17 15:48:15,719 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:15,817 [INFO] Registered new session 6940b786-b4ef-4c1b-a9f0-135b4fd7ae05 for user 'robbie'.
2025-08-17 15:48:15,822 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:15,945 [INFO] Registered new session a03c7585-ff6c-4a18-a0a1-d039655e93ef for user 'robbie'.
2025-08-17 15:48:15,950 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:16,050 [INFO] Registered new session 7c4fa843-34c6-4423-9fa6-430bd68b174c for user 'robbie'.
2025-08-17 15:48:16,054 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:16,151 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 15:48:16,151 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 15:48:16,156 [INFO] Removed session b5491a77-6b16-461c-95a6-301958b0613a for user 'robbie'.
2025-08-17 15:48:16,157 [INFO] User 'robbie' logged out and session 'b5491a77-6b16-461c-95a6-301958b0613a' was removed.
2025-08-17 15:48:16,252 [INFO] Registered new session 62911943-f384-4249-88b1-913a6d139d80 for user 'robbie'.
2025-08-17 15:48:16,257 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:48:16,264 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 15:48:16,264 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 15:48:16,266 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 15:48:16,269 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 15:48:16,400 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-63/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0081-by-robin-custance-rjc-rjc-0081
2025-08-17 15:48:16,401 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 15:48:16,406 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-63/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0082-by-robin-custance-rjc-rjc-0082
2025-08-17 15:48:16,406 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 15:48:16,407 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 15:48:16,408 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 15:48:16,412 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-63/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0085-by-robin-custance-rjc-rjc-0085
2025-08-17 15:48:16,507 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 15:48:16,507 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 15:48:16,514 [INFO] Assigned new SKU: RJC-0477. Tracker file updated.
2025-08-17 15:49:33,003 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:49:33,108 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:49:33,229 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 15:49:33,231 [INFO] Removed session 822f4f49-3956-489d-aefd-1249952dfa39 for user 'robbie'.
2025-08-17 15:49:33,231 [INFO] Removed session fa33a18a-b9b3-42ab-911c-78eb19707054 for user 'robbie'.
2025-08-17 15:49:33,232 [INFO] Removed session d70c3879-e67e-4da0-9547-55b43a76c4b9 for user 'robbie'.
2025-08-17 15:49:33,232 [INFO] Removed session 49a909c2-86fc-4a51-a9bb-526f55c02424 for user 'robbie'.
2025-08-17 15:49:33,233 [INFO] Removed session e50e6ae0-80ac-48c7-87a6-5f08f00f0b2b for user 'robbie'.
2025-08-17 15:49:33,327 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:49:33,333 [INFO] Registered new session a58abc7e-2073-453f-b605-b27f9589677c for user 'viewer'.
2025-08-17 15:49:33,338 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 15:49:33,341 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 15:49:33,342 [INFO] Removed session a58abc7e-2073-453f-b605-b27f9589677c for user 'viewer'.
2025-08-17 15:49:33,343 [INFO] User 'viewer' logged out and session 'a58abc7e-2073-453f-b605-b27f9589677c' was removed.
2025-08-17 15:49:33,435 [INFO] Registered new session 0325e955-562d-47f9-8ee1-bbda81dfe141 for user 'robbie'.
2025-08-17 15:49:33,439 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:33,481 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:49:33,575 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:49:33,600 [INFO] Removed session 0325e955-562d-47f9-8ee1-bbda81dfe141 for user 'robbie'.
2025-08-17 15:49:33,695 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:49:33,700 [INFO] Registered new session bf696f51-4e34-46a3-802e-eb6c83354e53 for user 'robbie'.
2025-08-17 15:49:33,704 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:33,710 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 15:49:33,753 [INFO] Users table is empty. Creating default admin user.
2025-08-17 15:49:33,848 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 15:49:33,989 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 15:49:33,990 [INFO] Removed session bf696f51-4e34-46a3-802e-eb6c83354e53 for user 'robbie'.
2025-08-17 15:49:34,098 [INFO] No site settings found in database; creating new default record.
2025-08-17 15:49:34,107 [INFO] Registered new session dbbc1172-1f88-4aab-b766-773511b1f1c3 for user 'robbie'.
2025-08-17 15:49:34,111 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:34,117 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 15:49:34,119 [INFO] Removed session dbbc1172-1f88-4aab-b766-773511b1f1c3 for user 'robbie'.
2025-08-17 15:49:34,119 [INFO] User 'robbie' logged out and session 'dbbc1172-1f88-4aab-b766-773511b1f1c3' was removed.
2025-08-17 15:49:34,216 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 15:49:34,232 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-64/test_load_json_file_safe_missi0/missing.json
2025-08-17 15:49:34,234 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-64/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 15:49:34,235 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-64/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 15:49:34,335 [INFO] Registered new session a0cb42a3-8a3a-44ce-958d-6cf15bf667ba for user 'robbie'.
2025-08-17 15:49:34,340 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:34,367 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-64/art_processing0/processed-artwork/dummy-artwork
2025-08-17 15:49:34,463 [INFO] Registered new session 0f0d1e11-755f-4c64-8443-4a017e7e5cca for user 'robbie'.
2025-08-17 15:49:34,467 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:34,474 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-64/art_processing1/processed-artwork/byte-art
2025-08-17 15:49:34,569 [INFO] Registered new session 4ff30b18-5b1a-40fb-a357-c80b66d7f452 for user 'robbie'.
2025-08-17 15:49:34,573 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:34,578 [ERROR] ❌ Error running analysis: A critical analysis error
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: A critical analysis error
2025-08-17 15:49:34,675 [INFO] Registered new session c7bf5a11-baa4-40a2-9065-d380e71e81f7 for user 'robbie'.
2025-08-17 15:49:34,679 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:34,685 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-64/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 15:49:34,685 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-64/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 15:49:34,686 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-64/art_processing3/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 15:49:34,688 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 15:49:34,729 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-64/art_processing_test0
2025-08-17 15:49:34,730 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 15:49:34,730 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-64/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 15:49:34,730 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 15:49:34,731 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-64/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-64/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:49:34,731 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 15:49:34,731 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-64/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-64/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:49:34,731 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 15:49:34,732 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-64/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-64/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 15:49:34,732 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 15:49:34,732 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-64/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 15:49:34,732 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 15:49:34,733 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 15:49:34,733 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-64/art_processing_test0
2025-08-17 15:49:34,742 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-64/test_move_and_registry0/registry.json
2025-08-17 15:49:34,742 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 15:49:34,841 [INFO] Registered new session cd0f0630-c109-41f4-8324-7b41ed7e3b59 for user 'robbie'.
2025-08-17 15:49:34,846 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:35,566 [INFO] Sellbrite authentication succeeded
2025-08-17 15:49:37,038 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 15:49:37,038 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 15:49:37,038 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 15:49:37,039 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 15:49:37,039 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 15:49:37,039 [ERROR] Analysis script not found: no such file
2025-08-17 15:49:37,163 [INFO] Registered new session 6683de76-78ee-4eb9-9a9f-8cfe94c9a36d for user 'robbie'.
2025-08-17 15:49:37,168 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:37,276 [INFO] Registered new session c4a5fdb6-81a2-45aa-9be1-9bd20e54ae67 for user 'robbie'.
2025-08-17 15:49:37,280 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:37,376 [INFO] Registered new session b3c7a3c9-0ff9-4010-9e36-754670fa891c for user 'robbie'.
2025-08-17 15:49:37,380 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:37,476 [INFO] Registered new session 9eae1646-ed53-4f76-9614-c0db2c30e414 for user 'robbie'.
2025-08-17 15:49:37,480 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:37,577 [INFO] Registered new session 0ccc8d40-02cc-4fd8-966b-da476d961665 for user 'robbie'.
2025-08-17 15:49:37,581 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:37,677 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 15:49:37,677 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 15:49:37,682 [INFO] Removed session 6683de76-78ee-4eb9-9a9f-8cfe94c9a36d for user 'robbie'.
2025-08-17 15:49:37,683 [INFO] User 'robbie' logged out and session '6683de76-78ee-4eb9-9a9f-8cfe94c9a36d' was removed.
2025-08-17 15:49:37,777 [INFO] Registered new session a8259567-c9a1-465f-a1e9-459852740290 for user 'robbie'.
2025-08-17 15:49:37,781 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 15:49:37,788 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 15:49:37,788 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 15:49:37,790 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 15:49:37,793 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 15:49:37,802 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-64/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0081-by-robin-custance-rjc-rjc-0081
2025-08-17 15:49:37,803 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 15:49:37,807 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-64/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0082-by-robin-custance-rjc-rjc-0082
2025-08-17 15:49:37,807 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 15:49:37,808 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 15:49:37,809 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 15:49:37,813 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-64/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0085-by-robin-custance-rjc-rjc-0085
2025-08-17 15:49:37,908 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 15:49:37,908 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 15:49:37,915 [INFO] Assigned new SKU: RJC-0478. Tracker file updated.
2025-08-17 16:15:19,493 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 16:15:19,494 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 16:15:19,776 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 16:15:20,244 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 16:15:21,394 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 16:15:22,022 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 16:15:22,051 [INFO] Users table is empty. Creating default admin user.
2025-08-17 16:15:22,147 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 16:15:22,268 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 16:15:22,270 [INFO] Removed session a0cb42a3-8a3a-44ce-958d-6cf15bf667ba for user 'robbie'.
2025-08-17 16:15:22,271 [INFO] Removed session 0f0d1e11-755f-4c64-8443-4a017e7e5cca for user 'robbie'.
2025-08-17 16:15:22,271 [INFO] Removed session 4ff30b18-5b1a-40fb-a357-c80b66d7f452 for user 'robbie'.
2025-08-17 16:15:22,271 [INFO] Removed session c7bf5a11-baa4-40a2-9065-d380e71e81f7 for user 'robbie'.
2025-08-17 16:15:22,272 [INFO] Removed session cd0f0630-c109-41f4-8324-7b41ed7e3b59 for user 'robbie'.
2025-08-17 16:15:22,365 [INFO] No site settings found in database; creating new default record.
2025-08-17 16:15:22,371 [INFO] Registered new session 443db124-ab6a-43df-a549-29758dcacd0e for user 'viewer'.
2025-08-17 16:15:22,376 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 16:15:22,378 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 16:15:22,380 [INFO] Removed session 443db124-ab6a-43df-a549-29758dcacd0e for user 'viewer'.
2025-08-17 16:15:22,380 [INFO] User 'viewer' logged out and session '443db124-ab6a-43df-a549-29758dcacd0e' was removed.
2025-08-17 16:15:22,475 [INFO] Registered new session 997cf4bf-d505-4906-8b7e-2adc0c9d0f09 for user 'robbie'.
2025-08-17 16:15:22,479 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:22,519 [INFO] Users table is empty. Creating default admin user.
2025-08-17 16:15:22,613 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 16:15:22,639 [INFO] Removed session 997cf4bf-d505-4906-8b7e-2adc0c9d0f09 for user 'robbie'.
2025-08-17 16:15:22,735 [INFO] No site settings found in database; creating new default record.
2025-08-17 16:15:22,741 [INFO] Registered new session 3eb88615-0ca7-4142-8639-57b6320e39c3 for user 'robbie'.
2025-08-17 16:15:22,745 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:22,751 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 16:15:22,791 [INFO] Users table is empty. Creating default admin user.
2025-08-17 16:15:22,908 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 16:15:23,045 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 16:15:23,045 [INFO] Removed session 3eb88615-0ca7-4142-8639-57b6320e39c3 for user 'robbie'.
2025-08-17 16:15:23,146 [INFO] No site settings found in database; creating new default record.
2025-08-17 16:15:23,153 [INFO] Registered new session a78cf44e-9863-4448-9c2e-ad42f72e5aa4 for user 'robbie'.
2025-08-17 16:15:23,156 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:23,162 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 16:15:23,163 [INFO] Removed session a78cf44e-9863-4448-9c2e-ad42f72e5aa4 for user 'robbie'.
2025-08-17 16:15:23,164 [INFO] User 'robbie' logged out and session 'a78cf44e-9863-4448-9c2e-ad42f72e5aa4' was removed.
2025-08-17 16:15:23,259 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 16:15:23,275 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-65/test_load_json_file_safe_missi0/missing.json
2025-08-17 16:15:23,276 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-65/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 16:15:23,278 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-65/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 16:15:23,376 [INFO] Registered new session c5777dd3-9048-4444-ba0e-62c66f29a615 for user 'robbie'.
2025-08-17 16:15:23,380 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:23,408 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-65/art_processing0/processed-artwork/dummy-artwork
2025-08-17 16:15:23,504 [INFO] Registered new session 1d21a40e-423b-4e60-8997-1044357c4edd for user 'robbie'.
2025-08-17 16:15:23,508 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:23,514 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-65/art_processing1/processed-artwork/byte-art
2025-08-17 16:15:23,614 [INFO] Registered new session 0631eb7c-e634-43dc-b538-acf38a81b534 for user 'robbie'.
2025-08-17 16:15:23,618 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:23,623 [ERROR] ❌ Error running analysis: A critical analysis error
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: A critical analysis error
2025-08-17 16:15:23,721 [INFO] Registered new session 7ea7dd74-e1a1-4fb1-af4e-994138b86db4 for user 'robbie'.
2025-08-17 16:15:23,725 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:23,731 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-65/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 16:15:23,731 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-65/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 16:15:23,732 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-65/art_processing3/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 16:15:23,734 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 16:15:23,767 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-65/art_processing_test0
2025-08-17 16:15:23,768 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 16:15:23,768 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-65/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 16:15:23,768 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 16:15:23,769 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-65/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-65/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 16:15:23,769 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 16:15:23,769 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-65/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-65/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 16:15:23,770 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 16:15:23,770 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-65/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-65/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 16:15:23,770 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 16:15:23,770 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-65/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 16:15:23,770 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 16:15:23,770 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 16:15:23,771 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-65/art_processing_test0
2025-08-17 16:15:23,779 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-65/test_move_and_registry0/registry.json
2025-08-17 16:15:23,779 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 16:15:23,877 [INFO] Registered new session 726a26b5-053a-4c22-9cb8-6dea882dd258 for user 'robbie'.
2025-08-17 16:15:23,882 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:24,588 [INFO] Sellbrite authentication succeeded
2025-08-17 16:15:26,109 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 16:15:26,109 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 16:15:26,109 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 16:15:26,111 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 16:15:26,111 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 16:15:26,111 [ERROR] Analysis script not found: no such file
2025-08-17 16:15:26,234 [INFO] Registered new session 9738e65f-4140-4357-b7ca-2d22364766d4 for user 'robbie'.
2025-08-17 16:15:26,238 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:26,347 [INFO] Registered new session 1624b138-5713-44c9-b59a-fd143a2c44c6 for user 'robbie'.
2025-08-17 16:15:26,351 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:26,447 [INFO] Registered new session 51368f29-8d42-4f08-b540-fa253d625c07 for user 'robbie'.
2025-08-17 16:15:26,450 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:26,545 [INFO] Registered new session 572acd2e-c3f1-4e36-94b6-5be47791f0f7 for user 'robbie'.
2025-08-17 16:15:26,549 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:26,646 [INFO] Registered new session 8aa966bd-cf64-4d03-b8a4-e25fb9b92a8f for user 'robbie'.
2025-08-17 16:15:26,649 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:26,744 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 16:15:26,745 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 16:15:26,750 [INFO] Removed session 9738e65f-4140-4357-b7ca-2d22364766d4 for user 'robbie'.
2025-08-17 16:15:26,750 [INFO] User 'robbie' logged out and session '9738e65f-4140-4357-b7ca-2d22364766d4' was removed.
2025-08-17 16:15:26,848 [INFO] Registered new session 5192c63e-0c7c-479a-8dc0-c1bf91c4a5b1 for user 'robbie'.
2025-08-17 16:15:26,852 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:15:26,859 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 16:15:26,859 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 16:15:26,861 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 16:15:26,864 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 16:15:26,993 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-65/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0081-by-robin-custance-rjc-rjc-0081
2025-08-17 16:15:26,994 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 16:15:26,998 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-65/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0082-by-robin-custance-rjc-rjc-0082
2025-08-17 16:15:26,999 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 16:15:26,999 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 16:15:27,000 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 16:15:27,004 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-65/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0085-by-robin-custance-rjc-rjc-0085
2025-08-17 16:15:27,098 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 16:15:27,098 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 16:15:27,105 [INFO] Assigned new SKU: RJC-0479. Tracker file updated.
2025-08-17 16:19:52,064 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 16:19:52,065 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 16:19:52,376 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 16:19:52,671 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 16:19:53,806 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 16:19:54,445 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 16:19:54,476 [INFO] Users table is empty. Creating default admin user.
2025-08-17 16:19:54,571 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 16:19:54,692 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 16:19:54,695 [INFO] Removed session c5777dd3-9048-4444-ba0e-62c66f29a615 for user 'robbie'.
2025-08-17 16:19:54,695 [INFO] Removed session 1d21a40e-423b-4e60-8997-1044357c4edd for user 'robbie'.
2025-08-17 16:19:54,696 [INFO] Removed session 0631eb7c-e634-43dc-b538-acf38a81b534 for user 'robbie'.
2025-08-17 16:19:54,697 [INFO] Removed session 7ea7dd74-e1a1-4fb1-af4e-994138b86db4 for user 'robbie'.
2025-08-17 16:19:54,697 [INFO] Removed session 726a26b5-053a-4c22-9cb8-6dea882dd258 for user 'robbie'.
2025-08-17 16:19:54,792 [INFO] No site settings found in database; creating new default record.
2025-08-17 16:19:54,799 [INFO] Registered new session a480331d-489a-48c7-8886-569b7e76e4e8 for user 'viewer'.
2025-08-17 16:19:54,804 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 16:19:54,807 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 16:19:54,809 [INFO] Removed session a480331d-489a-48c7-8886-569b7e76e4e8 for user 'viewer'.
2025-08-17 16:19:54,809 [INFO] User 'viewer' logged out and session 'a480331d-489a-48c7-8886-569b7e76e4e8' was removed.
2025-08-17 16:19:54,909 [INFO] Registered new session 6c4340e8-4595-47b8-87e7-43d281ac0616 for user 'robbie'.
2025-08-17 16:19:54,913 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:54,955 [INFO] Users table is empty. Creating default admin user.
2025-08-17 16:19:55,049 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 16:19:55,075 [INFO] Removed session 6c4340e8-4595-47b8-87e7-43d281ac0616 for user 'robbie'.
2025-08-17 16:19:55,169 [INFO] No site settings found in database; creating new default record.
2025-08-17 16:19:55,175 [INFO] Registered new session 6b3bad07-846a-444b-aeff-2c94bbd3fa63 for user 'robbie'.
2025-08-17 16:19:55,180 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:55,186 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 16:19:55,231 [INFO] Users table is empty. Creating default admin user.
2025-08-17 16:19:55,326 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 16:19:55,463 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 16:19:55,464 [INFO] Removed session 6b3bad07-846a-444b-aeff-2c94bbd3fa63 for user 'robbie'.
2025-08-17 16:19:55,566 [INFO] No site settings found in database; creating new default record.
2025-08-17 16:19:55,573 [INFO] Registered new session 3f747638-7ea2-48d7-b7ee-1aaee429aec8 for user 'robbie'.
2025-08-17 16:19:55,577 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:55,584 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 16:19:55,586 [INFO] Removed session 3f747638-7ea2-48d7-b7ee-1aaee429aec8 for user 'robbie'.
2025-08-17 16:19:55,587 [INFO] User 'robbie' logged out and session '3f747638-7ea2-48d7-b7ee-1aaee429aec8' was removed.
2025-08-17 16:19:55,690 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 16:19:55,705 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-66/test_load_json_file_safe_missi0/missing.json
2025-08-17 16:19:55,707 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-66/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 16:19:55,708 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-66/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 16:19:55,805 [INFO] Registered new session 5378a4e2-b3f5-4b12-99b4-a24feadfbabc for user 'robbie'.
2025-08-17 16:19:55,810 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:55,836 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-66/art_processing0/processed-artwork/dummy-artwork
2025-08-17 16:19:55,933 [INFO] Registered new session 7111ce41-3820-4d3c-b6ce-ab5d4afd6362 for user 'robbie'.
2025-08-17 16:19:55,937 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:55,943 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-66/art_processing1/processed-artwork/byte-art
2025-08-17 16:19:56,039 [INFO] Registered new session 79e81913-e5b1-42dc-a868-630463d0c319 for user 'robbie'.
2025-08-17 16:19:56,043 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:56,048 [ERROR] ❌ Error running analysis: A critical analysis error
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: A critical analysis error
2025-08-17 16:19:56,145 [INFO] Registered new session 69d758ce-5f94-4ca4-be14-2cf9f701c669 for user 'robbie'.
2025-08-17 16:19:56,149 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:56,154 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-66/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 16:19:56,154 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-66/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 16:19:56,155 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-66/art_processing3/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 16:19:56,157 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 16:19:56,189 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-66/art_processing_test0
2025-08-17 16:19:56,190 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 16:19:56,190 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-66/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 16:19:56,190 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 16:19:56,191 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-66/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-66/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 16:19:56,191 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 16:19:56,191 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-66/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-66/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 16:19:56,191 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 16:19:56,192 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-66/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-66/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 16:19:56,192 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 16:19:56,192 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-66/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 16:19:56,192 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 16:19:56,192 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 16:19:56,192 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-66/art_processing_test0
2025-08-17 16:19:56,201 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-66/test_move_and_registry0/registry.json
2025-08-17 16:19:56,201 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 16:19:56,299 [INFO] Registered new session 72dfa7ca-23ce-48f6-806e-894c50b54bc2 for user 'robbie'.
2025-08-17 16:19:56,303 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:57,003 [INFO] Sellbrite authentication succeeded
2025-08-17 16:19:58,502 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 16:19:58,502 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 16:19:58,502 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 16:19:58,503 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 16:19:58,504 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 16:19:58,504 [ERROR] Analysis script not found: no such file
2025-08-17 16:19:58,626 [INFO] Registered new session 49011d62-24f0-4cac-bc25-9736c122dd25 for user 'robbie'.
2025-08-17 16:19:58,631 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:58,740 [INFO] Registered new session 28dfd3a2-a31e-4196-be56-83b7f100b17a for user 'robbie'.
2025-08-17 16:19:58,744 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:58,840 [INFO] Registered new session 2e20e1fe-3b4f-4d0d-bf2a-60ec07eed75b for user 'robbie'.
2025-08-17 16:19:58,845 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:58,942 [INFO] Registered new session e983de37-73b2-4b6d-b2b1-f6b13545d0c1 for user 'robbie'.
2025-08-17 16:19:58,946 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:59,044 [INFO] Registered new session 42268664-5266-4e74-aabe-93618691e3c2 for user 'robbie'.
2025-08-17 16:19:59,047 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:59,143 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 16:19:59,143 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 16:19:59,148 [INFO] Removed session 49011d62-24f0-4cac-bc25-9736c122dd25 for user 'robbie'.
2025-08-17 16:19:59,149 [INFO] User 'robbie' logged out and session '49011d62-24f0-4cac-bc25-9736c122dd25' was removed.
2025-08-17 16:19:59,243 [INFO] Registered new session baeb1e66-2676-4d0e-988d-ee90eba6d41c for user 'robbie'.
2025-08-17 16:19:59,246 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 16:19:59,253 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 16:19:59,254 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 16:19:59,255 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 16:19:59,258 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 16:19:59,385 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-66/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0081-by-robin-custance-rjc-rjc-0081
2025-08-17 16:19:59,385 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 16:19:59,390 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-66/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0082-by-robin-custance-rjc-rjc-0082
2025-08-17 16:19:59,390 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 16:19:59,391 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 16:19:59,392 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 16:19:59,395 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-66/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0085-by-robin-custance-rjc-rjc-0085
2025-08-17 16:19:59,489 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 16:19:59,489 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 16:19:59,496 [INFO] Assigned new SKU: RJC-0480. Tracker file updated.
2025-08-17 17:13:06,581 [INFO] HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"
2025-08-17 17:13:06,582 [INFO] ✅ OpenAI API Key       Connection successful. Key is valid.
2025-08-17 17:13:07,026 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 17:13:07,494 [INFO] HTTP Request: GET https://api.openai.com/v1/models/gpt-4o "HTTP/1.1 200 OK"
2025-08-17 17:13:08,632 [INFO] ✅ Google Gemini        Connection successful. Key is valid and has access to gemini-1.5-pro-latest.
2025-08-17 17:13:09,260 [INFO] ✅ Sellbrite            Connection successful. 
2025-08-17 17:13:09,294 [INFO] Users table is empty. Creating default admin user.
2025-08-17 17:13:09,405 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 17:13:09,546 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 17:13:09,549 [INFO] Removed session 5378a4e2-b3f5-4b12-99b4-a24feadfbabc for user 'robbie'.
2025-08-17 17:13:09,549 [INFO] Removed session 7111ce41-3820-4d3c-b6ce-ab5d4afd6362 for user 'robbie'.
2025-08-17 17:13:09,550 [INFO] Removed session 79e81913-e5b1-42dc-a868-630463d0c319 for user 'robbie'.
2025-08-17 17:13:09,550 [INFO] Removed session 69d758ce-5f94-4ca4-be14-2cf9f701c669 for user 'robbie'.
2025-08-17 17:13:09,551 [INFO] Removed session 72dfa7ca-23ce-48f6-806e-894c50b54bc2 for user 'robbie'.
2025-08-17 17:13:09,660 [INFO] No site settings found in database; creating new default record.
2025-08-17 17:13:09,666 [INFO] Registered new session 978079d3-b67b-4047-9a96-a9cfd2efa59d for user 'viewer'.
2025-08-17 17:13:09,671 [INFO] Successful login for user 'viewer' with role 'viewer'.
2025-08-17 17:13:09,674 [WARNING] Role-based access denied for user 'viewer' (role: 'viewer') to endpoint 'admin.dashboard'. Required role: 'admin'.
2025-08-17 17:13:09,676 [INFO] Removed session 978079d3-b67b-4047-9a96-a9cfd2efa59d for user 'viewer'.
2025-08-17 17:13:09,676 [INFO] User 'viewer' logged out and session '978079d3-b67b-4047-9a96-a9cfd2efa59d' was removed.
2025-08-17 17:13:09,784 [INFO] Registered new session 33dec7a1-509a-4927-aa83-2e551b2d8e84 for user 'robbie'.
2025-08-17 17:13:09,788 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:09,831 [INFO] Users table is empty. Creating default admin user.
2025-08-17 17:13:09,975 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 17:13:10,004 [INFO] Removed session 33dec7a1-509a-4927-aa83-2e551b2d8e84 for user 'robbie'.
2025-08-17 17:13:10,124 [INFO] No site settings found in database; creating new default record.
2025-08-17 17:13:10,130 [INFO] Registered new session 9e53261a-094a-4258-9326-d74b71a2576e for user 'robbie'.
2025-08-17 17:13:10,135 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:10,140 [WARNING] ADMIN ACTION: Force 'no-cache' has been enabled for 1 minutes.
2025-08-17 17:13:10,184 [INFO] Users table is empty. Creating default admin user.
2025-08-17 17:13:10,292 [INFO] Default admin user 'robbie' created successfully.
2025-08-17 17:13:10,427 [INFO] Successfully added new user 'viewer' with role 'viewer'.
2025-08-17 17:13:10,428 [INFO] Removed session 9e53261a-094a-4258-9326-d74b71a2576e for user 'robbie'.
2025-08-17 17:13:10,535 [INFO] No site settings found in database; creating new default record.
2025-08-17 17:13:10,543 [INFO] Registered new session 4244bfc7-096e-4fd0-b1be-c687596a3c58 for user 'robbie'.
2025-08-17 17:13:10,547 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:10,553 [WARNING] ADMIN ACTION: Login requirement has been disabled for 1 minutes.
2025-08-17 17:13:10,555 [INFO] Removed session 4244bfc7-096e-4fd0-b1be-c687596a3c58 for user 'robbie'.
2025-08-17 17:13:10,555 [INFO] User 'robbie' logged out and session '4244bfc7-096e-4fd0-b1be-c687596a3c58' was removed.
2025-08-17 17:13:10,664 [WARNING] Login attempt by 'viewer' failed: Site is locked by admin.
2025-08-17 17:13:10,680 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-67/test_load_json_file_safe_missi0/missing.json
2025-08-17 17:13:10,682 [WARNING] File at /tmp/pytest-of-artnarrator/pytest-67/test_load_json_file_safe_empty0/empty.json was empty; reset to {}
2025-08-17 17:13:10,684 [ERROR] Invalid JSON in /tmp/pytest-of-artnarrator/pytest-67/test_load_json_file_safe_inval0/invalid.json, reset to {}. Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
2025-08-17 17:13:10,792 [INFO] Registered new session 5d002474-e29b-481d-a7e9-0f6ed56d7be7 for user 'robbie'.
2025-08-17 17:13:10,796 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:10,824 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-67/art_processing0/processed-artwork/dummy-artwork
2025-08-17 17:13:10,932 [INFO] Registered new session 0425634c-9242-419f-81c5-b127f167beb5 for user 'robbie'.
2025-08-17 17:13:10,936 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:10,942 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-67/art_processing1/processed-artwork/byte-art
2025-08-17 17:13:11,047 [INFO] Registered new session e761761a-7b8d-4abb-83a5-1148750b8bfa for user 'robbie'.
2025-08-17 17:13:11,051 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:11,057 [ERROR] ❌ Error running analysis: A critical analysis error
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/routes/artwork_routes.py", line 609, in analyze_artwork_by_filename
    analysis_result = _run_ai_analysis(src_path, provider)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1118, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1122, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1177, in _execute_mock_call
    raise effect
RuntimeError: A critical analysis error
2025-08-17 17:13:11,167 [INFO] Registered new session 21778a60-5edf-4b05-8370-64dff92f9ba3 for user 'robbie'.
2025-08-17 17:13:11,171 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:11,176 [INFO] [DEBUG] _run_ai_analysis: img_path=/tmp/pytest-of-artnarrator/pytest-67/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg provider=openai
2025-08-17 17:13:11,176 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py /tmp/pytest-of-artnarrator/pytest-67/art_processing3/unanalysed-artwork/cassowary-test-01/cassowary-test-01.jpg --json-output
2025-08-17 17:13:11,177 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-67/art_processing3/processed-artwork/mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK
2025-08-17 17:13:11,180 [WARNING] Generic text for  not found at /home/artnarrator/artnarrator.com/generic_texts/.txt
2025-08-17 17:13:11,212 [INFO] Created temporary test structure at: /tmp/pytest-of-artnarrator/pytest-67/art_processing_test0
2025-08-17 17:13:11,212 [INFO] --- STAGE 1: UPLOAD ---
2025-08-17 17:13:11,212 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'upload': {'path': '/tmp/pytest-of-artnarrator/pytest-67/art_processing_test0/unanalysed-artwork/eucalypt-woodland-original/eucalypt-woodland-open-dry-forest.jpg', 'folder': 'eucalypt-woodland-original', 'filename': 'eucalypt-woodland-open-dry-forest.jpg'}
2025-08-17 17:13:11,213 [INFO] --- STAGE 2: ANALYSE ---
2025-08-17 17:13:11,213 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'analyse': {'path': '/tmp/pytest-of-artnarrator/pytest-67/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-67/art_processing_test0/processed-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 17:13:11,213 [INFO] --- STAGE 3: FINALISED ---
2025-08-17 17:13:11,214 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'finalised': {'path': '/tmp/pytest-of-artnarrator/pytest-67/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-67/art_processing_test0/finalised-artwork/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 17:13:11,214 [INFO] --- STAGE 4: LOCKED ---
2025-08-17 17:13:11,214 [INFO] STATE UPDATE for 'eucalypt-woodland-original' at stage 'locked': {'path': '/tmp/pytest-of-artnarrator/pytest-67/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'folder': 'LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278', 'filename': 'moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg', 'json_path': '/tmp/pytest-of-artnarrator/pytest-67/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278-listing.json'}
2025-08-17 17:13:11,214 [INFO] --- STAGE 5: PUBLIC URL VERIFICATION ---
2025-08-17 17:13:11,214 [INFO] Final file path: /tmp/pytest-of-artnarrator/pytest-67/art_processing_test0/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 17:13:11,214 [INFO] Generated public URL: https://artnarrator.com/art-processing/artwork-vault/LOCKED-moon-over-fire-country-dot-art-by-robin-custance-RJC-0278/moon-over-fire-country-dot-art-by-robin-custance-RJC-0278.jpg
2025-08-17 17:13:11,214 [INFO] ✅ Full artwork lifecycle test completed successfully!
2025-08-17 17:13:11,215 [INFO] Cleaning up temporary test structure at: /tmp/pytest-of-artnarrator/pytest-67/art_processing_test0
2025-08-17 17:13:11,224 [WARNING] Created new empty JSON file at /tmp/pytest-of-artnarrator/pytest-67/test_move_and_registry0/registry.json
2025-08-17 17:13:11,224 [INFO] Registered new artwork test_uid_123 in legacy registry
2025-08-17 17:13:11,334 [INFO] Registered new session f4d9c801-a8e2-43eb-b742-8fdbe96fc8dd for user 'robbie'.
2025-08-17 17:13:11,339 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:12,052 [INFO] Sellbrite authentication succeeded
2025-08-17 17:13:13,594 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 17:13:13,594 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 17:13:13,594 [ERROR] AI analysis timed out: Command '['/home/artnarrator/artnarrator.com/venv/bin/python3', '/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py', 'img.jpg', '--json-output']' timed out after 600 seconds
2025-08-17 17:13:13,595 [INFO] [DEBUG] _run_ai_analysis: img_path=img.jpg provider=openai
2025-08-17 17:13:13,595 [INFO] [DEBUG] Subprocess cmd: /home/artnarrator/artnarrator.com/venv/bin/python3 /home/artnarrator/artnarrator.com/scripts/analyze_artwork.py img.jpg --json-output
2025-08-17 17:13:13,595 [ERROR] Analysis script not found: no such file
2025-08-17 17:13:13,734 [INFO] Registered new session 7a2910c9-3bf1-4f4c-a169-061ff1590ddf for user 'robbie'.
2025-08-17 17:13:13,738 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:13,859 [INFO] Registered new session cc330803-9436-44ff-bd43-b88791dd468a for user 'robbie'.
2025-08-17 17:13:13,863 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:13,968 [INFO] Registered new session 1878a292-e42f-4e95-8122-7cc1a73addef for user 'robbie'.
2025-08-17 17:13:13,971 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:14,079 [INFO] Registered new session 8ef2debf-5028-47d0-b20f-c30dbf30a02e for user 'robbie'.
2025-08-17 17:13:14,082 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:14,193 [INFO] Registered new session e325a960-fb48-4c72-818c-6aa50ef9543a for user 'robbie'.
2025-08-17 17:13:14,196 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:14,301 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 17:13:14,301 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 17:13:14,306 [INFO] Removed session 7a2910c9-3bf1-4f4c-a169-061ff1590ddf for user 'robbie'.
2025-08-17 17:13:14,307 [INFO] User 'robbie' logged out and session '7a2910c9-3bf1-4f4c-a169-061ff1590ddf' was removed.
2025-08-17 17:13:14,416 [INFO] Registered new session 50c7d6de-d437-4106-b473-ccbb90a75db7 for user 'robbie'.
2025-08-17 17:13:14,419 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 17:13:14,427 [INFO] Assigned new SKU: RJC-0011. Tracker file updated.
2025-08-17 17:13:14,427 [INFO] Assigned new SKU: RJC-0012. Tracker file updated.
2025-08-17 17:13:14,429 [INFO] Assigned new SKU: RJC-0006. Tracker file updated.
2025-08-17 17:13:14,432 [INFO] Assigned new SKU: RJC-0081. Tracker file updated.
2025-08-17 17:13:14,577 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-67/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0081-by-robin-custance-rjc-rjc-0081
2025-08-17 17:13:14,578 [INFO] Assigned new SKU: RJC-0082. Tracker file updated.
2025-08-17 17:13:14,582 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-67/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0082-by-robin-custance-rjc-rjc-0082
2025-08-17 17:13:14,583 [INFO] Assigned new SKU: RJC-0083. Tracker file updated.
2025-08-17 17:13:14,584 [INFO] Assigned new SKU: RJC-0084. Tracker file updated.
2025-08-17 17:13:14,584 [INFO] Assigned new SKU: RJC-0085. Tracker file updated.
2025-08-17 17:13:14,588 [INFO] Queued mockup generation for: /tmp/pytest-of-artnarrator/pytest-67/test_sequential_sku_assignment0/processed-artwork/artwork-rjc-0085-by-robin-custance-rjc-rjc-0085
2025-08-17 17:13:14,694 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 17:13:14,694 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 17:13:14,701 [INFO] Assigned new SKU: RJC-0481. Tracker file updated.
2025-08-17 17:14:16,244 [WARNING] Attempted to touch an invalid or expired session '8baf8f74-9d27-414b-81ab-ccfc0ae2d159' for user 'robbie'.
2025-08-17 17:14:45,046 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 17:14:45,046 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:02:55,015 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 18:02:55,015 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:05:07,213 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 18:05:07,213 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:05:33,018 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 18:05:33,019 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:12:35,071 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 18:12:35,071 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:12:38,693 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 18:12:38,693 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:12:58,319 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 18:12:58,319 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:13:04,091 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 18:13:04,091 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:19:57,113 [WARNING] Session registration denied for 'robbie': limit of 5 reached.
2025-08-17 18:19:57,114 [WARNING] Login attempt by 'robbie' failed: Maximum session limit reached.
2025-08-17 18:25:14,641 [INFO] Registered new session ecda5a5e-4c9e-411a-bb22-92cfa2bba452 for user 'robbie'.
2025-08-17 18:25:14,648 [INFO] Successful login for user 'robbie' with role 'admin'.
2025-08-17 18:25:15,821 [ERROR] Page not found (404): http://artnarrator.com/favicon.ico
2025-08-17 18:25:45,729 [INFO] Assigned new SKU: RJC-0482. Tracker file updated.
2025-08-17 18:25:47,885 [INFO] VIPS: selected loader is image source
2025-08-17 18:25:47,885 [INFO] VIPS: input size is 11520 x 14400
2025-08-17 18:25:47,885 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-17 18:25:47,886 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-17 18:25:47,886 [INFO] VIPS: converting to processing space srgb
2025-08-17 18:25:47,886 [INFO] VIPS: residual reducev by 0.263889
2025-08-17 18:25:47,886 [INFO] VIPS: reducev: 23 point mask
2025-08-17 18:25:47,888 [INFO] VIPS: reducev: using vector path
2025-08-17 18:25:47,888 [INFO] VIPS: reducev sequential line cache
2025-08-17 18:25:47,888 [INFO] VIPS: residual reduceh by 0.263889
2025-08-17 18:25:47,888 [INFO] VIPS: reduceh: 23 point mask
2025-08-17 18:25:47,888 [INFO] VIPS: converting to output space srgb
2025-08-17 18:25:59,300 [INFO] Initiating deletion for artwork: 'artwork-rjc-0482-by-robin-custance-rjc-rjc-0482'
2025-08-17 18:25:59,308 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0482-by-robin-custance-rjc-rjc-0482
2025-08-17 18:25:59,308 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0482-by-robin-custance-rjc-rjc-0482'
2025-08-17 18:26:03,101 [INFO] Initiating deletion for artwork: 'artwork-rjc-0445-by-robin-custance-rjc-rjc-0445'
2025-08-17 18:26:03,102 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0445-by-robin-custance-rjc-rjc-0445
2025-08-17 18:26:03,102 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0445-by-robin-custance-rjc-rjc-0445'
2025-08-17 18:26:06,455 [INFO] Initiating deletion for artwork: 'artwork-rjc-0447-by-robin-custance-rjc-rjc-0447'
2025-08-17 18:26:06,455 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0447-by-robin-custance-rjc-rjc-0447
2025-08-17 18:26:06,455 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0447-by-robin-custance-rjc-rjc-0447'
2025-08-17 18:26:09,446 [INFO] Initiating deletion for artwork: 'artwork-rjc-0450-by-robin-custance-rjc-rjc-0450'
2025-08-17 18:26:09,447 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0450-by-robin-custance-rjc-rjc-0450
2025-08-17 18:26:09,447 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0450-by-robin-custance-rjc-rjc-0450'
2025-08-17 18:26:12,075 [INFO] Initiating deletion for artwork: 'artwork-rjc-0449-by-robin-custance-rjc-rjc-0449'
2025-08-17 18:26:12,076 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0449-by-robin-custance-rjc-rjc-0449
2025-08-17 18:26:12,077 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0449-by-robin-custance-rjc-rjc-0449'
2025-08-17 18:26:15,476 [INFO] Initiating deletion for artwork: 'artwork-rjc-0452-by-robin-custance-rjc-rjc-0452'
2025-08-17 18:26:15,476 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0452-by-robin-custance-rjc-rjc-0452
2025-08-17 18:26:15,476 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0452-by-robin-custance-rjc-rjc-0452'
2025-08-17 18:26:18,896 [INFO] Initiating deletion for artwork: 'artwork-rjc-0454-by-robin-custance-rjc-rjc-0454'
2025-08-17 18:26:18,897 [INFO] Successfully deleted directory: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0454-by-robin-custance-rjc-rjc-0454
2025-08-17 18:26:18,897 [INFO] Successfully completed deletion for artwork: 'artwork-rjc-0454-by-robin-custance-rjc-rjc-0454'
2025-08-17 18:26:56,349 [INFO] Assigned new SKU: RJC-0483. Tracker file updated.
2025-08-17 18:26:58,442 [INFO] VIPS: selected loader is image source
2025-08-17 18:26:58,442 [INFO] VIPS: input size is 11520 x 14400
2025-08-17 18:26:58,442 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-17 18:26:58,443 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-17 18:26:58,443 [INFO] VIPS: converting to processing space srgb
2025-08-17 18:26:58,443 [INFO] VIPS: residual reducev by 0.263889
2025-08-17 18:26:58,443 [INFO] VIPS: reducev: 23 point mask
2025-08-17 18:26:58,445 [INFO] VIPS: reducev: using vector path
2025-08-17 18:26:58,445 [INFO] VIPS: reducev sequential line cache
2025-08-17 18:26:58,445 [INFO] VIPS: residual reduceh by 0.263889
2025-08-17 18:26:58,445 [INFO] VIPS: reduceh: 23 point mask
2025-08-17 18:26:58,446 [INFO] VIPS: converting to output space srgb
2025-08-17 18:47:22,919 [INFO] Assigned new SKU: RJC-00484. Tracker file updated.
2025-08-17 18:47:25,484 [INFO] VIPS: selected loader is image source
2025-08-17 18:47:25,485 [INFO] VIPS: input size is 11520 x 14400
2025-08-17 18:47:25,485 [INFO] VIPS: loading with factor 1 pre-shrink
2025-08-17 18:47:25,485 [INFO] VIPS: pre-shrunk size is 11520 x 14400
2025-08-17 18:47:25,485 [INFO] VIPS: converting to processing space srgb
2025-08-17 18:47:25,485 [INFO] VIPS: residual reducev by 0.263889
2025-08-17 18:47:25,485 [INFO] VIPS: reducev: 23 point mask
2025-08-17 18:47:25,487 [INFO] VIPS: reducev: using vector path
2025-08-17 18:47:25,487 [INFO] VIPS: reducev sequential line cache
2025-08-17 18:47:25,488 [INFO] VIPS: residual reduceh by 0.263889
2025-08-17 18:47:25,488 [INFO] VIPS: reduceh: 23 point mask
2025-08-17 18:47:25,488 [INFO] VIPS: converting to output space srgb
```


---
## project-toolkit-2025-08-17_18-24-45.log
---
**Path:** `logs/project-toolkit-2025-08-17_18-24-45.log`
**Updated:** `2025-08-17 18:46:43.389647701 +0930`
```
[1;36m[INFO](B[m Project Toolkit Initialised – Launching Main Menu...
[1;36m[INFO](B[m Attempting to clear all active user sessions...
[1;33m[WARN](B[m This will immediately log out ALL users from the application. This is useful if you are locked out due to the session limit.
[1;32m[SUCCESS](B[m Session registry file has been deleted. All users have been logged out.
[1;33m[WARN](B[m Invalid option ''
[1;36m[INFO](B[m Generating all audit files: Code Stack, Folder Tree, and Log Snapshot...
[1;36m[INFO](B[m Generating folder tree...
[1;32m[SUCCESS](B[m Log snapshot saved to: code-stacks/log-snapshots/log-stack-Sun-17-August-2025-06-30-PM.md
[1;32m[SUCCESS](B[m All audit files have been generated.
[1;36m[INFO](B[m Restarting all services...
[1;36m[INFO](B[m Restarting 'artnarrator' service...
[1;32m[SUCCESS](B[m Service 'restart' command issued successfully.
[1;32m[SUCCESS](B[m All services have been issued a restart command.
```


---
## 2025-08-17_08.log
---
**Path:** `logs/upload/2025-08-17_08.log`
**Updated:** `2025-08-17 18:27:00.506572388 +0930`
```
2025-08-17 08:55:50 | user: robbie | action: upload | file: great-barrier-reef-coral-patterns-generate-an-aboriginal-dot-painting-of-the-great-barrier-reef-focu-2.jpg | status: success | detail: uploaded
2025-08-17 08:57:00 | user: robbie | action: upload | file: tawny-frogmouth-generate-an-aboriginal-dot-painting-of-a-tawny-frogmouth-podargus-strigoides-perched-2.jpg | status: success | detail: uploaded
```


---
## 2025-08-17_09.log
---
**Path:** `logs/upload/2025-08-17_09.log`
**Updated:** `2025-08-17 18:47:27.312732466 +0930`
```
2025-08-17 09:17:25 | user: robbie | action: upload | file: RJC-00484 | status: success | detail: Generated thumbnail: RJC-00484-thumb.jpg
2025-08-17 09:17:27 | user: robbie | action: upload | file: forest-reflection-fire-beneath-water-blue-trees-mirrored-in-glowing-floodwaters-fire-sky-above-spiri-1.jpg | status: success | detail: uploaded
```


---
## project-toolkit-2025-08-17_18-13-38.log
---
**Path:** `logs/project-toolkit-2025-08-17_18-13-38.log`
**Updated:** `2025-08-17 18:13:53.311289373 +0930`
```
[1;36m[INFO](B[m Project Toolkit Initialised – Launching Main Menu...
[1;36m[INFO](B[m Restarting all services...
[1;36m[INFO](B[m Restarting 'artnarrator' service...
[1;32m[SUCCESS](B[m Service 'restart' command issued successfully.
[1;32m[SUCCESS](B[m All services have been issued a restart command.
```


---
## gunicorn-error.log
---
**Path:** `logs/gunicorn-error.log`
**Updated:** `2025-08-17 18:46:43.525657254 +0930`
```
[2025-08-16 13:44:52 +0930] [432822] [INFO] Starting gunicorn 23.0.0
[2025-08-16 13:44:52 +0930] [432822] [INFO] Listening at: http://127.0.0.1:8000 (432822)
[2025-08-16 13:44:52 +0930] [432822] [INFO] Using worker: sync
[2025-08-16 13:44:52 +0930] [432825] [INFO] Booting worker with pid: 432825
[2025-08-16 13:44:52 +0930] [432826] [INFO] Booting worker with pid: 432826
[2025-08-16 13:44:52 +0930] [432827] [INFO] Booting worker with pid: 432827
[2025-08-16 13:45:12 +0930] [432822] [INFO] Handling signal: term
[2025-08-16 13:45:12 +0930] [432825] [INFO] Worker exiting (pid: 432825)
[2025-08-16 13:45:12 +0930] [432826] [INFO] Worker exiting (pid: 432826)
[2025-08-16 13:45:12 +0930] [432827] [INFO] Worker exiting (pid: 432827)
[2025-08-16 13:45:14 +0930] [432822] [INFO] Shutting down: Master
[2025-08-16 13:45:14 +0930] [432926] [INFO] Starting gunicorn 23.0.0
[2025-08-16 13:45:14 +0930] [432926] [INFO] Listening at: http://127.0.0.1:8000 (432926)
[2025-08-16 13:45:14 +0930] [432926] [INFO] Using worker: sync
[2025-08-16 13:45:14 +0930] [432930] [INFO] Booting worker with pid: 432930
[2025-08-16 13:45:14 +0930] [432931] [INFO] Booting worker with pid: 432931
[2025-08-16 13:45:14 +0930] [432932] [INFO] Booting worker with pid: 432932
[2025-08-16 13:48:52 +0930] [433329] [INFO] Starting gunicorn 23.0.0
[2025-08-16 13:48:52 +0930] [433329] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:48:52 +0930] [433329] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:48:53 +0930] [433329] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:48:53 +0930] [433329] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:48:54 +0930] [433329] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:48:54 +0930] [433329] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:48:55 +0930] [433329] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:48:55 +0930] [433329] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:48:56 +0930] [433329] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:48:56 +0930] [433329] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:48:57 +0930] [433329] [ERROR] Can't connect to ('127.0.0.1', 8000)
[2025-08-16 13:49:03 +0930] [433388] [DEBUG] Current configuration:
  config: /home/artnarrator/artnarrator.com/gunicorn.conf.py
  wsgi_app: None
  bind: ['127.0.0.1:8000']
  backlog: 2048
  workers: 3
  worker_class: sync
  threads: 1
  worker_connections: 1000
  max_requests: 0
  max_requests_jitter: 0
  timeout: 120
  graceful_timeout: 30
  keepalive: 2
  limit_request_line: 4094
  limit_request_fields: 100
  limit_request_field_size: 8190
  reload: False
  reload_engine: auto
  reload_extra_files: []
  spew: False
  check_config: False
  print_config: False
  preload_app: False
  sendfile: None
  reuse_port: False
  chdir: /home/artnarrator/artnarrator.com
  daemon: False
  raw_env: []
  pidfile: None
  worker_tmp_dir: None
  user: 1004
  group: 1004
  umask: 0
  initgroups: False
  tmp_upload_dir: None
  secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
  forwarded_allow_ips: ['127.0.0.1', '::1']
  accesslog: logs/gunicorn-access.log
  disable_redirect_access_to_syslog: False
  access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
  errorlog: logs/gunicorn-error.log
  loglevel: debug
  capture_output: False
  logger_class: gunicorn.glogging.Logger
  logconfig: None
  logconfig_dict: {}
  logconfig_json: None
  syslog_addr: udp://localhost:514
  syslog: False
  syslog_prefix: None
  syslog_facility: user
  enable_stdio_inheritance: False
  statsd_host: None
  dogstatsd_tags: 
  statsd_prefix: 
  proc_name: artnarrator
  default_proc_name: app:create_app
  pythonpath: None
  paste: None
  on_starting: <function OnStarting.on_starting at 0x7f70ad503d80>
  on_reload: <function OnReload.on_reload at 0x7f70ad503ec0>
  when_ready: <function WhenReady.when_ready at 0x7f70ad514040>
  pre_fork: <function Prefork.pre_fork at 0x7f70ad514180>
  post_fork: <function Postfork.post_fork at 0x7f70ad5142c0>
  post_worker_init: <function PostWorkerInit.post_worker_init at 0x7f70ad514400>
  worker_int: <function WorkerInt.worker_int at 0x7f70ad514540>
  worker_abort: <function WorkerAbort.worker_abort at 0x7f70ad514680>
  pre_exec: <function PreExec.pre_exec at 0x7f70ad5147c0>
  pre_request: <function PreRequest.pre_request at 0x7f70ad514900>
  post_request: <function PostRequest.post_request at 0x7f70ad5149a0>
  child_exit: <function ChildExit.child_exit at 0x7f70ad514ae0>
  worker_exit: <function WorkerExit.worker_exit at 0x7f70ad514c20>
  nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x7f70ad514d60>
  on_exit: <function OnExit.on_exit at 0x7f70ad514ea0>
  ssl_context: <function NewSSLContext.ssl_context at 0x7f70ad515080>
  proxy_protocol: False
  proxy_allow_ips: ['127.0.0.1', '::1']
  keyfile: None
  certfile: None
  ssl_version: 2
  cert_reqs: 0
  ca_certs: None
  suppress_ragged_eofs: True
  do_handshake_on_connect: False
  ciphers: None
  raw_paste_global_conf: []
  permit_obsolete_folding: False
  strip_header_spaces: False
  permit_unconventional_http_method: False
  permit_unconventional_http_version: False
  casefold_http_method: False
  forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
  header_map: drop
[2025-08-16 13:49:03 +0930] [433388] [INFO] Starting gunicorn 23.0.0
[2025-08-16 13:49:03 +0930] [433388] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:49:03 +0930] [433388] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:49:03 +0930] [433388] [DEBUG] Retrying in 1 second.
[2025-08-16 13:49:04 +0930] [433388] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:49:04 +0930] [433388] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:49:04 +0930] [433388] [DEBUG] Retrying in 1 second.
[2025-08-16 13:49:05 +0930] [433388] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:49:05 +0930] [433388] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:49:05 +0930] [433388] [DEBUG] Retrying in 1 second.
[2025-08-16 13:49:06 +0930] [433388] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:49:06 +0930] [433388] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:49:06 +0930] [433388] [DEBUG] Retrying in 1 second.
[2025-08-16 13:49:07 +0930] [433388] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:49:07 +0930] [433388] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:49:07 +0930] [433388] [DEBUG] Retrying in 1 second.
[2025-08-16 13:49:08 +0930] [433388] [ERROR] Can't connect to ('127.0.0.1', 8000)
[2025-08-16 13:49:20 +0930] [434127] [DEBUG] Current configuration:
  config: /home/artnarrator/artnarrator.com/gunicorn.conf.py
  wsgi_app: None
  bind: ['127.0.0.1:8001']
  backlog: 2048
  workers: 1
  worker_class: sync
  threads: 1
  worker_connections: 1000
  max_requests: 0
  max_requests_jitter: 0
  timeout: 120
  graceful_timeout: 30
  keepalive: 2
  limit_request_line: 4094
  limit_request_fields: 100
  limit_request_field_size: 8190
  reload: False
  reload_engine: auto
  reload_extra_files: []
  spew: False
  check_config: False
  print_config: False
  preload_app: True
  sendfile: None
  reuse_port: False
  chdir: /home/artnarrator/artnarrator.com
  daemon: False
  raw_env: []
  pidfile: None
  worker_tmp_dir: None
  user: 1004
  group: 1004
  umask: 0
  initgroups: False
  tmp_upload_dir: None
  secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
  forwarded_allow_ips: ['127.0.0.1', '::1']
  accesslog: logs/gunicorn-access.log
  disable_redirect_access_to_syslog: False
  access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
  errorlog: logs/gunicorn-error.log
  loglevel: debug
  capture_output: False
  logger_class: gunicorn.glogging.Logger
  logconfig: None
  logconfig_dict: {}
  logconfig_json: None
  syslog_addr: udp://localhost:514
  syslog: False
  syslog_prefix: None
  syslog_facility: user
  enable_stdio_inheritance: False
  statsd_host: None
  dogstatsd_tags: 
  statsd_prefix: 
  proc_name: artnarrator
  default_proc_name: app:create_app
  pythonpath: None
  paste: None
  on_starting: <function OnStarting.on_starting at 0x7f47db37bd80>
  on_reload: <function OnReload.on_reload at 0x7f47db37bec0>
  when_ready: <function WhenReady.when_ready at 0x7f47db38c040>
  pre_fork: <function Prefork.pre_fork at 0x7f47db38c180>
  post_fork: <function Postfork.post_fork at 0x7f47db38c2c0>
  post_worker_init: <function PostWorkerInit.post_worker_init at 0x7f47db38c400>
  worker_int: <function WorkerInt.worker_int at 0x7f47db38c540>
  worker_abort: <function WorkerAbort.worker_abort at 0x7f47db38c680>
  pre_exec: <function PreExec.pre_exec at 0x7f47db38c7c0>
  pre_request: <function PreRequest.pre_request at 0x7f47db38c900>
  post_request: <function PostRequest.post_request at 0x7f47db38c9a0>
  child_exit: <function ChildExit.child_exit at 0x7f47db38cae0>
  worker_exit: <function WorkerExit.worker_exit at 0x7f47db38cc20>
  nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x7f47db38cd60>
  on_exit: <function OnExit.on_exit at 0x7f47db38cea0>
  ssl_context: <function NewSSLContext.ssl_context at 0x7f47db38d080>
  proxy_protocol: False
  proxy_allow_ips: ['127.0.0.1', '::1']
  keyfile: None
  certfile: None
  ssl_version: 2
  cert_reqs: 0
  ca_certs: None
  suppress_ragged_eofs: True
  do_handshake_on_connect: False
  ciphers: None
  raw_paste_global_conf: []
  permit_obsolete_folding: False
  strip_header_spaces: False
  permit_unconventional_http_method: False
  permit_unconventional_http_version: False
  casefold_http_method: False
  forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
  header_map: drop
[2025-08-16 13:49:23 +0930] [434127] [INFO] Starting gunicorn 23.0.0
[2025-08-16 13:49:23 +0930] [434127] [DEBUG] Arbiter booted
[2025-08-16 13:49:23 +0930] [434127] [INFO] Listening at: http://127.0.0.1:8001 (434127)
[2025-08-16 13:49:23 +0930] [434127] [INFO] Using worker: sync
[2025-08-16 13:49:23 +0930] [434152] [INFO] Booting worker with pid: 434152
[2025-08-16 13:49:23 +0930] [434127] [DEBUG] 1 workers
[2025-08-16 13:55:02 +0930] [434127] [INFO] Handling signal: hup
[2025-08-16 13:55:02 +0930] [434127] [INFO] Hang up: Master
[2025-08-16 13:55:02 +0930] [434127] [ERROR] Worker (pid:434152) was sent SIGHUP!
[2025-08-16 13:55:02 +0930] [434127] [DEBUG] Current configuration:
  config: /home/artnarrator/artnarrator.com/gunicorn.conf.py
  wsgi_app: None
  bind: ['127.0.0.1:8001']
  backlog: 2048
  workers: 1
  worker_class: sync
  threads: 1
  worker_connections: 1000
  max_requests: 0
  max_requests_jitter: 0
  timeout: 120
  graceful_timeout: 30
  keepalive: 2
  limit_request_line: 4094
  limit_request_fields: 100
  limit_request_field_size: 8190
  reload: False
  reload_engine: auto
  reload_extra_files: []
  spew: False
  check_config: False
  print_config: False
  preload_app: True
  sendfile: None
  reuse_port: False
  chdir: /home/artnarrator/artnarrator.com
  daemon: False
  raw_env: []
  pidfile: None
  worker_tmp_dir: None
  user: 1004
  group: 1004
  umask: 0
  initgroups: False
  tmp_upload_dir: None
  secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
  forwarded_allow_ips: ['127.0.0.1', '::1']
  accesslog: logs/gunicorn-access.log
  disable_redirect_access_to_syslog: False
  access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
  errorlog: logs/gunicorn-error.log
  loglevel: debug
  capture_output: False
  logger_class: gunicorn.glogging.Logger
  logconfig: None
  logconfig_dict: {}
  logconfig_json: None
  syslog_addr: udp://localhost:514
  syslog: False
  syslog_prefix: None
  syslog_facility: user
  enable_stdio_inheritance: False
  statsd_host: None
  dogstatsd_tags: 
  statsd_prefix: 
  proc_name: artnarrator
  default_proc_name: app:create_app
  pythonpath: None
  paste: None
  on_starting: <function OnStarting.on_starting at 0x7f47db37bd80>
  on_reload: <function OnReload.on_reload at 0x7f47db37bec0>
  when_ready: <function WhenReady.when_ready at 0x7f47db38c040>
  pre_fork: <function Prefork.pre_fork at 0x7f47db38c180>
  post_fork: <function Postfork.post_fork at 0x7f47db38c2c0>
  post_worker_init: <function PostWorkerInit.post_worker_init at 0x7f47db38c400>
  worker_int: <function WorkerInt.worker_int at 0x7f47db38c540>
  worker_abort: <function WorkerAbort.worker_abort at 0x7f47db38c680>
  pre_exec: <function PreExec.pre_exec at 0x7f47db38c7c0>
  pre_request: <function PreRequest.pre_request at 0x7f47db38c900>
  post_request: <function PostRequest.post_request at 0x7f47db38c9a0>
  child_exit: <function ChildExit.child_exit at 0x7f47db38cae0>
  worker_exit: <function WorkerExit.worker_exit at 0x7f47db38cc20>
  nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x7f47db38cd60>
  on_exit: <function OnExit.on_exit at 0x7f47db38cea0>
  ssl_context: <function NewSSLContext.ssl_context at 0x7f47db38d080>
  proxy_protocol: False
  proxy_allow_ips: ['127.0.0.1', '::1']
  keyfile: None
  certfile: None
  ssl_version: 2
  cert_reqs: 0
  ca_certs: None
  suppress_ragged_eofs: True
  do_handshake_on_connect: False
  ciphers: None
  raw_paste_global_conf: []
  permit_obsolete_folding: False
  strip_header_spaces: False
  permit_unconventional_http_method: False
  permit_unconventional_http_version: False
  casefold_http_method: False
  forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
  header_map: drop
[2025-08-16 13:55:02 +0930] [434290] [INFO] Booting worker with pid: 434290
[2025-08-16 13:56:38 +0930] [435492] [INFO] Starting gunicorn 23.0.0
[2025-08-16 13:56:38 +0930] [435492] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:56:38 +0930] [435492] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:56:39 +0930] [435492] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:56:39 +0930] [435492] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:56:40 +0930] [435492] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:56:40 +0930] [435492] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:56:41 +0930] [435492] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:56:41 +0930] [435492] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:56:42 +0930] [435492] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:56:42 +0930] [435492] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:56:43 +0930] [435492] [ERROR] Can't connect to ('127.0.0.1', 8000)
[2025-08-16 13:57:00 +0930] [435603] [DEBUG] Current configuration:
  config: ./gunicorn.conf.py
  wsgi_app: None
  bind: ['127.0.0.1:8000']
  backlog: 2048
  workers: 1
  worker_class: sync
  threads: 1
  worker_connections: 1000
  max_requests: 0
  max_requests_jitter: 0
  timeout: 120
  graceful_timeout: 30
  keepalive: 2
  limit_request_line: 4094
  limit_request_fields: 100
  limit_request_field_size: 8190
  reload: False
  reload_engine: auto
  reload_extra_files: []
  spew: False
  check_config: False
  print_config: False
  preload_app: False
  sendfile: None
  reuse_port: False
  chdir: /home/artnarrator/artnarrator.com
  daemon: False
  raw_env: []
  pidfile: None
  worker_tmp_dir: None
  user: 1004
  group: 1004
  umask: 0
  initgroups: False
  tmp_upload_dir: None
  secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
  forwarded_allow_ips: ['127.0.0.1', '::1']
  accesslog: logs/gunicorn-access.log
  disable_redirect_access_to_syslog: False
  access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
  errorlog: logs/gunicorn-error.log
  loglevel: debug
  capture_output: False
  logger_class: gunicorn.glogging.Logger
  logconfig: None
  logconfig_dict: {}
  logconfig_json: None
  syslog_addr: udp://localhost:514
  syslog: False
  syslog_prefix: None
  syslog_facility: user
  enable_stdio_inheritance: False
  statsd_host: None
  dogstatsd_tags: 
  statsd_prefix: 
  proc_name: artnarrator
  default_proc_name: app:app
  pythonpath: None
  paste: None
  on_starting: <function OnStarting.on_starting at 0x7f6fc410bd80>
  on_reload: <function OnReload.on_reload at 0x7f6fc410bec0>
  when_ready: <function WhenReady.when_ready at 0x7f6fc411c040>
  pre_fork: <function Prefork.pre_fork at 0x7f6fc411c180>
  post_fork: <function Postfork.post_fork at 0x7f6fc411c2c0>
  post_worker_init: <function PostWorkerInit.post_worker_init at 0x7f6fc411c400>
  worker_int: <function WorkerInt.worker_int at 0x7f6fc411c540>
  worker_abort: <function WorkerAbort.worker_abort at 0x7f6fc411c680>
  pre_exec: <function PreExec.pre_exec at 0x7f6fc411c7c0>
  pre_request: <function PreRequest.pre_request at 0x7f6fc411c900>
  post_request: <function PostRequest.post_request at 0x7f6fc411c9a0>
  child_exit: <function ChildExit.child_exit at 0x7f6fc411cae0>
  worker_exit: <function WorkerExit.worker_exit at 0x7f6fc411cc20>
  nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x7f6fc411cd60>
  on_exit: <function OnExit.on_exit at 0x7f6fc411cea0>
  ssl_context: <function NewSSLContext.ssl_context at 0x7f6fc411d080>
  proxy_protocol: False
  proxy_allow_ips: ['127.0.0.1', '::1']
  keyfile: None
  certfile: None
  ssl_version: 2
  cert_reqs: 0
  ca_certs: None
  suppress_ragged_eofs: True
  do_handshake_on_connect: False
  ciphers: None
  raw_paste_global_conf: []
  permit_obsolete_folding: False
  strip_header_spaces: False
  permit_unconventional_http_method: False
  permit_unconventional_http_version: False
  casefold_http_method: False
  forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
  header_map: drop
[2025-08-16 13:57:00 +0930] [435603] [INFO] Starting gunicorn 23.0.0
[2025-08-16 13:57:00 +0930] [435603] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:00 +0930] [435603] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:00 +0930] [435603] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:01 +0930] [435603] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:01 +0930] [435603] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:01 +0930] [435603] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:02 +0930] [435603] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:02 +0930] [435603] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:02 +0930] [435603] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:03 +0930] [435603] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:03 +0930] [435603] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:03 +0930] [435603] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:04 +0930] [435603] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:04 +0930] [435603] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:04 +0930] [435603] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:05 +0930] [435603] [ERROR] Can't connect to ('127.0.0.1', 8000)
[2025-08-16 13:57:14 +0930] [435672] [DEBUG] Current configuration:
  config: ./gunicorn.conf.py
  wsgi_app: None
  bind: ['127.0.0.1:8000']
  backlog: 2048
  workers: 1
  worker_class: sync
  threads: 1
  worker_connections: 1000
  max_requests: 0
  max_requests_jitter: 0
  timeout: 120
  graceful_timeout: 30
  keepalive: 2
  limit_request_line: 4094
  limit_request_fields: 100
  limit_request_field_size: 8190
  reload: False
  reload_engine: auto
  reload_extra_files: []
  spew: False
  check_config: False
  print_config: False
  preload_app: True
  sendfile: None
  reuse_port: False
  chdir: /home/artnarrator/artnarrator.com
  daemon: False
  raw_env: []
  pidfile: None
  worker_tmp_dir: None
  user: 1004
  group: 1004
  umask: 0
  initgroups: False
  tmp_upload_dir: None
  secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
  forwarded_allow_ips: ['127.0.0.1', '::1']
  accesslog: logs/gunicorn-access.log
  disable_redirect_access_to_syslog: False
  access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
  errorlog: logs/gunicorn-error.log
  loglevel: debug
  capture_output: False
  logger_class: gunicorn.glogging.Logger
  logconfig: None
  logconfig_dict: {}
  logconfig_json: None
  syslog_addr: udp://localhost:514
  syslog: False
  syslog_prefix: None
  syslog_facility: user
  enable_stdio_inheritance: False
  statsd_host: None
  dogstatsd_tags: 
  statsd_prefix: 
  proc_name: artnarrator
  default_proc_name: app:app
  pythonpath: None
  paste: None
  on_starting: <function OnStarting.on_starting at 0x7f991390bd80>
  on_reload: <function OnReload.on_reload at 0x7f991390bec0>
  when_ready: <function WhenReady.when_ready at 0x7f991391c040>
  pre_fork: <function Prefork.pre_fork at 0x7f991391c180>
  post_fork: <function Postfork.post_fork at 0x7f991391c2c0>
  post_worker_init: <function PostWorkerInit.post_worker_init at 0x7f991391c400>
  worker_int: <function WorkerInt.worker_int at 0x7f991391c540>
  worker_abort: <function WorkerAbort.worker_abort at 0x7f991391c680>
  pre_exec: <function PreExec.pre_exec at 0x7f991391c7c0>
  pre_request: <function PreRequest.pre_request at 0x7f991391c900>
  post_request: <function PostRequest.post_request at 0x7f991391c9a0>
  child_exit: <function ChildExit.child_exit at 0x7f991391cae0>
  worker_exit: <function WorkerExit.worker_exit at 0x7f991391cc20>
  nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x7f991391cd60>
  on_exit: <function OnExit.on_exit at 0x7f991391cea0>
  ssl_context: <function NewSSLContext.ssl_context at 0x7f991391d080>
  proxy_protocol: False
  proxy_allow_ips: ['127.0.0.1', '::1']
  keyfile: None
  certfile: None
  ssl_version: 2
  cert_reqs: 0
  ca_certs: None
  suppress_ragged_eofs: True
  do_handshake_on_connect: False
  ciphers: None
  raw_paste_global_conf: []
  permit_obsolete_folding: False
  strip_header_spaces: False
  permit_unconventional_http_method: False
  permit_unconventional_http_version: False
  casefold_http_method: False
  forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
  header_map: drop
[2025-08-16 13:57:17 +0930] [435672] [INFO] Starting gunicorn 23.0.0
[2025-08-16 13:57:17 +0930] [435672] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:17 +0930] [435672] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:17 +0930] [435672] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:18 +0930] [435672] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:18 +0930] [435672] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:18 +0930] [435672] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:19 +0930] [435672] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:19 +0930] [435672] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:19 +0930] [435672] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:20 +0930] [435672] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:20 +0930] [435672] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:20 +0930] [435672] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:21 +0930] [435672] [ERROR] Connection in use: ('127.0.0.1', 8000)
[2025-08-16 13:57:21 +0930] [435672] [ERROR] connection to ('127.0.0.1', 8000) failed: [Errno 98] Address already in use
[2025-08-16 13:57:21 +0930] [435672] [DEBUG] Retrying in 1 second.
[2025-08-16 13:57:22 +0930] [435672] [ERROR] Can't connect to ('127.0.0.1', 8000)
[2025-08-16 14:01:28 +0930] [432926] [INFO] Handling signal: term
[2025-08-16 14:01:28 +0930] [432930] [INFO] Worker exiting (pid: 432930)
[2025-08-16 14:01:28 +0930] [432931] [INFO] Worker exiting (pid: 432931)
[2025-08-16 14:01:28 +0930] [432932] [INFO] Worker exiting (pid: 432932)
[2025-08-16 14:01:28 +0930] [432926] [ERROR] Worker (pid:432930) was sent SIGTERM!
[2025-08-16 14:01:28 +0930] [432926] [ERROR] Worker (pid:432931) was sent SIGTERM!
[2025-08-16 14:01:29 +0930] [432926] [INFO] Shutting down: Master
[2025-08-16 14:01:29 +0930] [436662] [INFO] Starting gunicorn 23.0.0
[2025-08-16 14:01:29 +0930] [436662] [INFO] Listening at: http://127.0.0.1:8000 (436662)
[2025-08-16 14:01:29 +0930] [436662] [INFO] Using worker: sync
[2025-08-16 14:01:29 +0930] [436669] [INFO] Booting worker with pid: 436669
[2025-08-16 14:01:29 +0930] [436670] [INFO] Booting worker with pid: 436670
[2025-08-16 14:01:29 +0930] [436671] [INFO] Booting worker with pid: 436671
[2025-08-16 14:02:11 +0930] [436669] [INFO] Worker exiting (pid: 436669)
[2025-08-16 14:02:11 +0930] [436662] [INFO] Handling signal: term
[2025-08-16 14:02:11 +0930] [436671] [INFO] Worker exiting (pid: 436671)
[2025-08-16 14:02:11 +0930] [436670] [INFO] Worker exiting (pid: 436670)
[2025-08-16 14:02:11 +0930] [436662] [ERROR] Worker (pid:436669) was sent SIGTERM!
[2025-08-16 14:02:12 +0930] [436662] [INFO] Shutting down: Master
[2025-08-16 14:02:12 +0930] [434290] [INFO] Worker exiting (pid: 434290)
[2025-08-16 14:02:12 +0930] [434127] [INFO] Handling signal: term
[2025-08-16 14:02:13 +0930] [434127] [INFO] Shutting down: Master
[2025-08-16 14:02:48 +0930] [436964] [INFO] Starting gunicorn 23.0.0
[2025-08-16 14:02:48 +0930] [436964] [INFO] Listening at: http://127.0.0.1:8000 (436964)
[2025-08-16 14:02:48 +0930] [436964] [INFO] Using worker: sync
[2025-08-16 14:02:48 +0930] [436969] [INFO] Booting worker with pid: 436969
[2025-08-16 14:02:48 +0930] [436970] [INFO] Booting worker with pid: 436970
[2025-08-16 14:02:48 +0930] [436971] [INFO] Booting worker with pid: 436971
[2025-08-16 14:09:49 +0930] [436964] [INFO] Handling signal: term
[2025-08-16 14:09:49 +0930] [436970] [INFO] Worker exiting (pid: 436970)
[2025-08-16 14:09:49 +0930] [436969] [INFO] Worker exiting (pid: 436969)
[2025-08-16 14:09:49 +0930] [436971] [INFO] Worker exiting (pid: 436971)
[2025-08-16 14:09:50 +0930] [436964] [INFO] Shutting down: Master
[2025-08-16 14:09:51 +0930] [438513] [INFO] Starting gunicorn 23.0.0
[2025-08-16 14:09:51 +0930] [438513] [INFO] Listening at: http://127.0.0.1:8000 (438513)
[2025-08-16 14:09:51 +0930] [438513] [INFO] Using worker: sync
[2025-08-16 14:09:51 +0930] [438515] [INFO] Booting worker with pid: 438515
[2025-08-16 14:09:51 +0930] [438516] [INFO] Booting worker with pid: 438516
[2025-08-16 14:09:52 +0930] [438517] [INFO] Booting worker with pid: 438517
[2025-08-16 14:11:36 +0930] [438513] [INFO] Handling signal: term
[2025-08-16 14:11:36 +0930] [438516] [INFO] Worker exiting (pid: 438516)
[2025-08-16 14:11:36 +0930] [438515] [INFO] Worker exiting (pid: 438515)
[2025-08-16 14:11:36 +0930] [438517] [INFO] Worker exiting (pid: 438517)
[2025-08-16 14:11:36 +0930] [438513] [ERROR] Worker (pid:438517) was sent SIGTERM!
[2025-08-16 14:11:36 +0930] [438513] [ERROR] Worker (pid:438516) was sent SIGTERM!
[2025-08-16 14:11:36 +0930] [438513] [ERROR] Worker (pid:438515) was sent SIGTERM!
[2025-08-16 14:11:37 +0930] [438513] [INFO] Shutting down: Master
[2025-08-16 14:14:46 +0930] [438984] [INFO] Starting gunicorn 23.0.0
[2025-08-16 14:14:46 +0930] [438984] [INFO] Listening at: http://127.0.0.1:8000 (438984)
[2025-08-16 14:14:46 +0930] [438984] [INFO] Using worker: sync
[2025-08-16 14:14:46 +0930] [438986] [INFO] Booting worker with pid: 438986
[2025-08-16 14:14:47 +0930] [438987] [INFO] Booting worker with pid: 438987
[2025-08-16 14:14:47 +0930] [438988] [INFO] Booting worker with pid: 438988
[2025-08-16 14:19:42 +0930] [438984] [INFO] Handling signal: term
[2025-08-16 14:19:42 +0930] [438986] [INFO] Worker exiting (pid: 438986)
[2025-08-16 14:19:42 +0930] [438987] [INFO] Worker exiting (pid: 438987)
[2025-08-16 14:19:42 +0930] [438988] [INFO] Worker exiting (pid: 438988)
[2025-08-16 14:19:43 +0930] [438984] [INFO] Shutting down: Master
[2025-08-16 14:19:44 +0930] [439967] [DEBUG] Current configuration:
  config: ./gunicorn.conf.py
  wsgi_app: None
  bind: ['127.0.0.1:8000']
  backlog: 2048
  workers: 3
  worker_class: sync
  threads: 1
  worker_connections: 1000
  max_requests: 0
  max_requests_jitter: 0
  timeout: 120
  graceful_timeout: 30
  keepalive: 2
  limit_request_line: 4094
  limit_request_fields: 100
  limit_request_field_size: 8190
  reload: False
  reload_engine: auto
  reload_extra_files: []
  spew: False
  check_config: False
  print_config: False
  preload_app: False
  sendfile: None
  reuse_port: False
  chdir: /home/artnarrator/artnarrator.com
  daemon: False
  raw_env: []
  pidfile: None
  worker_tmp_dir: None
  user: 1004
  group: 1004
  umask: 0
  initgroups: False
  tmp_upload_dir: None
  secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
  forwarded_allow_ips: ['127.0.0.1', '::1']
  accesslog: logs/gunicorn-access.log
  disable_redirect_access_to_syslog: False
  access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
  errorlog: logs/gunicorn-error.log
  loglevel: debug
  capture_output: True
  logger_class: gunicorn.glogging.Logger
  logconfig: None
  logconfig_dict: {}
  logconfig_json: None
  syslog_addr: udp://localhost:514
  syslog: False
  syslog_prefix: None
  syslog_facility: user
  enable_stdio_inheritance: False
  statsd_host: None
  dogstatsd_tags: 
  statsd_prefix: 
  proc_name: artnarrator
  default_proc_name: app:app
  pythonpath: None
  paste: None
  on_starting: <function OnStarting.on_starting at 0x7f40330bfd80>
  on_reload: <function OnReload.on_reload at 0x7f40330bfec0>
  when_ready: <function WhenReady.when_ready at 0x7f40330d0040>
  pre_fork: <function Prefork.pre_fork at 0x7f40330d0180>
  post_fork: <function Postfork.post_fork at 0x7f40330d02c0>
  post_worker_init: <function PostWorkerInit.post_worker_init at 0x7f40330d0400>
  worker_int: <function WorkerInt.worker_int at 0x7f40330d0540>
  worker_abort: <function WorkerAbort.worker_abort at 0x7f40330d0680>
  pre_exec: <function PreExec.pre_exec at 0x7f40330d07c0>
  pre_request: <function PreRequest.pre_request at 0x7f40330d0900>
  post_request: <function PostRequest.post_request at 0x7f40330d09a0>
  child_exit: <function ChildExit.child_exit at 0x7f40330d0ae0>
  worker_exit: <function WorkerExit.worker_exit at 0x7f40330d0c20>
  nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x7f40330d0d60>
  on_exit: <function OnExit.on_exit at 0x7f40330d0ea0>
  ssl_context: <function NewSSLContext.ssl_context at 0x7f40330d1080>
  proxy_protocol: False
  proxy_allow_ips: ['127.0.0.1', '::1']
  keyfile: None
  certfile: None
  ssl_version: 2
  cert_reqs: 0
  ca_certs: None
  suppress_ragged_eofs: True
  do_handshake_on_connect: False
  ciphers: None
  raw_paste_global_conf: []
  permit_obsolete_folding: False
  strip_header_spaces: False
  permit_unconventional_http_method: False
  permit_unconventional_http_version: False
  casefold_http_method: False
  forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
  header_map: drop
[2025-08-16 14:19:44 +0930] [439967] [INFO] Starting gunicorn 23.0.0
[2025-08-16 14:19:44 +0930] [439967] [DEBUG] Arbiter booted
[2025-08-16 14:19:44 +0930] [439967] [INFO] Listening at: http://127.0.0.1:8000 (439967)
[2025-08-16 14:19:44 +0930] [439967] [INFO] Using worker: sync
[2025-08-16 14:19:44 +0930] [439971] [INFO] Booting worker with pid: 439971
[2025-08-16 14:19:44 +0930] [439979] [INFO] Booting worker with pid: 439979
[2025-08-16 14:19:44 +0930] [439978] [INFO] Booting worker with pid: 439978
[2025-08-16 14:19:44 +0930] [439967] [DEBUG] 3 workers
[2025-08-16 14:23:09 +0930] [439967] [INFO] Handling signal: int
[2025-08-16 14:23:09 +0930] [439971] [INFO] Worker exiting (pid: 439971)
[2025-08-16 14:23:09 +0930] [439978] [INFO] Worker exiting (pid: 439978)
[2025-08-16 14:23:09 +0930] [439979] [INFO] Worker exiting (pid: 439979)
[2025-08-16 14:23:10 +0930] [439967] [INFO] Shutting down: Master
[2025-08-16 14:23:10 +0930] [440065] [INFO] Starting gunicorn 23.0.0
[2025-08-16 14:23:10 +0930] [440065] [INFO] Listening at: http://127.0.0.1:8000 (440065)
[2025-08-16 14:23:10 +0930] [440065] [INFO] Using worker: sync
[2025-08-16 14:23:10 +0930] [440069] [INFO] Booting worker with pid: 440069
[2025-08-16 14:23:10 +0930] [440070] [INFO] Booting worker with pid: 440070
[2025-08-16 14:23:10 +0930] [440071] [INFO] Booting worker with pid: 440071
[2025-08-17 12:57:49 +0930] [440069] [INFO] Worker exiting (pid: 440069)
[2025-08-17 12:57:49 +0930] [440065] [INFO] Handling signal: term
[2025-08-17 12:57:49 +0930] [440070] [INFO] Worker exiting (pid: 440070)
[2025-08-17 12:57:49 +0930] [440071] [INFO] Worker exiting (pid: 440071)
[2025-08-17 12:57:49 +0930] [440065] [ERROR] Worker (pid:440070) was sent SIGTERM!
[2025-08-17 12:57:50 +0930] [440065] [INFO] Shutting down: Master
[2025-08-17 12:57:50 +0930] [597150] [INFO] Starting gunicorn 23.0.0
[2025-08-17 12:57:50 +0930] [597150] [INFO] Listening at: http://127.0.0.1:8000 (597150)
[2025-08-17 12:57:50 +0930] [597150] [INFO] Using worker: sync
[2025-08-17 12:57:50 +0930] [597154] [INFO] Booting worker with pid: 597154
[2025-08-17 12:57:50 +0930] [597164] [INFO] Booting worker with pid: 597164
[2025-08-17 12:57:50 +0930] [597165] [INFO] Booting worker with pid: 597165
[2025-08-17 12:57:55 +0930] [597150] [INFO] Handling signal: term
[2025-08-17 12:57:55 +0930] [597154] [INFO] Worker exiting (pid: 597154)
[2025-08-17 12:57:55 +0930] [597164] [INFO] Worker exiting (pid: 597164)
[2025-08-17 12:57:55 +0930] [597165] [INFO] Worker exiting (pid: 597165)
[2025-08-17 12:57:55 +0930] [597150] [ERROR] Worker (pid:597164) was sent SIGTERM!
[2025-08-17 12:57:56 +0930] [597150] [INFO] Shutting down: Master
[2025-08-17 12:57:56 +0930] [597193] [INFO] Starting gunicorn 23.0.0
[2025-08-17 12:57:56 +0930] [597193] [INFO] Listening at: http://127.0.0.1:8000 (597193)
[2025-08-17 12:57:56 +0930] [597193] [INFO] Using worker: sync
[2025-08-17 12:57:56 +0930] [597196] [INFO] Booting worker with pid: 597196
[2025-08-17 12:57:56 +0930] [597197] [INFO] Booting worker with pid: 597197
[2025-08-17 12:57:56 +0930] [597207] [INFO] Booting worker with pid: 597207
[2025-08-17 15:16:29 +0930] [597193] [INFO] Handling signal: term
[2025-08-17 15:16:29 +0930] [597196] [INFO] Worker exiting (pid: 597196)
[2025-08-17 15:16:29 +0930] [597197] [INFO] Worker exiting (pid: 597197)
[2025-08-17 15:16:29 +0930] [597207] [INFO] Worker exiting (pid: 597207)
[2025-08-17 15:16:29 +0930] [597193] [ERROR] Worker (pid:597207) was sent SIGTERM!
[2025-08-17 15:16:29 +0930] [597193] [ERROR] Worker (pid:597197) was sent SIGTERM!
[2025-08-17 15:16:29 +0930] [597193] [INFO] Shutting down: Master
[2025-08-17 15:16:29 +0930] [616034] [INFO] Starting gunicorn 23.0.0
[2025-08-17 15:16:29 +0930] [616034] [INFO] Listening at: http://127.0.0.1:8000 (616034)
[2025-08-17 15:16:29 +0930] [616034] [INFO] Using worker: sync
[2025-08-17 15:16:29 +0930] [616037] [INFO] Booting worker with pid: 616037
[2025-08-17 15:16:29 +0930] [616038] [INFO] Booting worker with pid: 616038
[2025-08-17 15:16:29 +0930] [616039] [INFO] Booting worker with pid: 616039
[2025-08-17 15:48:56 +0930] [616034] [INFO] Handling signal: term
[2025-08-17 15:48:56 +0930] [616039] [INFO] Worker exiting (pid: 616039)
[2025-08-17 15:48:56 +0930] [616037] [INFO] Worker exiting (pid: 616037)
[2025-08-17 15:48:56 +0930] [616038] [INFO] Worker exiting (pid: 616038)
[2025-08-17 15:48:56 +0930] [616034] [ERROR] Worker (pid:616037) was sent SIGTERM!
[2025-08-17 15:48:56 +0930] [616034] [ERROR] Worker (pid:616039) was sent SIGTERM!
[2025-08-17 15:48:56 +0930] [616034] [INFO] Shutting down: Master
[2025-08-17 15:48:56 +0930] [620221] [INFO] Starting gunicorn 23.0.0
[2025-08-17 15:48:56 +0930] [620221] [INFO] Listening at: http://127.0.0.1:8000 (620221)
[2025-08-17 15:48:56 +0930] [620221] [INFO] Using worker: sync
[2025-08-17 15:48:56 +0930] [620225] [INFO] Booting worker with pid: 620225
[2025-08-17 15:48:57 +0930] [620226] [INFO] Booting worker with pid: 620226
[2025-08-17 15:48:57 +0930] [620227] [INFO] Booting worker with pid: 620227
[2025-08-17 15:58:51 +0930] [620221] [INFO] Handling signal: term
[2025-08-17 15:58:51 +0930] [620225] [INFO] Worker exiting (pid: 620225)
[2025-08-17 15:58:51 +0930] [620226] [INFO] Worker exiting (pid: 620226)
[2025-08-17 15:58:51 +0930] [620227] [INFO] Worker exiting (pid: 620227)
[2025-08-17 15:58:51 +0930] [620221] [ERROR] Worker (pid:620225) was sent SIGTERM!
[2025-08-17 15:58:51 +0930] [620221] [ERROR] Worker (pid:620226) was sent SIGTERM!
[2025-08-17 15:58:51 +0930] [620221] [INFO] Shutting down: Master
[2025-08-17 15:58:51 +0930] [623291] [INFO] Starting gunicorn 23.0.0
[2025-08-17 15:58:51 +0930] [623291] [INFO] Listening at: http://127.0.0.1:8000 (623291)
[2025-08-17 15:58:51 +0930] [623291] [INFO] Using worker: sync
[2025-08-17 15:58:51 +0930] [623295] [INFO] Booting worker with pid: 623295
[2025-08-17 15:58:52 +0930] [623296] [INFO] Booting worker with pid: 623296
[2025-08-17 15:58:52 +0930] [623297] [INFO] Booting worker with pid: 623297
[2025-08-17 16:14:48 +0930] [623291] [INFO] Handling signal: term
[2025-08-17 16:14:48 +0930] [623296] [INFO] Worker exiting (pid: 623296)
[2025-08-17 16:14:48 +0930] [623295] [INFO] Worker exiting (pid: 623295)
[2025-08-17 16:14:48 +0930] [623297] [INFO] Worker exiting (pid: 623297)
[2025-08-17 16:14:48 +0930] [623291] [ERROR] Worker (pid:623296) was sent SIGTERM!
[2025-08-17 16:14:48 +0930] [623291] [ERROR] Worker (pid:623295) was sent SIGTERM!
[2025-08-17 16:14:49 +0930] [623291] [INFO] Shutting down: Master
[2025-08-17 16:14:49 +0930] [625369] [INFO] Starting gunicorn 23.0.0
[2025-08-17 16:14:49 +0930] [625369] [INFO] Listening at: http://127.0.0.1:8000 (625369)
[2025-08-17 16:14:49 +0930] [625369] [INFO] Using worker: sync
[2025-08-17 16:14:49 +0930] [625373] [INFO] Booting worker with pid: 625373
[2025-08-17 16:14:49 +0930] [625374] [INFO] Booting worker with pid: 625374
[2025-08-17 16:14:49 +0930] [625375] [INFO] Booting worker with pid: 625375
[2025-08-17 17:46:25 +0930] [625369] [INFO] Handling signal: term
[2025-08-17 17:46:25 +0930] [625375] [INFO] Worker exiting (pid: 625375)
[2025-08-17 17:46:25 +0930] [625373] [INFO] Worker exiting (pid: 625373)
[2025-08-17 17:46:25 +0930] [625374] [INFO] Worker exiting (pid: 625374)
[2025-08-17 17:46:26 +0930] [625369] [INFO] Shutting down: Master
[2025-08-17 17:46:26 +0930] [640135] [INFO] Starting gunicorn 23.0.0
[2025-08-17 17:46:26 +0930] [640135] [INFO] Listening at: http://127.0.0.1:8000 (640135)
[2025-08-17 17:46:26 +0930] [640135] [INFO] Using worker: sync
[2025-08-17 17:46:26 +0930] [640149] [INFO] Booting worker with pid: 640149
[2025-08-17 17:46:26 +0930] [640150] [INFO] Booting worker with pid: 640150
[2025-08-17 17:46:26 +0930] [640151] [INFO] Booting worker with pid: 640151
[2025-08-17 18:13:52 +0930] [640135] [INFO] Handling signal: term
[2025-08-17 18:13:52 +0930] [640149] [INFO] Worker exiting (pid: 640149)
[2025-08-17 18:13:52 +0930] [640150] [INFO] Worker exiting (pid: 640150)
[2025-08-17 18:13:52 +0930] [640151] [INFO] Worker exiting (pid: 640151)
[2025-08-17 18:13:53 +0930] [640135] [INFO] Shutting down: Master
[2025-08-17 18:13:53 +0930] [643076] [INFO] Starting gunicorn 23.0.0
[2025-08-17 18:13:53 +0930] [643076] [INFO] Listening at: http://127.0.0.1:8000 (643076)
[2025-08-17 18:13:53 +0930] [643076] [INFO] Using worker: sync
[2025-08-17 18:13:53 +0930] [643095] [INFO] Booting worker with pid: 643095
[2025-08-17 18:13:53 +0930] [643096] [INFO] Booting worker with pid: 643096
[2025-08-17 18:13:53 +0930] [643097] [INFO] Booting worker with pid: 643097
[2025-08-17 18:46:42 +0930] [643076] [INFO] Handling signal: term
[2025-08-17 18:46:42 +0930] [643095] [INFO] Worker exiting (pid: 643095)
[2025-08-17 18:46:42 +0930] [643096] [INFO] Worker exiting (pid: 643096)
[2025-08-17 18:46:42 +0930] [643097] [INFO] Worker exiting (pid: 643097)
[2025-08-17 18:46:42 +0930] [643076] [ERROR] Worker (pid:643095) was sent SIGTERM!
[2025-08-17 18:46:43 +0930] [643076] [INFO] Shutting down: Master
[2025-08-17 18:46:43 +0930] [648091] [INFO] Starting gunicorn 23.0.0
[2025-08-17 18:46:43 +0930] [648091] [INFO] Listening at: http://127.0.0.1:8000 (648091)
[2025-08-17 18:46:43 +0930] [648091] [INFO] Using worker: sync
[2025-08-17 18:46:43 +0930] [648098] [INFO] Booting worker with pid: 648098
[2025-08-17 18:46:43 +0930] [648099] [INFO] Booting worker with pid: 648099
[2025-08-17 18:46:43 +0930] [648100] [INFO] Booting worker with pid: 648100
```


---
## project-toolkit-2025-08-17_18-17-23.log
---
**Path:** `logs/project-toolkit-2025-08-17_18-17-23.log`
**Updated:** `2025-08-17 18:17:37.831056910 +0930`
```
[1;36m[INFO](B[m Project Toolkit Initialised – Launching Main Menu...
[1;36m[INFO](B[m Generating all audit files: Code Stack, Folder Tree, and Log Snapshot...
[1;36m[INFO](B[m Generating folder tree...
[1;32m[SUCCESS](B[m Log snapshot saved to: code-stacks/log-snapshots/log-stack-Sun-17-August-2025-06-17-PM.md
[1;32m[SUCCESS](B[m All audit files have been generated.
```


---
## SUN-17-AUG-2025-06-13-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-13-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:13:54.983406802 +0930`
```
```


---
## SUN-17-AUG-2025-06-46-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-46-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:46:45.041763733 +0930`
```
```


---
## SUN-17-AUG-2025-06-27-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-27-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:27:00.702586153 +0930`
```
2025-08-17 18:27:00,705 - analyze_artwork_script - INFO - Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0483-by-robin-custance-rjc-rjc-0483
```


---
## SUN-17-AUG-2025-06-43-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-43-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:43:41.916902555 +0930`
```
```


---
## SUN-17-AUG-2025-06-45-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-45-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:45:53.434139272 +0930`
```
```


---
## SUN-17-AUG-2025-06-25-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-25-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:25:50.193634471 +0930`
```
2025-08-17 18:25:50,200 - analyze_artwork_script - INFO - Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-0482-by-robin-custance-rjc-rjc-0482
```


---
## SUN-17-AUG-2025-06-47-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-47-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:47:27.484744547 +0930`
```
2025-08-17 18:47:27,486 - analyze_artwork_script - INFO - Queued mockup generation for: /home/artnarrator/artnarrator.com/art-processing/processed-artwork/artwork-rjc-00484-by-robin-custance-rjc-rjc-00484
```


---
## SUN-17-AUG-2025-06-39-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-39-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:39:55.084971378 +0930`
```
```


---
## SUN-17-AUG-2025-06-51-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-51-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:51:22.517251083 +0930`
```
```


---
## SUN-17-AUG-2025-06-42-PM-ANALYZE_SCRIPT.log
---
**Path:** `logs/general-logs/SUN-17-AUG-2025-06-42-PM-ANALYZE_SCRIPT.log`
**Updated:** `2025-08-17 18:42:06.758219316 +0930`
```
```
