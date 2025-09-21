# Write a program to tell which quadrat a given point lies in the first, second, third or fourth quadrant

x=int(input("Enter the number in x coordinate: "))
y=int(input("Enter the number in y coordinate: "))
if x>0 and y>0:
    print(f'The point is {x} and {y} is in First Quadrant ')
elif x>0 and y<0:
    print(f'The point is {x} and {y} is in Fourth Quadrant ')
elif x<0 and y>0:
    print(f'The point is {x} and {y} is in Second Quadrant ')
elif x<0 and y<0:
    print(f'The point is {x} and {y} is in Third Quadrant ')
elif x==0 and y==0:
    print(f"The point is {x} and {y} is at Origin ")
elif x>0 and y==0:
    print(f"The point is on x axis  ")
elif y>0 and x==0:
    print(f"The point is on y axis  ")
