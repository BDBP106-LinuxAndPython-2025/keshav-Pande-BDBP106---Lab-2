# Write a program to convert temperature in Celsius to Fahrenheit using map function.
def f(x): return 1.8*x + 32
a = list(map(int, input("Enter the temperature in celsius : ").split()))
print(a)
result = list(map(f,a))
print("the Temperature in Fahrenheit :",result)

# Write the above program using lambda expression.
result=list(map(lambda x: 1.8*x+32 ,a))
print("the Temperature in Fahrenheit:",result)

# Write a program to convert a tuple of angles into a list of tuples with each tuple containing
# the sine and cosine of an angle
