#!/bin/bash
#usage: ./myarguments.sh maddy 21

echo "Script Name: $0"
echo "first arg: $1"
echo "second arg : $2"
echo "total argument : $#"

if [$# -lt 2]; then 
	echo "usage $0 <name> and <age>"
	exit 1
fi 

echo " hello $1 you are $2 year old "
