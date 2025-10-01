# Write a script that computes the number of 1s in a binary representation of a decimal number, N.

x1 = int(input("Enter a decimal number: "))

# Convert to binary string (without '0b' prefix)
binary_str = format(x1, 'b')
print(f"Binary format: {binary_str}")

# Count number of '1's
count = 0
for i in binary_str:
    if i == '1':
        count += 1

print(f"Number of 1s: {count}")
