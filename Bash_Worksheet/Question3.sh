#!/bin/bash
# Script to count words, lines, and characters in a text file

# Check if a filename is provided as a command-line argument
if [ -z "$1" ]; then
    # If no filename is provided, display usage instructions and exit
    echo "Usage: $0 <filename>"
    exit 1
fi

# Check if the provided argument is a valid file
if [ ! -f "$1" ]; then
    # If the file does not exist, display an error message and exit
    echo "Error: $1 is not a valid file."
    exit 1
fi

# Assign the first command-line argument (filename) to a variable
file="$1"

# Count the number of lines in the file using wc with -l option
lines=$(wc -l < "$file")

# Count the number of words in the file using wc with -w option
words=$(wc -w < "$file")

# Count the number of characters in the file using wc with -m option
chars=$(wc -m < "$file")

# Display the results to the user
echo "File: $file"
echo "Lines: $lines"      # Prints the number of lines
echo "Words: $words"      # Prints the number of words
echo "Characters: $chars" # Prints the number of characters

