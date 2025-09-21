# Write a script to check if a number is palindrome or not.

num=int(input("Enter the number : "))
original=num
reverse=0

while num>0:
    reverse=num%10
    num=num//10
if reverse==original:
    print(f' Palindrome ')
else:
    print(f' Not a palindrome ')
