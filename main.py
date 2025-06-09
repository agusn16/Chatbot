import os
from dotenv import load_dotenv
import google.generativeai as genai

#Configuracion de la api
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key = API_KEY)

#Model
model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat()
print('chat Geminis - para salir escriba salir')

while True:
    pregunta = input('vos: ')
    if pregunta.lower() in ['salir','chau','hasta luego']:
        print('chat Geminis - hasta luego')
        break
    try:
        respuesta = chat.send_message(pregunta)
        print(f'chat Geminis: {respuesta.text}')
    except Exception as e:
        print(f'chat Geminis: {e}')

