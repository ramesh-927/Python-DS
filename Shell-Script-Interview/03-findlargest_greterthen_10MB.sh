#!/bin/bash

# Configuration
DIRECTORY="${1:-.}"  # Use provided directory or current directory (.)
MIN_SIZE="4k"       # Minimum file size (10 MB)

# Validate directory
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: '$DIRECTORY' is not a valid directory"
    exit 1
fi

# Display header
echo "Files Larger Than 10 MB in $DIRECTORY:"
echo "--------------------------------------"

# Find and list files larger than 10 MB
find "$DIRECTORY" -type f -size +"$MIN_SIZE" -exec du -sh {} + | sort -rh
