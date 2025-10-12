#
# Write a program to convert a tuple of angles into a list of tuples with each tuple containing
# the sine and cosine of an angle

import math

def f(x):
    return math.sin(math.radians(x))

def f1(y):
    return math.cos(math.radians(y))

a = (0, 15, 30, 45, 60, 75, 90)

# Calculate sine and cosine lists
b = list(map(f, a))
c = list(map(f1, a))

# Combine both lists into a list of tuples (sin, cos)
d = list(zip(b, c))

print("List of (sine, cosine) tuples:", d)
