import speech_recognition as sr
import openai
import tempfile
import os
from gtts import gTTS
from pydub import AudioSegment
import pyaudio
import json


# Configura tu clave de API de OpenAI
openai.api_key = "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"
def tts(texto):
    # Crear un objeto gTTS y guardarlo como archivo temporal
    tts = gTTS(texto, lang='es')
    tts.save("temp.mp3")

    # Cargar el archivo temporal con pydub
    audio = AudioSegment.from_mp3("temp.mp3")

    # Configurar PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(audio.sample_width),
                    channels=audio.channels,
                    rate=audio.frame_rate,
                    output=True)

    # Reproducir el audio
    stream.write(audio.raw_data)

    # Cerrar PyAudio y el flujo de audio
    stream.stop_stream()
    stream.close()
    p.terminate()

def tts2(texto):
    # Crear un objeto gTTS y guardarlo como archivo temporal
    tts2 = gTTS(texto, lang='en')
    tts2.save("temp.mp3")

    # Cargar el archivo temporal con pydub
    audio = AudioSegment.from_mp3("temp.mp3")

    # Configurar PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(audio.sample_width),
                    channels=audio.channels,
                    rate=audio.frame_rate,
                    output=True)

    # Reproducir el audio
    stream.write(audio.raw_data)

    # Cerrar PyAudio y el flujo de audio
    stream.stop_stream()
    stream.close()
    p.terminate()


def whispper():
    # Inicializa el reconocimiento de voz
    recognizer = sr.Recognizer()

    # Captura audio desde el micrófono durante 5 segundos
    with sr.Microphone() as source:
        print("Habla algo durante 5 segundos...")
        audio = recognizer.listen(source, timeout=5)
        print("¡Audio capturado!")

    # Guarda los datos de audio en un archivo temporal
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
        temp_audio_file.write(audio.get_wav_data())
        audio_file_path = temp_audio_file.name

    # Transcribe el audio usando la API de OpenAI
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            transcript1 = str(transcript)


    except Exception as e:
        print("Error al transcribir el audio:", e)
    finally:
        # Borra el archivo temporal después de usarlo
        if audio_file_path:
            try:
                os.remove(audio_file_path)
            except Exception as e:
                print("Error al eliminar el archivo temporal:", e)
    data = json.loads(transcript1)
    texto = data.get("text")

    return texto

#var = whispper()
#tts(var)
#print(var)



