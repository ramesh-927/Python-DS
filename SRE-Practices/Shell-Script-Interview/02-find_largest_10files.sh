#!/bin/bash

# Author: Ramesh Golla
# Creation Date : 06/24/2025
# Description : 
# Date Modified: 06/25/2025

DIRECTORY="${1:-.}"  # Use provided directory or current directory (.)

# Validate directory
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: '$DIRECTORY' is not a valid directory"
    exit 1
fi

# Display header
echo "Top 10 Largest Files in $DIRECTORY:"
echo "-----------------------------------"

# Find and list the 10 largest files
find "$DIRECTORY" -type f -exec du -sh {} + | sort -rh | head -n 10

