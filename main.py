from moviepy import *
from moviepy.decorators import requires_duration
import numpy as np
import pysrt



VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920

video = VideoFileClip("resources/videos/Cuphead324x574.mp4")

audioclip = AudioFileClip("resources/audios/homertts_RVC_1.wav")

intro_clip = video.with_subclip(1, 44)



# Definir el texto y la fuente
font = "resources/fonts/tiktok.otf"

list_of_clips =     [
        intro_clip,
    ]

subs = pysrt.open('homero.srt')

def search_images_unsplash(query):
    access_key = 'ukGrNTtP9AG04APLcirq1uQkeZSyw0M65-fv3iqPBJQ'
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={access_key}"
    "https://api.unsplash.com/search/photos?query=SIGNLETON-PROGRAMMIN&client_id=ukGrNTtP9AG04APLcirq1uQkeZSyw0M65-fv3iqPBJQ"



for sub in subs:
    if sub.start is None or sub.end is None:
        print(f"Subtítulo con tiempo inválido: {sub}")
        continue  # Salta este subtítulo si tiene tiempos inválidos
    
    # Duración total del subtítulo
    duration = sub.end - sub.start
    
    # Obtener el número de palabras
    words = sub.text.split()
    
    # Calcular la duración por palabra
    time_per_word = duration.seconds / len(words) if len(words) > 0 else duration
    
    # Duración mínima por palabra (puedes ajustarlo según sea necesario)
    min_duration_per_word = 0.25  # segundos
    
    # Usar la duración mínima si es necesario
    time_per_word = max(time_per_word, min_duration_per_word)
    
    # Inicializar el offset para las palabras
    offset = 0.25  # Le damos un pequeño desfase inicial de 0.3 segundos
    
    # Crear clips para cada palabra con la duración calculada
    for word in words:
        new_text = TextClip(
            font=font,
            text=word.upper(),  # Convertir el texto a mayúsculas
            font_size=40,
            color="white",  # Relleno blanco
            stroke_color="black",  # Borde negro
            stroke_width=4,  # Grosor del borde
            text_align="center",
            method="caption",  # Esto permite que el texto se ajuste automáticamente
            size=(video.size[0] - 40, None),  # Ajusta el tamaño del texto al ancho del video
            margin=(20, 10)  # Añade un margen alrededor del texto
        )
    
        # Establecer la duración de la palabra y el tiempo de inicio con el offset
        new_text = new_text.with_duration(time_per_word).with_start(max(min_duration_per_word,  (sub.start.seconds + offset)))
    
        # Centrar el texto en la pantalla
        new_text = new_text.with_position(('center', 'center'))
        
        # Agregar el nuevo texto a la lista de clips
        list_of_clips.append(new_text)
        
        # Actualizar el offset para la siguiente palabra
        offset += time_per_word  # Incrementar el offset por la duración de la palabra

    # También puedes agregar una superposición de imagen o animación como antes
    overlay_image = ImageClip("resources/images/homer_thinking.png").resized(height=100)
    overlay = overlay_image.with_start(sub.start.seconds).with_position(("left", "bottom")).with_duration(duration.seconds)
    list_of_clips.append(overlay)





try:
    final_clip = CompositeVideoClip(list_of_clips)
    final_clip.audio = audioclip
    # Exportar el video final
    final_clip.write_videofile("./result.mp4", threads=8, fps=24)
except Exception as e:
    print(f"Ocurrió un error al crear el video final: {e}")