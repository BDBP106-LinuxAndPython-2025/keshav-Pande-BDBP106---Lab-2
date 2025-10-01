# Write a script to find the highest frequency character in a string, S.
s=str(input("Enter the first string: "))

# Initialize variables for tracking max frequency and character
max_char = ''
max_count = 0

# Loop through each unique character
for char in set(s):
    count = s.count(char)
    if count > max_count:
        max_count = count
        max_char = char

print(f'{max_char} is {max_count}')