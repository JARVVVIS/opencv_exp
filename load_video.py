import cv2 
import numpy as np 

#starts capturing video from 1st webcam
cap = cv2.VideoCapture(0)
print(type(cap))

#to save the file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./assets/output.avi',fourcc,20.0,(640,480))

while True:
    #ret is a bool , and frame is the frame that is being captured
    ret,frame = cap.read()
    #convert the frame to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray_frame',gray)

    #write the output
    out.write(gray)
    #if q is pressed we want to exit the loop a.k.a stop capturing video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the camera ; stop 
cap.release()
out.release()
cv2.destroyAllWindows()