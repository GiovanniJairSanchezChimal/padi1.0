from ultralytics import YOLO
import cv2
import re
import numpy as np


#leer nuestro modelo
model = YOLO('padi.pt')

#Realizar videocaptura
cap = cv2.VideoCapture(1)


while True:
#leer los fotogramas
    ret, frame = cap.read()
    names= {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydran\
    t', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22:
    'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball\
    ', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42
    : 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'piz\
    za', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse',
    65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}

#leer resultados
    resultados = model.predict(frame, imgsz = 640)
#mostrar resultados
    anotaciones = resultados[0].plot()
    cls = []
    for r in resultados:
        boxes = r.boxes.cpu().numpy()
    str_boxes = str(boxes)
    match = re.search(r'cls: array\(\[([\d\s\.,]+)\]', str_boxes)
    if match:
        cls_str = match.group(1)
        cls = np.fromstring(cls_str, sep=',', dtype=float)
    results_counts ={}
    for result_id in cls:
        if result_id in results_counts:
            results_counts[result_id]+=1
        else:
            results_counts[result_id]=1
    final_name=[]
    final_count=[]
    for result_id, count in results_counts.items():
        if result_id in names:
            name = names[result_id]
            final_count.append(count)
            final_name.append(name)

#mosrtamos los fotogramas
    cv2.imshow("Deteccion y segmentacion", anotaciones)
    print(final_name)
    print(final_count)


#Cerrar el programa
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()