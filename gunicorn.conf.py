# gunicorn.conf.py
# Clean and complete configuration for the ArtNarrator application

import os
from config import LOGS_DIR

# --- Server Socket ---
# The address and port to bind to. We define it here so we don't
# need it in the systemd service file.
bind = "127.0.0.1:8000"

# --- Worker Processes ---
# The number of worker processes for handling requests.
workers = 3

# --- Logging ---
# This uses the LOGS_DIR from your main config.py to ensure
# logs are correctly written to:
# /home/artnarrator/artnarrator.com/logs/
accesslog = str(LOGS_DIR / "gunicorn-access.log")
errorlog = str(LOGS_DIR / "gunicorn-error.log")
loglevel = "info"

# --- Process Naming ---
# A descriptive name to help identify the process in system monitors.
proc_name = "artnarrator"

# --- Timeout ---
# Workers silent for more than this many seconds are killed and restarted.
# Increased to 120 seconds for potentially long-running AI analysis tasks.
timeout = 120