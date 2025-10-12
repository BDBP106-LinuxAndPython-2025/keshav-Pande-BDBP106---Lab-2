# Using a simple do loop structure or list comprehension, find the sum of elements in the above list a.
a=sum([i for i in range(1,51)])
print(a)

asum=0
result=[asum:=asum +i for i in range(1,51)][::-1]
print(result)



# Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
# List comprehension for prime numbers from 1 to 50
c=[]
b = [x for x in range(2, 51) if [i for i in range(2, x) if x % i == 0]]
c.append(b)
# [x for x in range(2, 51) if ...]  Take every number x from 2 to 50 and include it in the list only if the condition after if is true
#[i for i in range(2, x) if x % i == 0] range(2, x) → goes through all possible divisors of x.
# if x % i == 0 → checks if x is divisible by i.
# It creates a list of divisors of x (excluding 1 and itself).
# Example:
# If x = 10 → [i for i in range(2, 10) if 10 % i == 0] → [2, 5]
# If x = 7 → [i for i in range(2, 7) if 7 % i == 0] → []

#if x % i == 0] == []]
# “Include x in the list only if it has no divisors between 2 and x−1.”

print("Prime numbers from 1 to 50:", c)


#Question 2.3
# List a (1 to 50)
a = [i for i in range(1, 51)]

# List b (prime numbers from 1 to 50)
b = [x for x in range(2, 51) if [i for i in range(2, x) if x % i == 0] == []]

# Common elements using list comprehension
c = [i for i in a if i in b]

print("Common numbers in a and b:", c)
