import numpy as np
original_array = np.array([[255, 0, 1, 100, 25, 101],
                           [10, 200, 70, 80, 120, 150],
                           [95, 30, 30, 81, 96, 771],
                           [87, 89, 220, 250, 100, 10],
                           [18, 7, 221, 21, 8, 15]])
rows, cols = original_array.shape
height = rows
width = cols
flipped_array = original_array.copy ()
for i in range (height):
 for j in range(width):
  flipped_array[i][j]=original_array[i] [width-j-1]
#for i in range (height):
# flipped_array[i, :] = original_array[i, ::-1]
# Print the original and flipped arrays
print("Original Array:")
print (original_array)
print("\nFlipped Array:")
print (flipped_array)