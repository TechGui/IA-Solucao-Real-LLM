import torch
import cv2
import os

# Carrega o modelo YOLOv5 pré-treinado
model = torch.hub.load(
    'ultralytics/yolov5',
    'yolov5s',  
    pretrained=True,
    trust_repo=True
)

# Define a classe 'cow' no COCO (ID 20)
TARGET_CLASS = 'cow'

video_path = "./algoritmos/vacas.mp4"

def detectar_vacas(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Realiza a inferência com o YOLOv5
        results = model(frame)

        # Filtra apenas a classe 'cow'
        for *box, conf, cls in results.xyxy[0]:
            class_name = model.names[int(cls)]
            if class_name == TARGET_CLASS:
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("Detecção de Vacas", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_vacas