# Write a program to find the sum of all the elements in a list using lambda and reduce functions.
from functools import reduce
def f(x,y): return x+y
a = list(map(int, input("Enter the input the values to sum : ").split()))
print(reduce(f,a))