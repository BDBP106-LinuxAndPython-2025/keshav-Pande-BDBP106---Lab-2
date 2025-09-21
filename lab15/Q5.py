
import cmath
a=int(input("Enter the number : "))
b=int(input("Enter the Quadratic number : "))
c=int(input("Enter the constant : "))

D =(b**2 - 4*a*c)

x1= (-b + cmath.sqrt(b**2 - 4*a*c))/2*a
x2= (-b - cmath.sqrt(b**2 - 4*a*c))/2*a

print(x1)
print(x2)
