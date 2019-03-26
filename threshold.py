#simplifying an image
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img  = cv2.imread('./assets/book.jpg')
img_gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#any value greater than 12 is equal to [255,255,255].
retval,threshold  = cv2.threshold(img,12,255,cv2.THRESH_BINARY)
print(retval)
retval,threshold2  = cv2.threshold(img_gray,10,255,cv2.THRESH_BINARY)

#adaptive gaussian threshold which adaptively sets the threshold
gauss  = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gauss',gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()