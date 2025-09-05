#!/bin/bash

if [ $# -eq 4 ]; then 
	echo " the first argument is:" $1
	echo " the second argument is:" $2
	echo " the third argument is:" $3
	echo " the four argument is:" $4
	echo " "
	echo " the four argurments are : $@"
	exit 0

else
	echo "four argument are required"
	exit 1 
fi

