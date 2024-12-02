import json
from main import create_video_homero
from autogui.automatization import process_audios_auto
from tts.I_tts_generator import ITtsGenerator
from tts.google_tts import GoogleTts
from prompts.mega_prompt_generator import videos_personajes
from utils.create_subtitles import process_audios_to_transcript_folder

from playsound import playsound


import re
import unicodedata

#   Primero ejecutar topic generator para tener los temas a hablar en el video
#   Luego workflow.py para tener los tts
#   Manualmente hacer la voz de homero
#   Create Subtitles manualmente

def sanitize_filename(filename: str) -> str:
    # Normalizar el nombre para eliminar caracteres acentuados y otros caracteres especiales
    filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode('ASCII')
    
    # Reemplazar caracteres no alfanuméricos (excepto guiones y guiones bajos) con guiones bajos
    filename = re.sub(r'[^a-zA-Z0-9_-]', '_', filename)
    
    # Eliminar espacios extra al inicio y al final
    filename = filename.strip()
    
    return filename

def generate_videos_personajes(videos: list[tuple]):
    for video in videos:
        sanitized_name = sanitize_filename(video[1])
        videos_personajes(video[0], sanitized_name)

def generate_tts(json_location_path: str, tts_strategy:ITtsGenerator):
    with open(json_location_path) as f:
        data = json.load(f)
        for response in data:
            tts_strategy.generate_tts(response)

if __name__ == "__main__":
    
    playsound('bell.mp3')
    
    videos = [
    ("Homero Simpson", "Que es una KNEE SURGERY y porque estoy tan emocionado de que sea mañana"),
    ("Homero Simpson", "INTRODUCCION al lenguage de progrmacion rust"),
    ("Homero Simpson", "Introduccion a RUBY ON RAILS"),
    ("Homero Simpson", "¿Qué es el principio de inyección de dependencias?"),
    ("Homero Simpson", "Los secretos de las construcciones medievales"),
    ("Homero Simpson", "¿Cómo funciona un compilador?"),
    ("Homero Simpson", "¿Qué es un patrón de diseño 'factory'?"),
    ("Homero Simpson", "¿Qué es el agua en su estado líquido, sólido y gaseoso?"),
    ("Homero Simpson", "¿Qué es la complejidad algorítmica O(n)?"),
    ("Homero Simpson", "¿Qué es la teoría de la relatividad de Einstein?"),
    ("Homero Simpson", "¿Qué es una interfaz en programación orientada a objetos?"),
    ("Homero Simpson", "La importancia de los números primos"),
    ("Homero Simpson", "¿Qué es un test unitario?"),
    ("Homero Simpson", "El origen del ajedrez"),
    ("Homero Simpson", "¿Qué es el patrón 'observer'?"),
    ("Homero Simpson", "¿Qué es el teorema de Pitágoras?"),
    ("Homero Simpson", "¿Qué es el principio de abierto/cerrado en SOLID?"),
    ("Homero Simpson", "¿Qué es la teoría de la evolución de Darwin?"),
    ("Homero Simpson", "¿Qué son las excepciones en programación?"),
    ("Homero Simpson", "¿Qué es la energía cinética?"),
    ("Homero Simpson", "¿Qué es un endpoint en una API REST?"),
    ("Homero Simpson", "La historia detrás de la Mona Lisa"),
    ("Homero Simpson", "¿Qué es la programación funcional?"),
    ("Homero Simpson", "¿Cómo surgieron los primeros videojuegos?"),
    ("Homero Simpson", "¿Qué son las pilas y colas en estructuras de datos?"),
    ("Homero Simpson", "El arte de la fotografía en la historia"),
    ("Homero Simpson", "¿Qué es el patrón de diseño Singleton?"),
    ("Homero Simpson", "¿Qué son los 'Easter Eggs' en videojuegos?"),
    ("Homero Simpson", "¿Qué es un servidor web?"),
    ("Homero Simpson", "El impacto del Renacimiento en el arte"),
    ("Homero Simpson", "¿Qué son los métodos de búsqueda en bases de datos?"),
    ("Homero Simpson", "¿Por qué son importantes las capas en arquitectura de software?"),
    ("Homero Simpson", "¿Cómo funcionan las máquinas de Turing?"),
    ("Homero Simpson", "¿Qué es un framework en programación?"),
    ("Homero Simpson", "¿Cómo funciona la energía solar?"),
    ("Homero Simpson", "¿Qué es la programación orientada a objetos?"),
    ("Homero Simpson", "¿Cómo afecta el cambio climático a los ecosistemas?"),
    ("Homero Simpson", "¿Qué es un ciclo de vida de software?"),
    ("Homero Simpson", "¿Qué es la herencia en programación orientada a objetos?"),
    ("Homero Simpson", "Los fundamentos de la teoría de la probabilidad"),
    ("Homero Simpson", "¿Qué es una máquina de estados?"),
    ("Homero Simpson", "El ciclo del agua"),
    ("Homero Simpson", "¿Cómo funciona un algoritmo de ordenamiento como QuickSort?"),
    ("Homero Simpson", "¿Qué es la programación concurrente?"),
    ("Homero Simpson", "¿Cómo surgieron los primeros videojuegos?"),
    ("Homero Simpson", "¿Qué es la criptografía?"),
    ("Homero Simpson", "¿Qué es la arquitectura de microservicios?"),
    ("Homero Simpson", "La importancia de la seguridad en la programación"),
    ("Homero Simpson", "¿Cómo hacer pruebas de usabilidad en un sitio web?"),
    ("Homero Simpson", "¿Qué son los videojuegos de estrategia en tiempo real?"),
    ("Homero Simpson", "¿Cómo funciona la transmisión de señales de televisión?"),
    ("Homero Simpson", "¿Qué son las funciones lambda en Python?"),
    ("Homero Simpson", "¿Qué es el principio de segregación de interfaces?"),
    ("Homero Simpson", "El origen del papel moneda"),
    ("Homero Simpson", "¿Qué son las colecciones en Java?"),
    ("Homero Simpson", "El desarrollo de la inteligencia artificial"),
    ("Homero Simpson", "¿Qué es un servidor de bases de datos?"),
    ("Homero Simpson", "La historia de la computación"),
    ("Homero Simpson", "¿Qué es la sobrecarga de operadores en C++?"),
    ("Homero Simpson", "La historia de las olimpiadas"),
    ("Homero Simpson", "¿Qué son los algoritmos de compresión?"),
    ("Homero Simpson", "El impacto de los viajes espaciales en la ciencia"),
    ("Homero Simpson", "¿Qué es un script en programación?"),
    ("Homero Simpson", "¿Qué es la 'lógica difusa' en matemáticas?"),
    ("Homero Simpson", "¿Qué es la programación reactiva?"),
    ("Homero Simpson", "¿Qué es un videojuego de mundo abierto?"),
    ("Homero Simpson", "¿Cómo funciona la energía solar?"),
    ("Homero Simpson", "¿Qué son las máquinas virtuales?"),
    ("Homero Simpson", "La historia de la televisión"),
    ("Homero Simpson", "¿Qué son las API's RESTful?"),
    ("Homero Simpson", "La evolución de las redes sociales"),
    ("Homero Simpson", "¿Qué es el aprendizaje automático?"),
    ("Homero Simpson", "La evolución de los smartphones"),
    ("Homero Simpson", "¿Qué es un videojuego de aventura gráfica?"),
    ("Homero Simpson", "La historia de la música clásica"),
    ("Homero Simpson", "¿Qué es la computación en la nube?"),
    ("Homero Simpson", "¿Qué es un videojuego de disparos en primera persona?"),
    ("Homero Simpson", "¿Qué es un container en Docker?"),
    ("Homero Simpson", "¿Qué es el modelo cliente-servidor?"),
    ("Homero Simpson", "La historia del cine"),
    
    
    
    ("Homero Simpson", "¿Qué es un videojuego de disparos en primera persona?"),
    ("Homero Simpson", "¿Qué son las funciones recursivas?"),
    ("Homero Simpson", "La historia de la televisión"),
    ("Homero Simpson", "¿Qué es la computación en la nube?"),
    ("Homero Simpson", "¿Qué son las máquinas virtuales?"),
    ("Homero Simpson", "La evolución de las redes sociales"),
    ("Homero Simpson", "¿Qué es el aprendizaje automático?")
    
]

    generate_videos_personajes(videos)
    prompts_json_location_path = "prompts/generated_text_response.json"
    tts_strategy = GoogleTts()
    generate_tts(prompts_json_location_path,tts_strategy)
    input_folder = "tts_audios"  
    output_folder = "transcripts_homero" 
    process_audios_to_transcript_folder(input_folder, output_folder)
    
    try:
        playsound('bell.mp3')
    except:
        print("No se pudo reproducir el sonido de la campana")
        
    input("EMPIEZA EL PROCESO DE CREAR AUDIOS. ASEGURATE DE TENER EL RVC ABIERTO Y DEJAR LA COMPU TRABAJANDO UN RATITO")
    process_audios_auto()
    create_video_homero()

