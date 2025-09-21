# Write a program to reverse a number and print the reversed number.
num=int(input("Enter a number: "))
original=num
reverse=0

while num>0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10

print (f"The reverse number is {reverse}")
