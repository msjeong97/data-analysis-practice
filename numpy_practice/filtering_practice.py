import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(repr(arr == 3))

x_idx, y_idx = np.where(arr == 3)
print(x_idx, y_idx)

# filtering - using positives if filter is true, else using negetives
np_filter = np.array([[True, False], [False, True]])
positives = np.array([[1, 2], [3, 4]])
negatives = np.array([[-1, -2], [-3, -4]])
print(repr(np.where(np_filter, positives, negatives)))

np_filter = positives > 2
print(repr(np.where(np_filter, positives, negatives)))

# fill array as 0 if value  <= 2
print(repr(np.where(np_filter, positives, 0)))

# check arr with stmt
print(repr(arr > 3))
print(np.all(arr > 3))
print(np.any(arr > 3))

# axis option can be used
print(np.any(arr > 3, axis=0))
print(np.any(arr > 3, axis=1))
print('')

arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
has_positive = np.any(arr > 0, axis=1)
print(has_positive)
print(np.where(has_positive))
print(repr(arr[np.where(has_positive)]))




