import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread(r"D:/3rd Year 2nd Semester/CSE-3216 Digital Image Processing Sessional/DIP Sessional/Lab 02/cat.jpeg")

# Safety check
if img is None:
    raise FileNotFoundError("Image not found. Check the path and filename.")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = img_gray.shape

# Ensure correct datatype
img_threshold = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        if img_gray[i][j] < 150:
            img_threshold[i][j] = 0
        else:
            img_threshold[i][j] = 255

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_threshold, cmap='gray')
plt.title('Thresholded Image')
plt.axis('off')

plt.tight_layout()
plt.show()
