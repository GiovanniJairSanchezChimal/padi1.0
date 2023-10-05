from ultralytics import YOLO
import cv2

#leer nuestro modelo
model = YOLO('padi.pt')

#Realizar videocaptura
cap = cv2.VideoCapture(1)

while True:
#leer los fotogramas
    ret, frame = cap.read()
#leer resultados
    resultados = model.predict(frame, imgsz = 640)
#mostrar resultados
    anotaciones = resultados[0].plot()

#mosrtamos los fotogramas
    cv2.imshow("Deteccion y segmentacion", anotaciones)

#Cerrar el programa
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()