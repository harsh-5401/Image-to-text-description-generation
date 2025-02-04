import cv2 as cv

img=cv.imread("opencv\img.jpg")
cv.imshow("img" , img)


# converting to grayscale
# COLOR_BGR2GRAY since we are converting bg2 img to grayscale

gray=cv.cvtColor(img , cv.COLOR_BGR2GRAY )
# cv.imshow("graysclae image " , gray)



# how to blur an image = reduce noise in image 
# paramters aare img , kernal size , border the more kernal size the more blur is image 

blur=cv.GaussianBlur(img , (7,7) ,cv.BORDER_DEFAULT)
# cv.imshow("blur " , blur) 





# edge cascading

# paramters are image  , threshold value 

canny=cv.Canny(img , 125,175)
# and in o/p we can see the edges found in image
# cv.imshow("canny is" ,canny)

# we can reduce edges by passing blur image 

cannyedges=cv.Canny(blur , 125,175)
# cv.imshow("reduce canny edges are" ,cannyedges )



# how to dilate a image using structuring element 
# here our structuring element is edges 

# it takes blur edged imgge , kernal size , interation 
# it can apply on several iteration 

dilated=cv.dilate(cannyedges , (7,7 ) , iterations=3)
# cv.imshow("dilated " , dilated)


# eroding a image 
# eroding dilated image to get structutal element which is here cannyedges



# it takes dilated image  , kernal size , and iteration 
erode=cv.erode(dilated , (7,7) ,iterations=3)
# cv.imshow("eroded image" , erode)


# resize 

# it will resize image to 500 , 500 ignoring aspect ratio
resize = cv.resize(img , (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized" , resize)

# cropping 

cropped=img[50:200 , 200:400]
cv.imshow("cropped img=" ,cropped) 




cv.waitKey(0)