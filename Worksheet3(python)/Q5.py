# Define matrix addition
def add_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrix dimensions do not match for addition")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Define matrix subtraction
def subtract_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrix dimensions do not match for subtraction")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Example matrices with same dimensions
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [1, 2, 3]]

print("Matrix Addition:")
print(add_matrices(A, B))

print("Matrix Subtraction:")
print(subtract_matrices(A, B))

# Example with dimension mismatch to show error
C = [[1, 2],
     [3, 4],
     [5, 6]]

try:
    print(add_matrices(A, C))
except ValueError as e:
    print("Error:", e)
