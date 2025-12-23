import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:/3rd Year 2nd Semester/CSE-3216 Digital Image Processing Sessional/DIP Sessional/Lab 02/cat.jpeg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert the input image to grayscale
height=img_gray.shape [0] #shape[0] for no of rows
width=img_gray.shape[1] #shape[1] for no of columns
img_threshold = img_gray.copy()
for i in range (height):
 for j in range (width):
  if img_threshold[i] [j] < 50:
   img_threshold[i][j] = 0
  elif img_threshold[i] [j] > 150:
   img_threshold[i] [j] = 255
#show the image in subplot
plt.subplot(1,2,1)
plt.imshow (img_gray,cmap='gray')
plt.title('Original Image')
plt.subplot(1,2,2)
plt.imshow (img_threshold, cmap='gray')
plt.title('Thresholded Image')
print (img_gray)
print (img_threshold)
plt.show()