# if you didn't build tensorflow from source 
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

# [[1 2]	[[1 1]
# 	2 3]]	  1 1]]
a = tf.constant([[1, 2], [2, 3]])
b = tf.constant([[1, 1], [1, 1]])

add_res = tf.add(a, b)
sub_res = tf.subtract(a, b) 
mult_res = tf.multiply(a, b)
div_res = tf.divide(a, b)

print(add_res)
print(sub_res)
print(mult_res)
print(div_res)
