# inatll  following packages

# pip install opencv-contrib-python
# pip install caer

# read images in python

import cv2 as cv

img=cv.imread('opencv\img.jpg')
print(img)

# display image 
# we pass name and matric to display 
cv.imshow("flower" , img)


cv.waitKey(0)

# resize and rescale image
# rescale-modify height and width



   