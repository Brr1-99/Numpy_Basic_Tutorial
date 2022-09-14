import numpy as np

""" Multiply two matrix """

a = np.full((3, 2), 4)

b = np.ones((2, 4))

np.matmul(a*b)

""" Get the determinant of a matrix """

c = np.identity(3)

np.linalg.det(c)

""" Get min and max values """

np.min(b, axis=1) # array[1, 1, 1, 1]

np.sum(b) # 8