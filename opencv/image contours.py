import cv2 as cv
import numpy as np

# contours are continous points along the bounday of object 
# countous are useful in shape analysis , object detection and recognition 

img=cv.imread("opencv\img.jpg")
cv.imshow("img" , img)

# conver to gratscale

gray=cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("gray is" , gray)

# get edges

canny=cv.Canny(img , 152 , 175)
cv.imshow("canny edges" , canny)


# finding contours 
contours , hierarchies = cv.findContours(canny , cv.RETR_LIST , cv.CHAIN_APPROX_NONE)

cv.waitKey(0)
