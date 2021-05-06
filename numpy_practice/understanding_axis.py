import numpy as np

arr = np.arange(2*3*4)
arr = arr.reshape([2, 3, 4])

print(repr(arr))
# array([[[ 0,  1,  2,  3],
#         [ 4,  5,  6,  7],
#         [ 8,  9, 10, 11]],
# 
#        [[12, 13, 14, 15],
#         [16, 17, 18, 19],
#         [20, 21, 22, 23]]])

# dimension of arr - 3
# print(arr.ndim)

# axis=0 - x axis
# axis=0, 즉 x축을 기준으로 합치는 연산이다. return 결과는 x축을 제외한 (3, 4)의 형태의 array이다. 
# 0+12, 1+13, ... 11+23
sum_axis0 = arr.sum(axis=0)
print('sum x axis')
print(repr(sum_axis0))

# axis=1 - y axis
# axis=1, 즉 y축을 기준으로 합치는 연산이다. (2, 4)의 형태의 array를 return한다. 
# 0+4+8, 1+5+9, ... 15+19+23
sum_axis1 = arr.sum(axis=1)
print('sum y axis')
print(repr(sum_axis1))

# x, y축을 기준으로 합치고 싶다. (4)의 형태의 array를 return 한다.
# 0+12 + 4+16 + 8+20, ... 3+15 + 7+19 + 11+23
sum_axis01 = arr.sum(axis=0).sum(axis=0)
print(repr(sum_axis01))

