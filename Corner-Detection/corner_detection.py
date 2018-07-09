import cv2
import numpy as np

img = cv2.imread('C:\Users\Umar\Desktop\CV2\DataSet(Input)\opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
# happening in the back end np.float32

#                   change corner points   
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = npint0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 225, -1)
#                   loc   rad  col  
cv2.imshow('corner', img)
        
