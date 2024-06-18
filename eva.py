import tkinter as tk
from PIL import Image, ImageTk

# Lista de nombres de archivos de imágenes
image_files = ["padi_1.png", "padi_2.png", "padi_1.png", "padi_1.png", "padi_1.png"]
current_image_index = 0

def update_image():
    global current_image_index
    # Cargar la imagen actual
    image = Image.open(image_files[current_image_index])
    photo = ImageTk.PhotoImage(image)

    # Actualizar la etiqueta con la nueva imagen
    label.config(image=photo)
    label.image = photo

    # Cambiar a la siguiente imagen en la lista
    current_image_index = (current_image_index + 1) % len(image_files)

    # Llamar a esta función nuevamente después de 500 milisegundos (medio segundo)
    label.after(500, update_image)

# Crear la ventana principal
root = tk.Tk()
root.title("Animación de Imágenes")

# Crear una etiqueta para mostrar la imagen
label = tk.Label(root)
label.pack()

# Iniciar la animación
update_image()
# Esperar 4 segundos antes de cambiar a la siguiente imagen

# Iniciar el bucle principal de Tkinter
root.mainloop()
