import numpy as np

# cumulative sum of elements
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])

# returns the flatten array with cumulative sum
print(repr(np.cumsum(arr)))
# returns the array with cumulative sum across each column   
print(repr(np.cumsum(arr, axis=0)))
print(repr(np.cumsum(arr, axis=1)))

# array concatenation
arr1 = np.array([[0, 72, 3],
                 [1, 3, -60],
                 [-3, -2, 4]])
arr2 = np.array([[-15, 6, 1],
                 [8, 9, -4],
                 [5, -21, 18]])

# same results
print(repr(np.concatenate([arr1, arr2])))
print(repr(np.concatenate([arr1, arr2], axis=0)))

print(repr(np.concatenate([arr1, arr2], axis=1)))
print(repr(np.concatenate([arr2, arr1], axis=1)))


