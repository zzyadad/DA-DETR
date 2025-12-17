from ultralytics.models import RTDETR

if __name__ == '__main__':
    model = RTDETR(model=r'G:\niuma\object_detect\detr\ultralytics-main\ultralytics\cfg\models\rt-detr\rtdetr-l.yaml')

    # /home/s-zhangzy/RT-DETR/ultralytics-main/ultralytics/cfg/models/v8/yolov8.yaml
    # /home/s-zhangzy/RT-DETR/ultralytics-main/ultralytics/cfg/models/rt-detr/rtdetr-l.yaml
    # 训练配置
    model.train(
        data=r"G:\niuma\object_detect\detr\ultralytics-main\ultralytics\cfg\datasets\masati.yaml",
        epochs=200,
        batch=8,
        device=0,
        imgsz=640,
        workers=8,
        project='RTDETR_train_Brain',
        lr0=0.001,
        optimizer='Adam'
    )

