import json
import random
from moviepy import *
from moviepy.decorators import requires_duration
import numpy as np
import pysrt


def create_video(gameplay_location:str, audio_clip_location:str, json_transcript_location:str, personaje_image_location:str, name:str):
    print("Creando un video !")
    #VIDEO_WIDTH = 1080
    #VIDEO_HEIGHT = 1920

    #subs = pysrt.open('resources/srts/new_script.srt')

    with open (json_transcript_location, "r", encoding="utf-8") as f:
        words = json.load(f)
        FINAL_TIME = words[-1]["end"]
        
    DURATION = FINAL_TIME

    video = VideoFileClip(gameplay_location)
    audioclip = AudioFileClip(audio_clip_location)
    intro_clip = video.with_subclip(1, DURATION)


    # Definir el texto y la fuente
    font = "resources/fonts/tiktok.otf"

    list_of_clips =     [
            intro_clip,
        ]

    overlay_image = ImageClip(personaje_image_location).resized(height=160)
    overlay = overlay_image.with_start(0).with_position(("left", "bottom")).with_duration(DURATION)
    #overlay_image = overlay_image.with_opacity(1)

    list_of_clips.append(overlay)

    def add_subs_v2(list_of_clips):
        with open (json_transcript_location, "r", encoding="utf-8") as f:
            words = json.load(f)
            for word in words:
                
                new_text = TextClip(
                    font=font,
                    text=word["word"].upper(),  # Convertir el texto a mayúsculas
                    font_size=40,
                    color="white",  # Relleno blanco
                    stroke_color="black",  # Borde negro
                    stroke_width=4,  # Grosor del borde
                    text_align="center",
                    method="caption",  # Esto permite que el texto se ajuste automáticamente
                    size=(video.size[0] - 40, None),  # Ajusta el tamaño del texto al ancho del video
                    margin=(20, 10)  # Añade un margen alrededor del texto
                )
                
                duration = word["end"] - word["start"]
                new_text = new_text.with_duration(duration).with_start(word["start"])
                # Centrar el texto en la pantalla
                new_text = new_text.with_position(('center', 'center'))
                
                # Agregar el nuevo texto a la lista de clips
                list_of_clips.append(new_text)
        
        return list_of_clips

    list_of_clips = add_subs_v2(list_of_clips)

    try:
        final_clip = CompositeVideoClip(list_of_clips)
        final_clip.audio = audioclip
        # Exportar el video final
        export_name = f"./exports/{name}.mp4"
        final_clip.write_videofile(export_name, threads=8, fps=24)
    except Exception as e:
        print(f"Ocurrió un error al crear el video final: {e}")
