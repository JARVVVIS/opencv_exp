import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    #hue saturation value
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([150,150,50])
    upper_red=np.array([180,255,250])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    #where there is 1 in mask we will show color 
    res = cv2.bitwise_and(frame,frame,mask=mask)
    kernel = np.ones((15,15),np.float32)/255 
    #smoothing 
    smoothed = cv2.filter2D(res,-1,kernel)
    #gaussian blur
    blur = cv2.GaussianBlur(res,(15,15),0)
    #medain blur 
    median = cv2.medianBlur(res,15)
    

    cv2.imshow('blur',blur)
    cv2.imshow('sm0oth',smoothed)
    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('result',res)
    cv2.imshow('median',median)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break 
    
cv2.destroyAllWindows()
cap.release()