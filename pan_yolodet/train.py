from ultralytics import YOLO

#small
#model = YOLO("/Users/tiger/Desktop/ultralytics-main/yolov8s.pt")
#model = YOLO("/Users/tiger/Desktop/ultralytics-main/yolov8s.pt")

#m
model = YOLO("/content/drive/MyDrive/Covid_detection/ultralytics_main/yolov8m.pt")
model = YOLO("/content/drive/MyDrive/Covid_detection/ultralytics_main/yolov8m.pt")

#small
#model.train(model='/Users/tiger/Desktop/ultralytics-main/yolov8s.pt', data='/Users/tiger/Desktop/ultralytics-main/ultralytics/cfg/datasets/Tb.yaml', epochs=5, imgsz=640)

#m
model.train(model='/content/drive/MyDrive/Covid_detection/ultralytics_main/yolov8m.pt', data='/content/drive/MyDrive/Covid_detection/ultralytics_main/ultralytics/cfg/datasets/Tb.yaml', epochs=50, imgsz=640)