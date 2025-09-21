
import math

degree=float(input("Enter the Number: "))
radian=degree*(math.pi/180)

sin=math.sin(radian)
print( f'the value in sin {degree} is {sin:.4f}')

cos=math.cos(radian)
print( f'the value in cos {degree} is {cos:.4f}')

tan=math.tan(radian)
print( f'the value in tan {degree} is {tan:.4f}')

cosec=1/sin
print( f'the value in cosec is {cosec:.4f}')

sec=1/cos
print( f'the value in sec is {sec:.4f}')

cot=1/tan
print( f'the value in cot {degree} is {cot:.4f}')