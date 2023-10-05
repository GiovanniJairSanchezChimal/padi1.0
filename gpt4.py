import openai


openai.api_key = "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"

messages = [{"role": "system", "content": "Eres un programador senior"}]
contenido = 'que modelo de gpt eres?'
messages.append({"role": "user", "content": contenido})
respuesta = openai.ChatCompletion.create(model="gpt-4", messages=messages, max_tokens=300)
respuesta_server = respuesta.choices[0].message.content

print(respuesta_server)
