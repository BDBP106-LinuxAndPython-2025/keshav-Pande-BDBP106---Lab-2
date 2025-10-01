# Write a script to find the sum of squares of first N numbers
num=int(input("Enter a number: "))
sum=0
for i in range(num+1):
    square=i*i
    sum+=square
print(f'The sum of square from 0 to {num} is , {sum}')