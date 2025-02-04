from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import os

model = YOLO("D:\\object detection\\runs\\detect\\train6\\weights\\best.pt")

# validation_results = model.predict("D:\\object detection\\parastic dataset\\test\\images\\Ancylostoma-Spp--39-_jpg.rf.73ca96803b9aab00588beb77128d9251.jpg", imgsz=640, conf=0.25 , show=True , save_txt=True , save=True)

# validation_results = model.predict("D:\\object detection\\parastic dataset\\test\\images\\Ascaris-Lumbricoides--57-_jpg.rf.fbc1343917c182bb167a9a25fa337427.jpg", imgsz=640, conf=0.25 , show=True , save_txt=True , save=True)


validation_results = model.predict("D:\\object detection\\parastic dataset\\test\\images\\Schistosoma--217-_jpg.rf.e7de39464aa920ee28afb8fadf0a6c03.jpg", imgsz=640, conf=0.25 , show=True , save_txt=True , save=True)


# parastic dataset\test\images\Schistosoma--217-_jpg.rf.e7de39464aa920ee28afb8fadf0a6c03.jpg

# parastic dataset\test\images\Ascaris-Lumbricoides--57-_jpg.rf.fbc1343917c182bb167a9a25fa337427.jpg

# parastic dataset\test\images\Taenia-Sp--179-_jpg.rf.4b307cd57a14c1ddfa5be2be1b6e8d0b.jpg

# metrics = model.val(save=True, save_txt=True)  # no arguments needed, dataset and settings remembered
# metrics.box.map  # map50-95
# metrics.box.map50  # map50
# metrics.box.map75  # map75
# metrics.box.maps  # a list contains map50-95 of each category
# print("mAP (50-95):", metrics.box.map)  # Overall mAP
# print("mAP (50):", metrics.box.map50)    # mAP at IoU 0.50
# print("mAP (75):", metrics.box.map75)    # mAP at IoU 0.75
# print("mAP per class:", metrics.box.maps) 