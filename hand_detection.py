#necessary  libs
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.metrics import pairwise

background = None 
accumulated_weight = 0.5 

# top corner of video stream
roi_top = 20
roi_bottom = 300
roi_right = 300
roi_left = 600

def calc_accum_avg(frame,accumulated_weight):
    #grab global background value
    global background
    if background is None:
        background = frame.copy().astype('float')
        return None 
    cv2.accumulateWeighted(frame,background,accumulated_weight)

def segment(frame,threshold_min=25):
    diff = cv2.absdiff(background.astype('uint8'),frame)

    #apply thresholding
    ret,thresholded = cv2.threshold(diff,threshold_min,255,cv2.THRESH_BINARY)

    image,contours,hierarchy = cv2.findContours(thresholded.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None 
    else:
        #largest contour is hand
        hand_segment = max(contours,key=cv2.contourArea)
        return (thresholded,hand_segment)

