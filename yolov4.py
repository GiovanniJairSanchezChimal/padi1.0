import cv2
import numpy as np

# Cargar el modelo YOLOv4-tiny
net = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

# Cargar las clases (nombres de las clases) en un archivo de texto
with open('coco.names', 'r') as f:
    classes = f.read().strip().split('\n')

# Cargar la imagen que deseas analizar
image = cv2.imread('results.jpg')

# Obtener las dimensiones de la imagen
height, width = image.shape[:2]

# Configurar la entrada de la red neuronal
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

# Establecer la entrada de la red neuronal
net.setInput(blob)

# Realizar la detección de objetos
outs = net.forward(net.getUnconnectedOutLayersNames())

# Lista para almacenar los resultados de detección
detections = []

# Recorrer las salidas de la red neuronal y filtrar detecciones
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:  # Filtro de confianza (ajusta según tus necesidades)
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            detections.append([x, y, w, h, class_id, confidence])

# Dibujar cuadros delimitadores en la imagen
for detection in detections:
    x, y, w, h, class_id, confidence = detection
    label = f'{classes[class_id]}: {confidence:.2f}'
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Mostrar la imagen con las detecciones
cv2.imshow('YOLOv4-tiny Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
