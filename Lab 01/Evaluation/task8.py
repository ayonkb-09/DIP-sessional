import numpy as np
nparray1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
nparray2 = np.array([5, 6, 7, 8])
nparray3 = np.zeros((3, 4))
nparray4 = np.ones((3, 7))
print("nparray1:\n", nparray1)
print("nparray2:", nparray2)
print("nparray3 (3x4 zeros):\n", nparray3)
print("nparray4 (3x7 ones):\n", nparray4)
# First 2 rows and 2 columns
subarray = nparray1[:2, :2]
print("First 2 rows and first 2 columns of nparray1:\n", subarray)
# First, middle, and last element
flat_array = nparray1.flatten()
first_element = flat_array[0]
middle_element = flat_array[len(flat_array) // 2]
last_element = flat_array[-1]
print("First element of nparray1:", first_element)
print("Middle element of nparray1:", middle_element)
print("Last element of nparray1:", last_element)