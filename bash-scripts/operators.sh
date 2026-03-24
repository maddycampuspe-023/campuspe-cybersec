#!/bin/bash

#A=10
#B=45

#using $(()) for aithmetic 

#echo "Addition $((A + B))"
#echo "Substraction $((B - A))"

#((A++))
#((B--))

#comparision

#-eq   ==
#-ne   !=
#-gt   >
#-ge   >=
#-lt   <
#-le  <=
#-z
#-n
 
read -p "Enter a  number " NUM

if [ $NUM -gt 0 ]; then 
	echo $NUM is Positive 
elif [ $NUM -lt 0 ]; then 
	echo $NUM is Neghative
else 
	echo "entered number  is Zero" 
fi 
