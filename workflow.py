import json
from utils.eleven_labs import create_tts
from prompts.mega_prompt_generator import videos_personajes

#   Primero ejecutar topic generator para tener los temas a hablar en el video
#   Luego workflow.py para tener los tts
#   Manualmente hacer la voz de homero
#   Create Subtitles manualmente


videos = [
]



for video in videos:
    pass
    #videos_personajes(video[0], video[1])
    
with open("prompts/generated_text_response.json") as f:
    data = json.load(f)
    for i in data:
        respuesta = i["response"]
        create_tts(i)

