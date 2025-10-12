#!/bin/bash

# Author: Ramesh Golla
# Date Created: 03/26/2025
# Description: This script is used for list of user logged in particular time.
# Date modified: 03/26/2025
#!/bin/bash

#DATE=$1
# Extract logs for the specified date
#last | awk -v date="$DATE" '$4"-"$5"-"$6 == date {print $1, $3, $4, $5, $6, $7, $8}'
echo "Please enter a day(e.g Mon)"
read d
echo
echo "Please enter a month(e.g Sep)"
read m
echo
echo "Please enter  a date(e.g 26)"
read da
echo

last | grep "$d $m $da"

