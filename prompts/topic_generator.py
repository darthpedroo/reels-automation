from generate_prompt import generate_situation_with_character
from mega_prompt_generator import videos_personajes

videos = [
    ("Homero Simpson", "Qué es UI y cómo afecta la experiencia del usuario"),
    ("Homero Simpson", "La importancia de la investigación en el proceso de UX"),
    ("Homero Simpson", "Cómo diseñar un flujo de aplicación que no genere frustración"),
    ("Homero Simpson", "Las mejores prácticas en UI para mejorar la accesibilidad"),
    ("Homero Simpson", "La diferencia entre UX y UI: Cómo ambos se complementan"),
    ("Homero Simpson", "Cómo usar el contraste y la tipografía para una mejor interfaz de usuario"),
    ("Homero Simpson", "La importancia de la paleta de colores en el diseño de aplicaciones"),
    ("Homero Simpson", "Qué es el Quality Assurance y por qué es esencial en el desarrollo de software"),
    ("Homero Simpson", "Testing vs Quality Assurance: Cuál es la diferencia y por qué importa"),
    ("Homero Simpson", "La importancia de la consistencia en el diseño de interfaces"),
    ("Homero Simpson", "Cómo un buen diseño de interacción puede facilitar la experiencia de usuario"),
    ("Homero Simpson", "El impacto de los wireframes y prototipos en el diseño de aplicaciones"),
    ("Homero Simpson", "Cómo el feedback de los usuarios mejora el diseño final de una aplicación"),
    ("Homero Simpson", "La relación entre UX y la satisfacción del cliente en el desarrollo de software"),
    ("Homero Simpson", "Cómo evitar la sobrecarga visual en el diseño de UI"),
    ("Homero Simpson", "La importancia de la investigación de usuarios en la fase de diseño de una aplicación")
]

for video in videos:
    print(video[0],video[1])
    videos_personajes(video[0],video[1])