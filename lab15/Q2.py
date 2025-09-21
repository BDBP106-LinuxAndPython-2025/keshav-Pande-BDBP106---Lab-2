#!/bin/python

Principal=float(input("Enter principal: "))
Rate=float(input("Enter the rate of interest: "))
Time=float(input("Enter the time in Years: "))

Simple_interest=((Principal*Rate*Time)/100)
print("The interest is",Simple_interest)
print("the Total Amount ",Simple_interest+ Principal)

