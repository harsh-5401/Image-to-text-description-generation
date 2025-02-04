
import cv2 as cv

def rescaleframe(frame , scale=0.75) :
    # images , video , live video 
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

# cv.waitKey(0)

def changeres(width , height) :
    # live video from webcam 
    capture.set(3 , width)
    capture.set(4 , height)



capture=cv.VideoCapture('opencv\Small_waterfall__SaveYouTube_com_.mp4')

# using while loop and reading video frame by frame 
while True:
    isTrue, frame = capture.read()

    frame_resized=rescaleframe(frame)

    # display each frame of video
    cv.imshow('Video' , frame)
    cv.imshow('Video resized ' , frame_resized)
    

    # break out to prevent video from playing infintely
    # if letetr d is pressed break out of this lopp
    if cv.waitKey(20) & 0xFF==ord('d') :
        break

capture.release()
cv.destroyAllWindows()