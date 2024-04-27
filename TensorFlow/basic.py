import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np

tensor = tf.constant([[23, 4], [32, 51]])
variable = tf.Variable([[30, 30], [10, 45]])
numpyTensor = np.array([[23, 4], [32, 51]])
tensorFromNumpy = tf.constant(numpyTensor)
variable[0, 1].assign(100)
tfString = tf.constant('TensorFlow')
tfStringArray = tf.constant(['TensorFlow', 'Deep Learning', 'AI'])

print(tensor, end='\n\n')
tensor += 2
print(tensor, end='\n\n')
tensor *= 5
print(tensor, end='\n\n')
print(np.square(tensor), end='\n\n')
print(np.sqrt(tensor), end='\n\n')
print(variable, end='\n\n')
print(np.dot(tensor, variable), end='\n\n')
variable[0, 1].assign(100)
print(variable, end='\n\n')
print(tensor.shape, end='\n\n')
print(tensor.numpy(), end='\n\n')
print(numpyTensor, end='\n\n')
print(tensorFromNumpy, end='\n\n')
print(tfString, end='\n\n')
print(tf.strings.length(tfString), end='\n\n')
print(tf.strings.unicode_decode(tfString, 'UTF8'), end='\n\n')
for string in tfStringArray:
    print(string)
