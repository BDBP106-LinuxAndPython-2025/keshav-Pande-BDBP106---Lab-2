#!/bin/bash
# Script to check if file exists and is executable

echo "Enter the filename to check: "
read filename

if [ -f "$filename" ]; then
    echo "File '$filename' exists"
else
    echo "File '$filename' does not exist"
fi        
if [ -x "$filename" ]; then
        echo "File '$filename' is executable"
else
        echo "File '$filename' is not executable"
fi
