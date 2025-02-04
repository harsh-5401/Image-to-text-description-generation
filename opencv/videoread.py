import cv2 as cv

# reading video

# it take interger or path to a vidwe file 
# provide inteer like 0 if you are uisng camera connected to your comp
# capture=cv.VideoCapture(0)

capture=cv.VideoCapture('opencv\Small_waterfall__SaveYouTube_com_.mp4')

# using while loop and reading video frame by frame 
while True:
    isTrue, frame = capture.read()

    # display each frame of video
    cv.imshow('Video' , frame)

    # break out to prevent video from playing infintely
    # if letetr d is pressed break out of this lopp
    if cv.waitKey(20) & 0xFF==ord('d') :
        break

capture.release()
cv.destroyAllWindows()