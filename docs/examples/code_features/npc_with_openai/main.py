"""
Create a Prompt iteration with OpenAI's API
"""

import dotenv
import os
import sys
import json
import openai
# import numpy as np


if __name__ == "__main__":
    msg_history = []
    dotenv.load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    game_description = open("game_description.md", "r").read()
    background_story = open("background_story.md", "r").read()
    level_starter = open("level_starter.md", "r").read()

    # Create a prompt
    prompt = (
        game_description + 
        background_story 
    )

    msg_history.extend(
        [
            { "role": "system", "content": prompt},
            {"role": "user", "content": level_starter }
        ]
    )
    while True:
        chat_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=msg_history,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        response_content = chat_response.choices[-1]["message"]["content"]
        msg_history.append({"role": "assistant", "content": response_content })
        print(response_content)
        user_interaction = input(" >> ")
        msg_history.append({"role": "user", "content": user_interaction })
