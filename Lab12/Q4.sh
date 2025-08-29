#!/bin/bash
read -ra number < nums.txt

echo "${number[@]}"

for n in "${number[@]}"
do 
        double=$((n*2))
	echo "$n double = $double "

done



