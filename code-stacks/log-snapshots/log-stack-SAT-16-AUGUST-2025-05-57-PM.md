# 📦 LOG SNAPSHOT (Last 60 Minutes)


---
## 2025-08-16_04.log
---
**Path:** `logs/delete/2025-08-16_04.log`
**Updated:** `2025-08-16 14:25:23`
2025-08-16 04:13:14 | user: robbie | action: delete | file: RJC-00312 | status: success | detail: Deleted unanalysed artwork folder.
2025-08-16 04:41:22 | user: robbie | action: delete | file: RJC-00314 | status: success | detail: Deleted unanalysed artwork folder.
2025-08-16 04:41:26 | user: robbie | action: delete | file: RJC-00313 | status: success | detail: Deleted unanalysed artwork folder.
2025-08-16 04:55:23 | user: robbie | action: delete | file: artwork-rjc-99999-by-robin-custance-rjc-rjc-99999 | status: success | detail: Initiating delete for 'artwork-rjc-99999-by-robin-custance-rjc-rjc-99999'
2025-08-16 04:55:23 | user: robbie | action: delete | file: artwork-rjc-99999-by-robin-custance-rjc-rjc-99999 | status: success | detail: Delete process completed.


---
## 2025-08-16_05.log
---
**Path:** `logs/delete/2025-08-16_05.log`
**Updated:** `2025-08-16 15:00:23`
2025-08-16 05:29:07 | user: robbie | action: delete | file: artwork-rjc-test00-by-robin-custance-rjc-rjc-test00 | status: success | detail: Initiating delete for 'artwork-rjc-test00-by-robin-custance-rjc-rjc-test00'
2025-08-16 05:29:07 | user: robbie | action: delete | file: artwork-rjc-test00-by-robin-custance-rjc-rjc-test00 | status: success | detail: Delete process completed.
2025-08-16 05:30:23 | user: robbie | action: delete | file: RJC-00325 | status: success | detail: Deleted unanalysed artwork folder.


---
## gunicorn-access.log
---
**Path:** `logs/gunicorn-access.log`
**Updated:** `2025-08-16 17:28:27`
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


---
## project-toolkit-2025-08-16_17-57-12.log
---
**Path:** `logs/project-toolkit-2025-08-16_17-57-12.log`
**Updated:** `2025-08-16 17:57:12`
[1;36m[INFO][0m Project Toolkit Initialised – Launching Main Menu...


---
## composites-workflow.log
---
**Path:** `logs/composites-workflow.log`
**Updated:** `2025-08-16 17:35:20`
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


---
## composite_gen_4bc3bb1810f84853b7d22551c4e9341e.log
---
**Path:** `logs/composite-generation-logs/composite_gen_4bc3bb1810f84853b7d22551c4e9341e.log`
**Updated:** `2025-08-16 17:53:01`
=== STDOUT ===


=== STDERR ===
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'


---
## composite_gen_5e85f642abb44628afb4ae2ab096b4c6.log
---
**Path:** `logs/composite-generation-logs/composite_gen_5e85f642abb44628afb4ae2ab096b4c6.log`
**Updated:** `2025-08-16 17:53:40`
=== STDOUT ===


=== STDERR ===
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/generate_composites.py", line 32, in <module>
    from helpers.image_utils import make_working_copy, get_image_dimensions
ModuleNotFoundError: No module named 'helpers'


---
## 2025-08-16_04.log
---
**Path:** `logs/upload/2025-08-16_04.log`
**Updated:** `2025-08-16 14:11:02`
2025-08-16 04:13:45 | user: robbie | action: upload | file: coastal-dunes-at-sunset-generate-an-aboriginal-dot-painting-of-coastal-sand-dunes-at-sunset-showing.jpg | status: success | detail: uploaded
2025-08-16 04:41:02 | user: robbie | action: upload | file: generate-an-aboriginal-dot-painting-of-a-sulphur-crested-cockatoo-cacatua-galerita-focusing-on-its-w-2.jpg | status: success | detail: uploaded


---
## 2025-08-16_05.log
---
**Path:** `logs/upload/2025-08-16_05.log`
**Updated:** `2025-08-16 15:00:54`
2025-08-16 05:29:42 | user: robbie | action: upload | file: outback-billabong-generate-an-aboriginal-dot-painting-of-an-outback-billabong-surrounded-by-reeds-an-8.jpg | status: success | detail: uploaded
2025-08-16 05:30:54 | user: robbie | action: upload | file: coastal-dunes-at-sunset-generate-an-aboriginal-dot-painting-of-coastal-sand-dunes-at-sunset-showing.jpg | status: success | detail: uploaded


---
## gunicorn-error.log
---
**Path:** `logs/gunicorn-error.log`
**Updated:** `2025-08-16 14:23:10`
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


---
## SAT-16-AUG-2025-01-44-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-01-44-PM-ANALYZE.log`
**Updated:** `2025-08-16 13:44:54`


---
## SAT-16-AUG-2025-01-57-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-01-57-PM-ANALYZE.log`
**Updated:** `2025-08-16 13:57:15`


---
## SAT-16-AUG-2025-01-49-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-01-49-PM-ANALYZE.log`
**Updated:** `2025-08-16 13:49:21`


---
## SAT-16-AUG-2025-05-34-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-05-34-PM-ANALYZE.log`
**Updated:** `2025-08-16 17:34:46`


---
## SAT-16-AUG-2025-02-15-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-15-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:15:16`
2025-08-16 14:15:16,569 - __main__ - CRITICAL - A fatal error occurred during analysis: Unanalysed folder not found for SKU: RJC-99999
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 200, in main
    result = process_sku(str(args.input), json_output=args.json_output)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 117, in process_sku
    raise FileNotFoundError(f"Unanalysed folder not found for SKU: {sku}")
FileNotFoundError: Unanalysed folder not found for SKU: RJC-99999



---
## SAT-16-AUG-2025-01-48-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-01-48-PM-ANALYZE.log`
**Updated:** `2025-08-16 13:48:40`


---
## SAT-16-AUG-2025-05-52-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-05-52-PM-ANALYZE.log`
**Updated:** `2025-08-16 17:52:23`
2025-08-16 17:52:23,695 - __main__ - CRITICAL - A fatal error occurred during analysis: 'list' object has no attribute 'get'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 280, in main
    result = analyze_single(Path(args.input))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 113, in analyze_single
    ai_listing, raw = generate_ai_listing(image_path, aspect, sku)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 94, in generate_ai_listing
    "description": assemble_gdws_description(aspect),
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/helpers/listing_utils.py", line 323, in assemble_gdws_description
    middle_order = load_json_file_safe(order_file).get("order", []) if order_file.exists() else []
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'get'



---
## SAT-16-AUG-2025-02-01-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-01-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:01:31`


---
## SAT-16-AUG-2025-02-09-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-09-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:09:53`


---
## SAT-16-AUG-2025-02-02-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-02-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:02:50`


---
## SAT-16-AUG-2025-02-59-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-59-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:59:43`
2025-08-16 14:59:43,209 - __main__ - CRITICAL - A fatal error occurred during analysis: 'list' object has no attribute 'get'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 200, in main
    result = process_sku(str(args.input), json_output=args.json_output)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 123, in process_sku
    ai_listing, raw = generate_ai_listing(analyse, aspect, sku)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 77, in generate_ai_listing
    "description": assemble_gdws_description(aspect),
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/helpers/listing_utils.py", line 309, in assemble_gdws_description
    middle_order = load_json_file_safe(order_file).get("order", []) if order_file.exists() else []
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'get'



---
## SAT-16-AUG-2025-02-08-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-08-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:08:46`


---
## SAT-16-AUG-2025-02-05-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-05-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:05:43`


---
## SAT-16-AUG-2025-03-00-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-03-00-PM-ANALYZE.log`
**Updated:** `2025-08-16 15:00:54`
2025-08-16 15:00:54,302 - __main__ - CRITICAL - A fatal error occurred during analysis: 'list' object has no attribute 'get'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 200, in main
    result = process_sku(str(args.input), json_output=args.json_output)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 123, in process_sku
    ai_listing, raw = generate_ai_listing(analyse, aspect, sku)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 77, in generate_ai_listing
    "description": assemble_gdws_description(aspect),
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/helpers/listing_utils.py", line 309, in assemble_gdws_description
    middle_order = load_json_file_safe(order_file).get("order", []) if order_file.exists() else []
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'get'



---
## SAT-16-AUG-2025-02-28-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-28-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:28:06`


---
## SAT-16-AUG-2025-02-14-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-14-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:14:24`


---
## SAT-16-AUG-2025-02-11-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-11-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:11:03`
2025-08-16 14:11:03,253 - __main__ - CRITICAL - A fatal error occurred during analysis: 'list' object has no attribute 'get'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 200, in main
    result = process_sku(str(args.input), json_output=args.json_output)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 123, in process_sku
    ai_listing, raw = generate_ai_listing(analyse, aspect, sku)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 77, in generate_ai_listing
    "description": assemble_gdws_description(aspect),
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/helpers/listing_utils.py", line 309, in assemble_gdws_description
    middle_order = load_json_file_safe(order_file).get("order", []) if order_file.exists() else []
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'get'



---
## SAT-16-AUG-2025-05-51-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-05-51-PM-ANALYZE.log`
**Updated:** `2025-08-16 17:51:00`
2025-08-16 17:51:00,697 - __main__ - CRITICAL - A fatal error occurred during analysis: 'list' object has no attribute 'get'
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 280, in main
    result = analyze_single(Path(args.input))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 113, in analyze_single
    ai_listing, raw = generate_ai_listing(image_path, aspect, sku)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 94, in generate_ai_listing
    "description": assemble_gdws_description(aspect),
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/helpers/listing_utils.py", line 323, in assemble_gdws_description
    middle_order = load_json_file_safe(order_file).get("order", []) if order_file.exists() else []
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'get'



---
## SAT-16-AUG-2025-02-19-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-19-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:19:46`


---
## SAT-16-AUG-2025-05-35-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-05-35-PM-ANALYZE.log`
**Updated:** `2025-08-16 17:35:18`


---
## SAT-16-AUG-2025-02-23-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-23-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:23:12`


---
## SAT-16-AUG-2025-01-56-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-01-56-PM-ANALYZE.log`
**Updated:** `2025-08-16 13:56:50`


---
## SAT-16-AUG-2025-03-37-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-03-37-PM-ANALYZE.log`
**Updated:** `2025-08-16 15:37:29`


---
## SAT-16-AUG-2025-02-13-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-02-13-PM-ANALYZE.log`
**Updated:** `2025-08-16 14:13:56`
2025-08-16 14:13:56,579 - __main__ - CRITICAL - A fatal error occurred during analysis: Unanalysed folder not found for SKU: RJC-00000
Traceback (most recent call last):
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 200, in main
    result = process_sku(str(args.input), json_output=args.json_output)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/artnarrator/artnarrator.com/scripts/analyze_artwork.py", line 117, in process_sku
    raise FileNotFoundError(f"Unanalysed folder not found for SKU: {sku}")
FileNotFoundError: Unanalysed folder not found for SKU: RJC-00000



---
## SAT-16-AUG-2025-01-45-PM-ANALYZE.log
---
**Path:** `logs/general-logs/SAT-16-AUG-2025-01-45-PM-ANALYZE.log`
**Updated:** `2025-08-16 13:45:16`
