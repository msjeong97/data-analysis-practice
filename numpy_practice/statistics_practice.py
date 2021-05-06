import numpy as np

arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])

print(arr.min())
print(arr.max())

print(repr(arr.min(axis=0)))
# 1 == -1
print(repr(arr.min(axis=1)))
print(repr(arr.min(axis=-1)))

print(np.mean(arr))
print(np.var(arr))
print(np.median(arr))
print(np.median(arr, axis=0))
