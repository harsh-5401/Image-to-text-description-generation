from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import os

model = YOLO("D:\\object detection\\runs\\detect\\train6\\weights\\best.pt")

validation_results = model.predict("D:\\object detection\\parastic dataset\\test\\images\\Trichuris-Trichiura--243-_jpg.rf.43a6416271d12d9184e96839f4620e92.jpg", imgsz=640,  show=True , save_txt=True , save=True)


# metrics = model.val(save=True, save_txt=True)  # no arguments needed, dataset and settings remembered
# metrics.box.map  # map50-95
# metrics.box.map50  # map50
# metrics.box.map75  # map75
# metrics.box.maps  # a list contains map50-95 of each category
# print("mAP (50-95):", metrics.box.map)  # Overall mAP
# print("mAP (50):", metrics.box.map50)    # mAP at IoU 0.50
# print("mAP (75):", metrics.box.map75)    # mAP at IoU 0.75
# print("mAP per class:", metrics.box.maps) 