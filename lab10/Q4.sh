#!/bin/bash
# Script with exit codes

echo "Enter the filename to check: "
read filename

if [ -e "$filename" ]; then
    echo "File '$filename' exists"
    echo 200
    
    if [ -x "$filename" ]; then
        echo "File '$filename' is executable"
    else
        echo "File '$filename' is not executable"
    fi
else
    echo "File '$filename' does not exist"
    exit 201
fi
