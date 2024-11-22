import json
from utils.srt_to_tts import create_tts_from_srt


#   Primero ejecutar topic generator para tener los temas a hablar en el video
#   Luego workflow.py para tener los tts
#   Manualmente hacer la voz de homero
#   Create Subtitles manualmente

with open("prompts/generated_text_response.json") as f:
    data = json.load(f)
    for i in data:
        respuesta = i["response"]
        create_tts_from_srt(i)

