import cv2
import numpy as np
import pygame
from ultralytics import YOLO  # Asegúrate de importar correctamente el modelo YOLO
import re


def detect_objects():
    # Leer nuestro modelo
    model = YOLO('padi.pt')
    pygame.mixer.init()


    # Realizar la captura de video desde la cámara (cambiar a 0 para la cámara predeterminada)
    cap = cv2.VideoCapture(1)
    # Definir el diccionario de nombres de clases
    names = {
        0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck',
        8: 'boat', 9: 'traffic light',
        10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog',
        17: 'horse', 18: 'sheep',
        19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella',
        26: 'handbag', 27: 'tie',
        28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat',
        35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass',
        41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich',
        49: 'orange',
        50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch',
        58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse',
        65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink',
        72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair dryer',
        79: 'toothbrush'
    }

    while True:
        # Leer los fotogramas
        ret, frame = cap.read()

        # Leer resultados
        resultados = model.predict(frame, imgsz=640)

        # Mostrar resultados
        anotaciones = resultados[0].plot()
        cls = []

        for r in resultados:
            boxes = r.boxes.cpu().numpy()

        str_boxes = str(boxes)
        match = re.search(r'cls: array\(\[([\d\s\.,]+)\]', str_boxes)

        if match:
            cls_str = match.group(1)
            cls = np.fromstring(cls_str, sep=',', dtype=float)

        results_counts = {}
        for result_id in cls:
            if result_id in results_counts:
                results_counts[result_id] += 1
            else:
                results_counts[result_id] = 1

        final_name = []
        final_count = []
        for result_id, count in results_counts.items():
            if result_id in names:
                name = names[result_id]
                final_count.append(count)
                final_name.append(name)
                # Reproducir audio si se detecta una persona
                if name == 'person':
                    pygame.mixer.music.load('alarmaAlerta.mp3')
                    pygame.mixer.music.play()


        resultados = []
        for nombre, valor in zip(final_name, final_count):
            resultados.append(f'{valor}:{nombre}')
        print('##########', resultados)
        texto_final = '\n'.join(resultados)
        # Mostrar los fotogramas
        cv2.imshow("Deteccion y segmentacion", anotaciones)

        # Cerrar el programa con la tecla ESC
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()



def detect_objects_interfaz():
    # Leer nuestro modelo
    model = YOLO('padi.pt')

    # Realizar la captura de video desde la cámara (cambiar a 0 para la cámara predeterminada)
    cap = cv2.VideoCapture(1)
    # Definir el diccionario de nombres de clases
    names = {
        0: 'Persona', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light',
        10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep',
        19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie',
        28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat',
        35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass',
        41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange',
        50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch',
        58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse',
        65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink',
        72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair dryer',
        79: 'toothbrush'
    }

    while True:

        # Leer los fotogramas
        ret, frame = cap.read()


        # Leer resultados
        resultados = model.predict(frame, imgsz=640, optimizer=True)
        # Mostrar resultados
        anotaciones = resultados[0].plot()
        cls = []

        for r in resultados:
            boxes = r.boxes.cpu().numpy()

        str_boxes = str(boxes)
        match = re.search(r'cls: array\(\[([\d\s\.,]+)\]', str_boxes)

        if match:
            cls_str = match.group(1)
            cls = np.fromstring(cls_str, sep=',', dtype=float)

        results_counts = {}
        for result_id in cls:
            if result_id in results_counts:
                results_counts[result_id] += 1
            else:
                results_counts[result_id] = 1

        final_name = []
        final_count = []
        for result_id, count in results_counts.items():
            if result_id in names:
                name = names[result_id]
                final_count.append(count)
                final_name.append(name)
        resultados= []
        for nombre, valor in zip(final_name, final_count):
            resultados.append(f'{valor}:{nombre}')

        texto_final = '\n'.join(resultados)

        # Mostrar los fotogramas
        cv2.imshow("Deteccion y segmentacion", anotaciones)

        # Cerrar el programa con la tecla ESC
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
detect_objects()