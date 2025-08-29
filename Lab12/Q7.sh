#!/bin/bash
# Function to check directory existence

check_directory() {
    local dir_name=$1
    
    if [ -d "$dir_name" ]
    then
        echo "Directory '$dir_name' exists. Files in directory:"
        ls -la "$dir_name"
    else
        echo "Directory '$dir_name' does not exist. Creating it now..."
        mkdir "$dir_name"
        echo "Directory '$dir_name' created successfully."
    fi
}

# Test the function
echo "Enter directory name:"
read directory

# Store function output and execute
result=$(check_directory $directory)
echo "$result"
