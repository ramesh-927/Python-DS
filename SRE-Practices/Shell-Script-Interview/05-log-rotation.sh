#!/bin/bash

# Author: Ramesh Golla
# Date Created: 07/07/2025
# Description: 
# Date Modified: 07/07/2025

# Variables:
LOG_DIR="/var/log/myapp"
LOG_FILE="/var/log/myapp/log_rotation.log"

# To Ensure the log directory exists.

if [ ! -d "$LOG_DIR" ]; then
	echo "[$(date)] ERROR: log directory $LOG_DIR does not exists" >> "$LOG_FILE"
	exit 1
fi

# Compress the logs older than 7 days
find "$LOG_DIR" -type f -name "*.log"-mtype +7 -mtime -30 ! -name "*.gz" -exec gzip {}\; -exec echo "[$(data)] Compressed: {}" >> "$LOG_FILE" \;

