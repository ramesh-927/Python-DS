#!/bin/bash

# Author: Ramesh Golla
# Date Created: 03/26/2025
# Description: This script is aobut creating directories and files and adding soem text in it.
# Date modified: 03/26/2025

for i in {1..5};
do
	dir_name="dir-0$i"
	mkdir -p "$dir_name"
	echo " Created directory: $dir_name"
	
	# Create  files in each directory
	for j in {1..10}; do
		file_name="$dir_name/file_$j.txt"
		echo "This is sample text in file $j of $dir_name" > "$file_name"
		echo " Created file: $file_name" 
	done
done

echo " All directories and fiels created successfully"
