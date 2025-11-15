import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"D:\3rd Year 2nd Semester\Mine\CSE-3216 Digital Image Processing Sessional\DIP Sessional\Lab 02\cat.jpeg")

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert the input image to grayscale
height=img_gray.shape[0] #shape [0] for no of rows
width=img_gray.shape[1] #shape[1] for no of columns

#input a zero matrix of the same size of the image
img_mirrored=np.zeros((height,width))

for i in range(height): #flip img gray on y-axis
 for j in range (width):
   img_mirrored[i] [j]=img_gray[i] [width-j-1]

#show the image in subplot
plt.subplot (1,2,1)
plt.imshow (img_gray,cmap='gray')
plt.title('Original Image')

plt.subplot (1,2,2)
plt.imshow (img_mirrored, cmap='gray')
plt.title('Mirrored Image')

plt.show()