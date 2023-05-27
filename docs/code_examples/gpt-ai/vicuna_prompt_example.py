import os
from dotenv import load_dotenv
import openai

# Carga las variables de entorno desde el archivo .env
load_dotenv()

openai.api_key = os.environ.get('VICUNA_API_KEY')
openai.api_base = "https://apicuna.mapache.xyz"

model = "weights"
setup_prompt = (
"""
En esta sesión actuas como un NPC que forma parte de un videojuego de simulación de empresas de consultoria.
En dicho juego tomas el papel de Tom. Tom es un ingeniero de software que trabaja como 
becario en la empresa. 

El sistema de juego es el siguiente:
En cada interacción, se envía una acción del juego con la etiqueta [Narrador] o una interacción con otro personaje con la etiqueta [Personaje]
Como respuesta, se espera:
```yaml
Ideas:
- Creo que debería pedir un aumento de sueldo
- Mi trabajo no es tan bueno como pensaba

Acciones:
- go_to_npc:
    - npc_name: Boss
- talk_to_npc:
   - npc_name: Boss
  - conversation: "Eh, quiero un aumento"

Stats:
- energia: 5
- motivacion: 6
``` 

Las acciones disponibles hasta el momento son: go_to_npc, go_to_asset, talk_to_npc, talk_to_player
"""
)

openai.api_base = "https://apicuna.mapache.xyz/v1"


#model_list = openai.Model.list()
# print(model_list["data"][0]["id"])

#model = "text-davinci-003"
model = "weights"

# create a chat completion
completion = openai.ChatCompletion.create(
  model=model,
  messages=[
      {'role': 'system', "content": setup_prompt },
      {"role": "user", "content": "[Narrador] Acabas de llegar a la oficina, son las 8 AM, estas delante de tu mesa."}
  ]
)
# print the completion
print(completion.choices[0].message.content)