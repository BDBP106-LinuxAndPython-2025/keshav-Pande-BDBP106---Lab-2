#Create a string by joining the numbers in the above list a using the comma.
# L = ["Jayshree Nagesh", "Ramakrishnan Nithaya"]
# swapped_list = []
#
# for name in L:
#     parts = name.split()          # Split into ['Jayshree', 'Nagesh']
#     swapped = " ".join(parts[::-1])  # Reverse order and join → 'Nagesh Jayshree'
#     swapped_list.append(swapped)
#
# print(swapped_list)

#Q1
a=[ i for i in range(1,51)]
s1 = ",".join([str(i) for i in a])
print("Comma-separated string:\n", s1)

#Q2
s2 = ".".join([str(i) for i in a])
print("Period-separated string:\n", s2)

#Q3
s3 = "—".join([str(i) for i in a])
print("Dash-separated string:\n", s3)

#Q4
s4 = "\n".join([f"{i} {i**2}" for i in a])
print("Number and its square:\n", s4)

#Q5
people = [
    "Ravi Kumar", "Sneha Patil", "Amit Sharma", "Priya Nair", "Karan Joshi",
    "Meera Singh", "Rahul Deshmukh", "Ananya Gupta", "Vivek Reddy", "Pooja Mehta"
]
upper_case = [p.upper() for p in people]
print("Upper case list:\n", upper_case)

swapped = [" ".join(p.split()[::-1]) for p in people]
print("Swapped names:\n", swapped)

formatted = [".".join([p.split()[0].capitalize(), p.split()[1].capitalize()]) for p in people]
print("Formatted names (First.Last):\n", formatted)

sentence = "She sells sea shells that she collects from the sea floor"
words = sentence.split()
longest = max([w for w in words], key=len)
print("Longest word:", longest)

repeated = [w for w in set(words) if words.count(w) > 1]
print("Repeated words:", repeated)
