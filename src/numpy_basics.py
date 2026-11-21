import numpy as np

# 1. Creating an array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# 2. Array operations
print("Addition:", arr + 5)
print("Multiplication:", arr * 2)

# 3. Array properties
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# 4. Mathematical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 5. Creating special arrays
print("Zeros:", np.zeros(5))
print("Ones:", np.ones(5))
print("Range:", np.arange(1, 6))

# 6. Two-dimensional array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:")
print(matrix)
print("Matrix shape:", matrix.shape)