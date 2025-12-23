import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread(r"D:\3rd Year 2nd Semester\CSE-3216 Digital Image Processing Sessional\DIP Sessional\Lab 02\cat.jpeg")

# IMPORTANT CHECK
if img is None:
    raise FileNotFoundError(f"Could not read image at: {img_path}")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = img_gray.shape

img_mirrored = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        img_mirrored[i][j] = img_gray[i][width - j - 1]

plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_mirrored, cmap='gray')
plt.title('Mirrored Image')
plt.axis('off')

plt.show()
