import speech_recognition as sr

# Crea un objeto de reconocimiento de voz
recognizer = sr.Recognizer()

# Abre el micrófono para escuchar
with sr.Microphone() as source:
    print("Habla algo...")
    audio = recognizer.listen(source)

try:
    # Utiliza el reconocedor de voz para convertir el audio en texto
    texto = recognizer.recognize_google(audio, language="es-ES") # Cambia el idioma según tu preferencia
    print("Texto detectado:", texto)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print("Error en la solicitud:", e)

