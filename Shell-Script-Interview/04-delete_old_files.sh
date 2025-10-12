#!/bin/bash

# Author: Ramesh Golla
# Date Created: 06/25/2025
# Description:  This shell script to delete files older than a certain number of days in a specific directory
# Date Modified: 06/25/2025

TARGET_DIR="/var/logs"
DAYS_OLD=30

#Printing maessage
echo "Deleting files older than $DAYS_OLD in a $TARGET_DIR ."

find "$TARGET_DIR" -type f -mtime +$DAYS_OLD -exec rm -f {} \;

# Completion message
echo "Old files deleted successfully."
