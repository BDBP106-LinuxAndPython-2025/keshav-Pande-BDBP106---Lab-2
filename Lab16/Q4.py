# Write a script to print the first half of a string, S.
a=str(input('Enter a number: '))
if len(a) % 2 != 0:
    print("The string length is not even.")

first_half = a[:len(a) // 2]
print("First half of the string:", first_half)