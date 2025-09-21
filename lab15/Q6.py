#Write a program to print the sum of the digits in a number

a=input("Enter a number: ")
sum=0
for i in a:
    sum+=int(i)
print(f'The sum of is {sum}')
