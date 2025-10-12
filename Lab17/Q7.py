def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Test case
a = 5
b = 5
c = 8

print("Sides of the triangle are:", a, b, c)
print("Type of triangle:", triangle_type(a, b, c))

