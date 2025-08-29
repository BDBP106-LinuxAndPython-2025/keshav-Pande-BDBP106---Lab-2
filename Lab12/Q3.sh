#!/bin/bash

echo "Enter a number:"
read number
counter=1
until [ $counter -gt 15 ]
do
    result=$((number * counter))
    echo "$number x $counter = $result"
    counter=$((counter + 1))
done
