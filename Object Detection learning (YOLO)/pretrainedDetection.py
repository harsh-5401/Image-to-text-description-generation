from ultralytics import YOLO
import cv2
from PIL import Image


model = YOLO("yolo11x.pt")

results = model.predict(source="08b92ce5952b2b08_jpg.rf.ee7c1026d9cf805aed984b0640ce2754.jpg", show=True , save_txt=True , save=True)


# from PIL
# PIL stands for Python Imaging Library, and it is used for opening, manipulating,
#  and saving image files

# im1 = Image.open("object images\multiple 2.jpg")
# results = model.predict(source=im1, save=True)  # save plotted images


# im2 = cv2.imread("object images\kidsRunning.jpg")
# results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels


# results = model.predict(source=[im1, im2])


# tracker in video / track nay person/object in video / live video 

# Specifies the use of ByteTrack (a popular multi-object tracking algorithm).
#  The bytetrack.yaml configuration defines how the tracking will be performed.
#  You can customize this file to adjust the parameters for the tracking process.

# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")


# Export the model
# there are various format to export ex= ONNX, TensorRT, CoreML => fastest tensor rt 
# model.export(format="onnx")