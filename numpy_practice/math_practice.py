import numpy as np

arr = np.array([[1, 2], [3, 4]])

print(repr(arr + 1))
print(repr(arr ** 0.5))
print(repr(np.log(arr)))

arr2 = np.array([[2, 2], [1, 1]])

# raise arr2 to power of each number in arr
# arr ** arr2
print(repr(np.power(arr, arr2)))

arr = np.array([[-0.5, 0.8, -0.1], [0.0, -1.2, 1.3]])
arr2 = np.array([[1.2, 3.1], [1.2, 0.3], [1.5, 2.2]])

multiplied = arr * np.pi
added = arr + multiplied
squared = added**2
exp = np.exp(squared)
logged = np.log(arr2)

print(repr(exp))
print(repr(logged))

# (3, 2) * (2, 3) = (3, 3)
matmul1 = np.matmul(logged, exp)
# (2, 3) * (3, 2) = (2, 2)
matmul2 = np.matmul(exp, logged)

print(repr(matmul1))
print(repr(matmul2))

# (2, 3)
arr = [[1, 2, 3], [4, 5, 6]]
# (3, 2)
arr2 = [[1, 2], [3, 4], [5, 6]]

# similar with vector multiplication
mul1 = np.matmul(arr, arr2)
mul2 = np.matmul(arr2, arr)

print(repr(mul1))
print(repr(mul2))
