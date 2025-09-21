# Write a program to print the factorial of a number
num=int(input("Enter the number:"))
factorial=1
multiplication_string = ""
for i in range(1,num+1):
    factorial*=i
    multiplication_string += f" * {i}"
    print(f"{multiplication_string} = {factorial}")
