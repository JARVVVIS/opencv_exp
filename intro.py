#basic introduction and loading images
#always rem. videos are stacked still frames(images)
#open cv reads image in bgr not in rgb

#import basic libs.
import numpy as np 
import matplotlib.pyplot as plt 
import cv2

#loads in an image and reads as a numpy array
img = cv2.imread('./assets/lena.jpg')
#numpy
print(type(img))
#show by matplotlib
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show();

#load image with filtes
img_fil = cv2.imread('./assets/lena.jpg',cv2.IMREAD_GRAYSCALE)
#title of window, image to be shown
cv2.imshow('image',img_fil)
cv2.waitKey(0)
#destroys all the open cv windows
cv2.destroyAllWindows()