import numpy as np

""" Creating arrays """

arr = np.array([1, 2, 3], dtype= "int16")

arr2 = np.array([6.0, 4.2, 9.6], [3.0, 5.0, 1.2])

""" Get parameters of the arrays """

arr.ndim # 1 dimension

arr2.shape # (2,3) 2 arrays of length 3

arr.itemsize # 2 bytes of memory

arr.size # 3 number of elements

arr.nbytes # 6 itemsize * size

""" Create np from file """

file = np.genfromtxt('file.txt', delimiter=',')