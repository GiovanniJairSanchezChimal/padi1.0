from threading import Thread
from main import detect_objects, detect_objects_interfaz
from gpt4 import gpt
from wispper import tts, tts2, whispper
from algoritmo_evaluacion import evaluacion
import tkinter as tk
from PIL import Image, ImageTk

def main_padi():
    thread = Thread(target=detect_objects)
    thread.daemon = True
    thread.start()

    while True:


        welcome = 'Bienvenidos a este curso de inglés impartido por una IA. '
        welcome_2 = 'Mi nombre es PADI, y seré tu profesora de inglés. '
        Leccion1 = 'Repite después de mí: '
        total = welcome + welcome_2 + Leccion1
        tts(total)
        objects = detect_objects()
        respuesta = gpt(objects)
        if respuesta == 'procesando':
            objects = detect_objects()
            respuesta = gpt(objects)
            print(respuesta)
            tts2(respuesta)
            voz = whispper()
            print(voz)
            evaluation = evaluacion(respuesta, voz)
            tts2(evaluation)
            return respuesta
        else:
            print(respuesta)
            tts2(respuesta)
            voz = whispper()
            print(voz)
            evaluation = evaluacion(respuesta, voz)
            tts2(evaluation)
            return respuesta
def main_padi_repeat():
    thread = Thread(target=detect_objects)
    thread.daemon = True
    thread.start()

    while True:

        Leccion1 = 'Repite después de mí: '
        total = Leccion1
        tts(total)
        objects = detect_objects()
        respuesta = gpt(objects)
        if respuesta == 'procesando':
            objects = detect_objects()
            respuesta = gpt(objects)
            print(respuesta)
            tts2(respuesta)
            voz = whispper()
            if voz == 'Salir.':
                break
            else:
                print(voz)
                evaluation = evaluacion(respuesta, voz)
                tts2(evaluation)
        else:
            print(respuesta)
            tts2(respuesta)
            voz = whispper()
            if voz == 'Salir.':
                break
            else:
                print(voz)
                evaluation = evaluacion(respuesta, voz)
                tts2(evaluation)
detect_objects_interfaz()
if __name__ == "__main__":
    main_padi()
    main_padi_repeat()
