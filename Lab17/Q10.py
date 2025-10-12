# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find next prime after n
def nextPrime(n):
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

# --- Main Program ---
n = int(input("Enter an integer: "))
print("The next prime number after", n, "is", nextPrime(n))
