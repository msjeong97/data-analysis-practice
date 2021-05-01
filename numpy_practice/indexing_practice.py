import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# array indexing 
print(repr(arr[:]))
print(repr(arr[:, 1:2]))

# find min max index in array
print(np.argmin(arr[0]))
print(arr[0][np.argmin(arr[0])])
print(np.argmax(arr))

# find min max index in array using axis keyword, axis=0 - see same column idx, axis=1 - see same row idx
print(np.argmin(arr, axis=0))

def slice_data(arr):
	slice1 = arr[:, 0:2]
	slice2 = arr[:, 2:]
	return slice1, slice2

print(repr(slice_data(arr)))	





