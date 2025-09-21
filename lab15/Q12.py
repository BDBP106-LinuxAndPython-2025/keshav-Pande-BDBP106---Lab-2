# Write a program to check if an input string is palindrome
a=str(input("Enter a string: "))
reverse=""
for i in a:
    reverse+= i + reverse
if reverse==a:
    print (f'The {a} is palindrome')
else:
    print (f'The {a} is not palindrome')


a=str(input("Enter a string: "))
reverse=""
for char in a:
    reverse+= char + reverse
print({reverse})
if reverse==a:
    print (f'The {a} is palindrome')
else:
    print (f'The {a} is not palindrome')
