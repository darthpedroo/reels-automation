from generate_prompt import generate_situation_with_character
from mega_prompt_generator import videos_personajes

videos = [
    ("Homero Simpson", "Explicación del principio de responsabilidad única en programación orientada a objetos"),
    ("Homero Simpson", "Cómo funcionan las interfaces en programación orientada a objetos"),
    ("Homero Simpson", "La diferencia entre herencia y composición en diseño de software"),
    ("Homero Simpson", "Qué es el polimorfismo y cómo se aplica en programación orientada a objetos"),
    ("Homero Simpson", "Cómo escribir código modular utilizando clases y objetos"),
]

for video in videos:
    # print(video[0], video[1])
    videos_personajes(video[0], video[1])
