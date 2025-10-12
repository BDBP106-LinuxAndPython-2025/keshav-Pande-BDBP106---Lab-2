# A magic date is a date where the date multiplied by the month is equal to the two-digit
# year. For example, June 10, 1960 is a magic date because June is the sixth month, and
# 6 times 10 is 60 which is the two-digit year. Write a function that determines whether
# or not a date is a magic date. Use your function to create a main program that finds
# and displays all of the magic dates in the 20th century.

from datetime import date

for year in range(1901, 2001):   # 20th century
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                d = date(year, month, day)   # makes sure date is valid
                if d.day * d.month == year % 100:
                    print(d.strftime("%d/%m/%Y"))
            except ValueError:
                pass   # skip invalid days

