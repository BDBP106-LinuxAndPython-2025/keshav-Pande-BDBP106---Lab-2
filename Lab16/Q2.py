# Write a script that computes power - raise base to the n-th power. Eg. power(2, 5). Here base is 2 and n-th power is 5.

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent (n): "))
y=1
for i in range(exponent-1):
    y = base ** exponent
print(y)