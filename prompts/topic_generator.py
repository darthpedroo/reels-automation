from generate_prompt import generate_situation_with_character
from mega_prompt_generator import videos_personajes

videos = [
    ("Rigby de Un Show Mas", "Explicacion del principio de Responsabilidad unica en programcion orientada a objetos"),

]

for video in videos:
    print(video[0],video[1])
    videos_personajes(video[0],video[1])