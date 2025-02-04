import cv2 as cv
import numpy as np

img=cv.imread("opencv\img.jpg")
cv.imshow("img" , img)


# transslation 

# -x -> shifting left

def translate(img,x,y) :
    transMat=np.float32([[1,0,x] , [0,1,y]])
    dimensions= (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , transMat , dimensions)


translated=translate(img , -100 , 100)
cv.imshow("translated"  , translated)


# rotation 

def rotate(img , angle , rotatepoint=None): 
    (height , width) = img.shape[:2]

    if rotatepoint is None:
        rotatepoint=(width//2 , height//2)

    rotmat=cv.getRotationMatrix2D(rotatepoint , angle , 1.0)
    dimensions=(width , height)

    return cv.warpAffine(img , rotmat , dimensions)


rotatedimg=rotate(img ,45 )
# img rotated anticlockwise
cv.imshow("roated img" , rotatedimg)


# resize a image 

# enlarging = cv.INTER_CUBIC  =>slow but high qiality image

resized=cv.resize(img ,(500,500) , interpolation=cv.INTER_CUBIC)
cv.imshow("resize " , resized)


# flipping

# it take image and flip code 
# flip code can be 0,1,-1
# 0-verticla flip
# 1-horizontal flip 
# -1 both flip 

flip=cv.flip(img , 0)
cv.imshow("flip verticaally " , flip)


# cropping

cropped= img[200:400 , 300:400]
cv.imshow("cropped image" , cropped)

cv.waitKey(0)
