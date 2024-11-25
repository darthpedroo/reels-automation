
from gtts import gTTS
import os
import shutil

def create_tts_from_srt(json_response: dict):

    mytext = json_response["response"]
    language = 'es'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    audio_name = json_response["name"]
    myobj.save(audio_name)
