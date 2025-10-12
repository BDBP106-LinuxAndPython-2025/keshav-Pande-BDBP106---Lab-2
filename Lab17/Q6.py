# Write a program with a function to calculate the area of a triangle using the formula,
# where a, b, c are sides of the triangle, also providing a test case output from the program
# Area=p
# s(s − a)(s − b)(s − c) where 2s = a + b + c.

import math
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a = 5
b = 6
c = 7
print("Sides of the triangle are:", a, b, c)
print("Area of the triangle = {:.2f}".format(triangle_area(a, b, c)))
