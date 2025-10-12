
def fibonacci_odds(n):
    fib = [0, 1]

    while (next_value := fib[-1] + fib[-2]) and len(fib) < n:
        fib.append(next_value)
    odd_fib = list(filter(lambda x: x % 2 != 0, fib[:n]))
    return odd_fib
n = int(input("Enter number of terms: "))
print("Odd Fibonacci numbers:", fibonacci_odds(n))


