import numpy as np 
import matplotlib.pyplot as plt 
import cv2 

img = cv2.imread('./assets/lena.jpg',cv2.IMREAD_COLOR)

#draw a line on the image ; color - BGR
#blue line
cv2.line(img,(0,0),(100,100),(255,0,0),15)

#draw a rectangle
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)

#draw a circle
#-1 will fill in the circle
cv2.circle(img,(100,63),55,(0,0,255),-1)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()