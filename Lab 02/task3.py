import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image from local path (CHANGE THIS PATH)
img = cv2.imread(r"D:\3rd Year 2nd Semester\CSE-3216 Digital Image Processing Sessional\DIP Sessional\Lab 02\cat.jpeg")

# Check if image loaded correctly
if img is None:
    raise FileNotFoundError("Image not found. Check the file path.")

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height = img_gray.shape[0]
width = img_gray.shape[1]

# Create a zero matrix
img_flip = np.zeros((height, width), dtype=np.uint8)

# Flip image vertically (along X-axis)
for i in range(height):
    for j in range(width):
        img_flip[i][j] = img_gray[height - i - 1][j]

# Show images
plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_flip, cmap='gray')
plt.title('Flipped Image')
plt.axis('off')

plt.show()
