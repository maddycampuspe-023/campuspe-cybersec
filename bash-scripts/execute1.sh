#!/bin/bash

greetings(){
	local name=$1
	local upper_name="${name^^}"
	local name_length=${#name}
	echo "Hello $upper_name (your name has $name_length characters)"
}

NAMES=( "Madan" "Kumar" "Hitman" "ES" )

for NAME in "${NAMES[@]}"; do 
	greetings "$NAME" 
done   
