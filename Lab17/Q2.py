#Write a program to sum all the values of a dictionary.
num= {'a': 100, 'b': 200, 'c': 300}
sum=0
for key in num:
    sum=sum+num[key]
print(sum)