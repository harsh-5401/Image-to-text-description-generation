from ultralytics import YOLO

# Load a model
# model = YOLO("yolo11n.yaml")  # build a new model from YAML

model = YOLO()    

results = model.train(
    data="D:\\object detection\\parastic dataset\\data.yaml",
    epochs=15,  # Start with fewer epochs
    imgsz=640,
    lr0=0.01,  # Adjust as necessary
    lrf=0.1,
    batch=4,  # Smaller batch size   
    patience=5,  # Early stopping, 
    save_txt=True,
    show=True,
    save_json=True
)