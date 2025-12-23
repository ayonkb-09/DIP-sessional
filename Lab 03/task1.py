import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"D:\3rd Year 2nd Semester\CSE-3216 Digital Image Processing Sessional\DIP Sessional\Lab 03\image.jpg")
array = np.array([ [255, 0, 1, 100, 25, 101], [10, 200, 70, 80, 120, 150], [95, 30, 30, 81, 96, 77], [87, 89, 220, 250, 100, 10],
[18, 7, 221, 21, 8, 15]])
temp = array.copy() #copy the input array in temp variable
max_pixel = np.max(array) #finding the max pixel value in the arr
max_pixel = (2** (np.ceil(np.log2 (max_pixel))))-1 #L-1 = 255
for i in range(0, 5):
    for j in range(0, 6):
        #subtract each pixel value from the max value and replace it11/40
        array[i] [j] = max_pixel-array[i] [j]
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow (temp, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow (array, cmap='gray')
plt.title('Negative Image')
plt.show()