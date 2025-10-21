#!/bin/bash

# Author: Ramesh Golla
# Date Created: 07/28/2025
# Description: This script used for monitor disk space usage across multiple servers using bash script.
# Date Modified: 07/28/2025

servers=("server1" "server2" "server3")
threshold=90

for server in "${servers[@]}"; do
	usage=$(ssh $server "df -h / | tail -1 | awk '{print \$5}' | cut -d'%'-f1")
	if [ $usage -gt $threshold ]; then
		echo "Alert: $server disk usage is at $usage%"
	fi
done
