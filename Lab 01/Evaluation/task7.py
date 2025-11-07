import numpy as np
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
np1 = np.array(list1)
np2 = np.array(list2)
np3 = np.array(list3)
sum_result = np1 + np2 + np3
print("Element-wise Sum:", sum_result)