import tensorflow as tf

a = tf.constant(1.0)
b = tf.constant(2.0)
c = tf.constant(3.0)
d = (a + b) / c  # or tf.div(tf.add(a, b), c)

with tf.Session() as session:
  print(session.run(d))