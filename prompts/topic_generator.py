from generate_prompt import generate_situation_with_character


videos = [
    #("Homero Simpson", "Por qué los programadores prefieren el café al té"),
   # ("Homero Simpson", "La diferencia entre Python y Java: Cuál es más fácil de aprender"),
   # ("Homero Simpson", "Qué es un bug y cómo evitarlo"),
   # ("Homero Simpson", "La magia de los algoritmos: Cómo Google sabe todo"),
   # ("Homero Simpson", "Por qué las variables son como cajas de donas"),
   # ("Homero Simpson", "Qué son los frameworks y por qué todos los aman... o los odian"),
    ("Homero Simpson", "La diferencia entre frontend y backend: ¿Quién tiene el trabajo más fácil?"),
    ("Homero Simpson", "Qué es un IDE y por qué debería importarte"),
    ("Homero Simpson", "Cómo funcionan las bases de datos sin romperte la cabeza"),
    ("Homero Simpson", "Qué es la programación funcional y por qué suena tan aburrido"),
    ("Homero Simpson", "Cómo funciona el machine learning explicado con donas"),
    ("Homero Simpson", "Por qué los programadores usan tanto 'foo' y 'bar'"),
    ("Homero Simpson", "La historia detrás de los lenguajes de programación más populares"),
    ("Homero Simpson", "Qué es un stack overflow y por qué no es un sitio de recetas"),
    ("Homero Simpson", "Qué es la inteligencia artificial y cómo podría quitarme el trabajo"),
    ("Homero Simpson", "Por qué las pruebas unitarias son como revisar la cerveza antes de tomarla"),
    ("Homero Simpson", "Qué son las APIs y por qué las usamos todo el tiempo"),
    ("Homero Simpson", "Cómo funciona internet explicado para simples mortales"),
    ("Homero Simpson", "Por qué los servidores no son meseros (pero sí son importantes)"),
    ("Homero Simpson", "Qué es Git y cómo evitar perder tu código para siempre")
]

for video in videos:
    print(video[0],video[1])
    generate_situation_with_character(video[0],video[1])