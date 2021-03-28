import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 1 2
# 2 3
a = tf.constant([[1, 2], [2, 3]])
b = tf.constant([[1, 2], [2, 3]])

c = tf.add(a, b)
d = tf.subtract(a, b) 

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

c_out = sess.run(c)
d_out = sess.run(d)

print(c_out)
print(d_out)
