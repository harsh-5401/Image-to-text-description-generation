import cv2 as cv
import numpy as np

# creat balank image
# height , width and no of color channel which is 3

blank=np.zeros((500,500 , 3) , dtype='uint8')
# cv.imshow("blank" , blank)


# img=cv.imread("opencv\img.jpg")
# cv.imshow("image" , img)

# paint a image a certain color
# blank[ : ] = 0,255,0
# cv.imshow("green" , blank)



# paint certian portion of image



# blank[200:300 , 300:400 ] = 0,0,255
# cv.imshow("green" , blank)

# draw a rectangel



# method 1

    # fields are start positon , endposition and volor code 

# cv.rectangle(blank , (0,0) , (250,350) ,(50,20,240) , thickness=cv.FILLED)
# cv.imshow("rectangel" , blank)

# method 2

  # fields are start positon , endposition and volor code ]

# cv.rectangle(blank , (0,0) , (blank.shape[1]//2 , blank.shape[0]//2) , (50,20,240) , thickness=cv.FILLED)
# cv.imshow("another way rectangel" , blank)




# draw a circle on image



# paramters are imagename , center of cicle , radius , color , thickness

# cv.circle(blank , (250,250) , 40 , (250,0,0) , thickness=5)

# make thickness = -1 to make cicle completly filled

# cv.circle(blank , (250,250) , 40 , (250,0,0) , thickness=-1)

# cv.imshow("circle is" , blank)





# # make line on image




# cv.line(blank , (200,300) , (250,250) , (250,255,255) , thickness=3 )
# cv.imshow("line on image " , blank)







# write text on a image 




# it take image , text to put , starting postion ,  font faces , scale , color , thickness

cv.putText(blank , 'hello ' , (0,255) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,255,0) , 2)
cv.imshow("text on image" , blank)

cv.waitKey(0)

