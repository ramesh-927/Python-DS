#!/bin/bash
# Author: Ramesh Golla
# Date Created: 03/29/2025
# Description: This script is for creting users on mac
# Date Modified: 03/29/2025

echo "Please provide a Username"
read u
echo

grep -q $u /etc/passwd
	if [ $? -eq 0 ]
	then
	echo ERROR --User $u already exist!
	echo Please choose another username
	echo
	exit 0
	fi
echo "Please provide user description?"
read d
echo
useradd "$u" -c "$d"
echo $u user accout has been created.

