from tts.I_tts_generator import ITtsGenerator
from gtts import gTTS
import os
import shutil

class GoogleTts(ITtsGenerator):
    
    def generate_tts(self, parsed_json_data:dict):
        
        mytext = parsed_json_data["response"]
        language = 'es'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        audio_name = parsed_json_data["name"] 
        myobj.save(audio_name)
        shutil.move(audio_name, "tts_audios/" + audio_name)
