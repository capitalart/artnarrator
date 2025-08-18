#!/bin/bash

# ======================================================================================
# 🛡️ ArtNarrator Automated Backup Engine 🛡️
#
# Version: 1.4
# Author: Robbie (Adapted for ArtNarrator, Enhanced by Gemini)
#
# This script is designed to be run exclusively by cron for automated backups.
# It performs NO Git operations and NO server restarts. Its sole purpose is to:
# 1. Create a secure backup of the application code.
# 2. Upload the backup to a cloud remote (Google Drive).
# 3. Apply a retention policy to the cloud backups.
#
# ---
#
# Usage (for cron jobs):
#   /path/to/cron-backup.sh >> /path/to/logs/cron.log 2>&1
#
# Usage (for manual testing):
#   ./cron-backup.sh
#   ./cron-backup.sh --dry-run
#
# ======================================================================================

# === [ SECTION 1: SCRIPT SETUP & CONFIGURATION ] ======================================
set -euo pipefail

# --- Pre-computation Checks ---
# Ensure the script is run from a predictable location if paths are relative.
# For cron, it's best to use absolute paths or cd to the project root.
if [[ -d "/home/artnarrator/artnarrator.com" ]]; then
    cd /home/artnarrator/artnarrator.com
else
    echo "ERROR: Project directory /home/artnarrator/artnarrator.com not found. Exiting." >&2
    exit 1
fi

# --- Project & Backup Configuration ---
readonly PROJECT_ROOT_DIR="$(pwd)"
readonly LOG_DIR="${PROJECT_ROOT_DIR}/logs"
readonly BACKUP_DIR="${PROJECT_ROOT_DIR}/backups"

# --- Naming Conventions ---
readonly NOW=$(date '+%Y-%m-%d_%H-%M-%S')
readonly LOG_FILE="$LOG_DIR/cron-backup-${NOW}.log"
readonly BACKUP_ZIP="$BACKUP_DIR/backup_${NOW}.zip"

# --- Cloud Configuration ---
readonly GDRIVE_RCLONE_REMOTE="gdrive"
readonly GDRIVE_BACKUP_FOLDER="artnarrator-backups"
readonly CLOUD_RETENTION_COUNT=300 # Number of backups to keep in the cloud

# --- Colors for Logging ---
readonly COL_RESET='\033[0m'
readonly COL_INFO='\033[0;36m'
readonly COL_SUCCESS='\033[0;32m'
readonly COL_WARN='\033[0;33m'
readonly COL_ERROR='\033[0;31m'

# --- Flag Parsing ---
DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=true
fi

# === [ SECTION 2: LOGGING & UTILITY FUNCTIONS ] =======================================

# Consistent logging function
log() {
  local type="$1"
  local msg="$2"
  local color="$COL_INFO"
  case "$type" in
    SUCCESS) color="$COL_SUCCESS" ;;
    WARN)    color="$COL_WARN" ;;
    ERROR)   color="$COL_ERROR" ;;
  esac
  # Log to both stdout/stderr and the dedicated log file
  echo -e "$(date '+%Y-%m-%d %H:%M:%S') | ${color}${type^^}:${COL_RESET} ${msg}" | tee -a "$LOG_FILE"
}

# Function to terminate the script on critical failure
die() {
  log "ERROR" "$1"
  exit 1
}

# Wrapper to execute and log commands
run_cmd() {
  log "EXEC" "$@"
  if ! $DRY_RUN; then
    # Use eval to handle complex commands with quotes and redirects
    if ! eval "$@" >> "$LOG_FILE" 2>&1; then
        log "ERROR" "Command failed: $@"
        return 1
    fi
  fi
  return 0
}

# Check for required command-line tools
check_dependencies() {
    log "INFO" "Checking for required tools..."
    for cmd in zip rclone du; do
        if ! command -v "$cmd" &> /dev/null; then
            die "Required command '$cmd' is not installed. Aborting."
        fi
    done
    log "SUCCESS" "All required tools are present."
}

# === [ SECTION 3: SCRIPT WORKFLOW FUNCTIONS ] =========================================

# Interactively confirm backup if running in a terminal
confirm_backup_size() {
    # Only run this check in an interactive terminal and not during a dry run
    if ! [[ -t 0 && "$DRY_RUN" == false ]]; then
        return 0
    fi

    log "INFO" "Calculating estimated backup size..."

    # Define patterns for du to exclude. Note these are slightly different from zip's patterns.
    local du_exclude_patterns=(
        '.git' 'venv' 'node_modules' '__pycache__' 'backups' 'logs'
        'git-update-push-logs' 'dev-logs' 'reports' '*.DS_Store' '.env'
        'inputs' 'outputs' 'exports' 'art-uploads' 'audit' 'assets'
        'descriptions' 'gdws_content' 'mnt'
    )
    local du_excludes=()
    for pattern in "${du_exclude_patterns[@]}"; do
        du_excludes+=(--exclude="$pattern")
    done

    # Calculate and display the size
    local estimated_size
    estimated_size=$(du -sh "${du_excludes[@]}" . | awk '{print $1}')
    log "WARN" "Estimated uncompressed backup size is: ${estimated_size}B"

    # Prompt for confirmation. -r prevents backslash interpretation.
    read -p "Proceed with the actual backup? (y/N) " -n 1 -r
    echo # Move to a new line for cleaner output

    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        die "Backup cancelled by user."
    fi

    log "INFO" "User confirmed. Proceeding with backup..."
}


# Create a zip archive of the project, excluding specified directories and files
create_backup_archive() {
    log "INFO" "Creating full project backup ZIP archive..."
    local exclude_patterns=(
        '.git/*' 'venv/*' 'node_modules/*' '__pycache__/*'
        'backups/*' 'logs/*' 'git-update-push-logs/*' 'dev-logs/*'
        'reports/*' '*.DS_Store' '.env' 'inputs/*' 'outputs/*'
        'exports/*' 'art-uploads/*' 'audit/*' 'assets/*'
        'descriptions/*' 'gdws_content/*' 'mnt/*'
    )
    local zip_command="zip -r -q '$BACKUP_ZIP' ."
    for pattern in "${exclude_patterns[@]}"; do
        zip_command+=" -x '$pattern'"
    done

    if run_cmd "$zip_command"; then
        log "SUCCESS" "Backup ZIP created: $BACKUP_ZIP"
    else
        die "Failed to create backup archive. Check permissions and disk space."
    fi
}

# Upload the backup to the cloud and apply retention policy
sync_to_cloud() {
    log "INFO" "Uploading backup to Google Drive ($GDRIVE_RCLONE_REMOTE:$GDRIVE_BACKUP_FOLDER)..."
    if ! run_cmd "rclone copy '$BACKUP_ZIP' '$GDRIVE_RCLONE_REMOTE:$GDRIVE_BACKUP_FOLDER' --progress"; then
        log "ERROR" "Rclone upload failed. Check rclone configuration and network. The local backup file will be kept for now."
        return 1 # Return an error code but don't exit, so we can decide not to delete the local file
    fi
    log "SUCCESS" "Backup successfully uploaded."

    log "INFO" "Applying cloud retention policy (keeping last $CLOUD_RETENTION_COUNT backups)..."
    # Get a list of all backup files, sorted by modification time (oldest first)
    local old_backups
    old_backups=$(rclone lsf "$GDRIVE_RCLONE_REMOTE:$GDRIVE_BACKUP_FOLDER" --format "p" | sort | head -n -"$CLOUD_RETENTION_COUNT")

    if [[ -n "$old_backups" ]]; then
        log "WARN" "The following old backups will be deleted from the cloud:"
        # Use a subshell for cleaner output formatting
        (echo "$old_backups") | tee -a "$LOG_FILE"
        while IFS= read -r file; do
            run_cmd "rclone delete '$GDRIVE_RCLONE_REMOTE:$GDRIVE_BACKUP_FOLDER/$file'"
        done <<< "$old_backups"
        log "SUCCESS" "Cloud retention policy applied."
    else
        log "INFO" "Fewer than $CLOUD_RETENTION_COUNT backups in the cloud. No cleanup needed."
    fi
    return 0
}

# === [ SECTION 4: MAIN EXECUTION ] ====================================================
main() {
    # Ensure log and backup directories exist
    mkdir -p "$LOG_DIR" "$BACKUP_DIR"

    log "INFO" "=== 🛡️ ArtNarrator Automated Backup Initialized ==="
    if $DRY_RUN; then
        log "WARN" "Dry run mode is enabled. No actual changes will be made."
    fi

    check_dependencies
    confirm_backup_size
    create_backup_archive

    # Only clean up local backup if cloud sync was successful
    if sync_to_cloud; then
        log "INFO" "Cleaning up local backup file..."
        run_cmd "rm -f '$BACKUP_ZIP'"
    else
        log "WARN" "Cloud sync failed. Local backup file '$BACKUP_ZIP' has been retained."
    fi

    log "SUCCESS" "🎉 Automated backup workflow completed. 💚"
}

# Kick off the main function, redirecting all output to the log file
main
