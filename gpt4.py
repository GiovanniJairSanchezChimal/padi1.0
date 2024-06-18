
def gpt(objetos):
    import openai
    openai.api_key = "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"
    respuesta_server = 'procesando'
    if objetos == '':
        return respuesta_server
    else:
        messages = [{"role": "system", "content": "Eres una profesora de inglés llamada PADI"}]
        contenido = 'genera una oración de no mas de 5 palabras de nivel principiante en inglés con los siguientes objetos' + objetos
        messages.append({"role": "user", "content": contenido})
        respuesta = openai.ChatCompletion.create(model="gpt-4", messages=messages, max_tokens=300)
        respuesta_server = respuesta.choices[0].message.content
        return respuesta_server


def gptfrench(objetos):
    import openai
    openai.api_key = "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"
    messages = [{"role": "system", "content": "Eres una profesora de francés llamada PADI"}]
    contenido = 'genera una oración de nivel principiante en francés con los siguientes objetos' + objetos
    messages.append({"role": "user", "content": contenido})
    respuesta = openai.ChatCompletion.create(model="gpt-4", messages=messages, max_tokens=300)
    respuesta_server = respuesta.choices[0].message.content
    return respuesta_server

#text ='como te llamas'
#respuesta=gpt(text)
#print(respuesta)