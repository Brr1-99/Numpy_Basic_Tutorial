import numpy as np

""" Creating a all 0s matrix """

zero = np.zeros((2, 3))

""" Creating a all 1s matrix """

one = np.ones((4, 1, 2), dtype='int32')

""" Creating a all Ns matrix """

n = np.full((2, 3), 69)

""" Matrix with random numbers """

rand = np.random.rand(4, 3) # Random decimal values

sample = np.random.random_sample(zero.shape)

randint = np.random.randint(6, 10, size=(3, 3))

""" Identity matrix """

i = np.identity(4)

""" Repeat an array n times """

arr = np.array([[1, 2, 3]])

rep = np.repeat(arr, 4, axis=0)