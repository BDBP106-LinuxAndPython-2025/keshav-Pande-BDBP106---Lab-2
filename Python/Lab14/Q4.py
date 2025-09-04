#For Quadratic Equation 

#Input real numbers a,b and c. Treating these as coefficients of the quadratic equation ax2 + bx + c = 0 find and print the roots

import cmath
a=1
b=5
c=6

D=b**2 - 4*a*c

print(D)

x1= (-b + cmath.sqrt(b**2 - 4*a*c))/2*a
x2= (-b - cmath.sqrt(b**2 - 4*a*c))/2*a

print(x1)
print(x2)

