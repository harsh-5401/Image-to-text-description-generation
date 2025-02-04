# from ultralytics import YOLO

from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import os



# # Customize validation settings
# validation_results = model.val(data="D:\\object detection\\yolo dataset\\data.yaml", imgsz=640, conf=0.25 , save=True, save_txt=True)



# real   on trained model on images

model = YOLO("D:\\object detection\\runs\\detect\\train\\weights\\best.pt")
validation_results = model.predict("D:\\object detection\\yolo dataset\\train\\images\\0b29c79bee09e9f9_jpg.rf.e260f499c4f5dfe741c37307a4e13517.jpg", imgsz=640, conf=0.25 , show=True , save_txt=True , save=True)


# test using yolo model on same image


# model = YOLO("yolo11n.pt")
# validation_results = model.predict("D:\\object detection\\yolo dataset\\train\\images\\0b29c79bee09e9f9_jpg.rf.e260f499c4f5dfe741c37307a4e13517.jpg", imgsz=640, conf=0.25 , show=True , save_txt=True , save=True)





# print("validation result................=" , dir(validation_results))



# Load a model

# model = YOLO("yolo11n.yaml")  # load an official model

# model = YOLO("D:\object detection\runs\detect\train9\weights\best.pt")  # load a custom model


# model = YOLO("D:\\object detection\\runs\\detect\\train11\\weights\\best.pt")




# Validate the model

metrics = model.val(save=True, save_txt=True)  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list contains map50-95 of each category
print("mAP (50-95):", metrics.box.map)  # Overall mAP
print("mAP (50):", metrics.box.map50)    # mAP at IoU 0.50
print("mAP (75):", metrics.box.map75)    # mAP at IoU 0.75
print("mAP per class:", metrics.box.maps) 


# image_paths = ["D:\\object detection\\yolo dataset\\valid\\images\\0f6f3b623f39f09a_jpg.rf.0e007c0e9eb63c136c0fd4af1ea4e069.jpg",
#                "D:\\object detection\\yolo dataset\\valid\\images\\02b89c1aabb61c46_jpg.rf.0aa02568ac111cfe4e66f4c2b257310a.jpg"]

# image_dir = "D:\\object detection\\yolo dataset\\valid\\images"










