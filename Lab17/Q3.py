# Write a program to find the maximum and minimum values of a dictionary.
num= {'a': 100, 'b': 200, 'c': 300}
key=list(num.keys())
max_value=num[key[0]]
min_value=num[key[0]]
for key in num:
    if num[key] > max_value:
        max_value = num[key]
    if num[key] < min_value:
        min_value = num[key]

print(max_value)
print(min_value)