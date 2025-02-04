from ultralytics import YOLO

# Load a model
# model = YOLO("yolo11n.yaml")  # build a new model from YAML

model = YOLO()  

# build a new model from YAML

# model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
# model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

# Train the model
# results = model.train(data="D:\object detection\yolo dataset\data.yaml", epochs=30, imgsz=640)




results = model.train(
    data="D:\\object detection\\yolo dataset\\data.yaml",
    epochs=15,  # Start with fewer epochs
    imgsz=640,
    lr0=0.01,  # Adjust as necessary
    lrf=0.1,
    batch=4,  # Smaller batch size   
    patience=5  # Early stopping
)



