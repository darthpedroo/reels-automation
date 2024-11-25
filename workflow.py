import json
from utils.eleven_labs import create_tts
from prompts.mega_prompt_generator import videos_personajes

#   Primero ejecutar topic generator para tener los temas a hablar en el video
#   Luego workflow.py para tener los tts
#   Manualmente hacer la voz de homero
#   Create Subtitles manualmente


videos = [
    ("Homero Simpson", "¿Qué es el Manifiesto Ágil y cuáles son sus cuatro valores y doce principios?"),
    ("Homero Simpson", "Cómo se aplican los valores y principios del Manifiesto Ágil en un equipo de trabajo."),
    ("Homero Simpson", "Características principales de Scrum, Kanban y XP en metodologías ágiles."),
    ("Homero Simpson", "Diferencias entre Scrum, Kanban y XP y cuándo usar cada uno según el proyecto."),
    ("Homero Simpson", "¿Qué es la deuda técnica y por qué es importante manejarla?"),
    ("Homero Simpson", "Estrategias simples para reducir la deuda técnica en un proyecto."),
    ("Homero Simpson", "Propósito y beneficios de las reuniones de revisión y retrospectiva en Agile."),
    ("Homero Simpson", "Temas comunes a tratar en una retrospectiva para mejorar los próximos sprints."),
    ("Homero Simpson", "¿Qué significa la Definition of Done (DoD) y por qué es clave para la calidad?"),
    ("Homero Simpson", "Ejemplos de criterios para definir cuándo algo está 'Hecho' en un equipo ágil."),
    ("Homero Simpson", "¿Qué es la Definition of Ready (DoR) y cómo ayuda a preparar el trabajo en Agile?"),
    ("Homero Simpson", "Criterios clave para que una tarea esté 'Lista' y priorizada en Agile."),
]


for video in videos:
    videos_personajes(video[0], video[1])
    
with open("prompts/generated_text_response.json") as f:
    data = json.load(f)
    for i in data:
        respuesta = i["response"]
        create_tts(i)

