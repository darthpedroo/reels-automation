from generate_prompt import generate_situation_with_character
from mega_prompt_generator import videos_personajes

videos = [
    ("Homero Simpson", "Comparación entre una base de datos SQL y una base de datos NO SQL")
]

for video in videos:
    # print(video[0], video[1])
    videos_personajes(video[0], video[1])
