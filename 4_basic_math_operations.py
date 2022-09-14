import numpy as np

""" Arithmetic operations"""

arr = np.array([1, 2, 3], dtype= "int16")

arr - 2 # Substracts 2 from all elements

arr * 2 # Multiplies all elements by 2

arr ** 3 # Raises all elements to the third power

arr2 = np.array([1, 4, 2, 0])

arr + arr2 # array([2, 6, 5, 0])

np.cos(arr)