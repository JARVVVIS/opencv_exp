import cv2 
import numpy as np 

#original color
img = cv2.imread('./assets/lena.jpg',cv2.IMREAD_COLOR)

##color value at this location
px = img[55,55]
print(px)

#Modify pixel
img[55,55] = [255,255,255]
px = img[55,55]
print(px)

#ROI -> Region of image
roi  = img[100:150,100:150] 
print(roi)

#convert a region to white
img[100:150,100:500] = [255,255,255]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()