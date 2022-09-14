import numpy as np

""" Accessing elements of the array """

arr = np.array([6.0, 4.2, 9.6], [3.0, 5.0, 1.2])

arr[1, 2] # 1.2

arr[0, :] # array([6.0, 4.2, 9.6])

arr[:, 1] # array([4.2, 5.0])

arr[0, ::2] # array([6.0, 9.6])

""" Advanced access and filter """

a = np.array([1, 2, 4, 6, 6, 9, 3])

a[[0, 3, 6]] # array([1, 6, 3])

a[a < 3] # array([1, 2])

np.any(a > 3, axis=0) # array([False, False, True, True, True, True, False])

((a > 3) & (a < 20)) # array([False, False, True, True, True, True, False])

np.all(~(a < 5))

""" Changing values """

arr[1, 2] = 10.0

arr[:, 1] = [2.0, 3.0]

""" Resizing a matrix """

after = arr.reshape(6, 1) # Resize to any shape as long as it contains the same number of elements

""" Stacking vectors """

np.vstack([arr, arr]) # Vertically stacking

np.hstack([arr, arr]) # Horizontally stacking