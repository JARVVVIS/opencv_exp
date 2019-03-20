import cv2 
import numpy as np 

#load image
img1 = cv2.imread('./assets/3D-Matplotlib.png')
img2 = cv2.imread('./assets/mainsvmimage.png')
img3 = cv2.imread('./assets/mainlogo.png')

# #stack too images
# add = img1 + img2

# # add  all pixels value together
# # add = cv2.add(img1,img2)

# cv2.imshow('add',add)

# #make weighted images
# w = cv2.addWeighted(img1,0.6,img2,0.4,0)
# cv2.imshow('weight',w)

#threshold the image 
rows,cols,channels = img3.shape
#for identical sizes
roi  = img1[0:rows,0:cols]

img2gray  = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',img2gray)
#do thresholding
#if pixel value is above 220 its converted to white(255) else black(0)
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow('mask',mask)

#blacked out area
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('inverse mask',mask_inv)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img3_fg = cv2.bitwise_and(img3,img3,mask=mask)

dst = cv2.add(img1_bg,img3_fg)
img1[:rows,:cols] = dst
cv2.imshow('res',img1)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img3_fg',img3_fg)


cv2.waitKey(0)
cv2.destroyAllWindows()