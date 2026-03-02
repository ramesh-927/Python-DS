#!/bin/bash

LOG_FILE="/var/log/app.log"
MAX_SIZE=100M
BACKUP_DIR="/var/log/acrhive"

# Create a backup directory if doesn't exist.
mkdir -p $ARCHIVE_DIR

# Get the file size.
FILE_SIZE=$(du -m $LOG_FILE | cut -f1)

if [ $FILE_SIZE - gt $MAX_SIZE ]; then
    DATE=$(date +%Y%m%d%H%M)

    mv $LOG_FILE $ARCHIVE_DIR/app.log.$DATE
    gzip $ARCHIVE_DIR/app.log.$DATE
    
    touch $LOG_FILE
fi