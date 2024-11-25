import os
import re
from elevenlabs import save
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HOMER")

# Función para limpiar nombres de archivo
def sanitize_filename(filename):
    # Reemplaza caracteres inválidos con guiones bajos o vacíos
    return re.sub(r'[\/:*?"<>|¿]', '', filename).strip()

def create_tts(json_response):
    client = ElevenLabs(api_key=API_KEY)
    
    # Extraer datos
    text = json_response["response"]
    audio_name = json_response["name"]
    
    # Sanitizar el nombre del archivo
    sanitized_name = sanitize_filename(audio_name)
    
    # Generar audio
    audio = client.generate(
        text=text,
        voice="Brian",
        model="eleven_multilingual_v2"
    )
    
    # Guardar el archivo en la carpeta específica
    os.makedirs("tts_audios", exist_ok=True)  # Crear la carpeta si no existe
    save(audio, f"tts_audios/{sanitized_name}")
