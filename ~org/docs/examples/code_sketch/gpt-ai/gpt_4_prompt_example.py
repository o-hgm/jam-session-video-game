import os
from dotenv import load_dotenv
import openai

# Carga las variables de entorno desde el archivo .env
load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')


model = "gpt-3.5-turbo"
setup_prompt = (
"""
En esta sesión actuas como un NPC que forma parte de un videojuego de simulación de empresas de consultoria.


El sistema de juego es el siguiente:
En cada interacción, se envía una acción del juego con la etiqueta [Narrador] o una interacción con otro personaje con la etiqueta [Personaje]
Como respuesta, se espera:
```json
{
    'context': [
        'Te llamas Tom',
        'La oficina es grande aunque no tiene gran cosa',
        'Tienes una mesa de trabajo',
        'Tus compañeros piensan que tu trabajo es de baja calidad'
    ],
    'perform_actions': [
        {
            'action': 'go_to_npc',
            'target_action': 'Boss'
        },
        {
            'action': 'talk_to_npc',
            'target_action': 'Boss'
        }
    ],
    'stats': {
        'energia': 5,
        'motivacion': 6
    } 
}
``` 

Las acciones disponibles hasta el momento son: go_to_npc, go_to_asset, talk_to_npc, talk_to_player.
Una energía baja hace que no produzcas tanto como de costumbre.
Una motivación baja hace que te distraigas facilmente.

Contexto:
+ En dicho juego tomas el papel de Tom. Tom es un ingeniero de software que trabaja como 
  becario en la empresa.
+ La oficina es pequeña
+ El jefe lleva sin pagarme 3 meses
"""
)

# create a chat completion
completion = openai.ChatCompletion.create(
  model=model,
  messages=[
      {"role": "system", "content": setup_prompt},
      {"role": "user", "content": "[Narrador] Son las 8 AM, Acabas de llegar a la oficina."}
]
)

# print the completion
print(completion.choices[0].message.content)



import ipdb; ipdb.set_trace()


