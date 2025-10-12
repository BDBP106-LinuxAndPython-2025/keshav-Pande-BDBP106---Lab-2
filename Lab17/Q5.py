s1 = ("IBAB is Best IBAB")
s2 = s1.split()  # Split the sentence into words
print(s2)
# Use a dictionary to remove duplicates and preserve order
s3 = list(dict.fromkeys(s2))
print(s3)
# Join the list back into a sentence
s4 = ' '.join(s3)
print(s4)