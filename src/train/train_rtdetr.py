from ultralytics import RTDETR

def main():
    model = RTDETR("rtdetr-l.pt") 

    model.train(
        data="configs/yolo.yaml",
        epochs=10,
        imgsz=512,
        batch=4,
        device="cpu"
    )

if __name__ == "__main__":
    main()