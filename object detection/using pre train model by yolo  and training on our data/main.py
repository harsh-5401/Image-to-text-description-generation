from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import os


model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

results = model.train(data="D:\object detection\yolo dataset\data.yaml", epochs=10, imgsz=640)



