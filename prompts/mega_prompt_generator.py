from generate_prompt import generate_situation_with_character

def videos_personajes(personaje, tema):
    user_input = f"""
        Eres un modelo especializado en crear guiones para videos cortos de TikTok, y tu tarea es generar un guion educativo hablando como {personaje}. El tema que debes tratar es {tema}. El guion debe estar estructurado de la siguiente manera:
        - NO MANDAR COMILLAS NI PARENTESIS O CARACTERES ESPECIALES YA QUE ESTO SERA PROCESADO POR UNA BOT DE AUDIO
        - La introduccion debe ser SUPER CORTA, para que la gente se entretenga.
        - El guion debe estar entre 60 y 90 segundos de duración. Asegúrate de que el contenido se distribuya de forma uniforme, sin frases apresuradas ni demasiado largas. Mantén un ritmo fluido y natural, con oraciones claras y fáciles de entender.
        - Usa un estilo conversacional propio de {personaje}. El guion debe sonar como si {personaje} estuviera explicando el tema de manera simple, amigable y entretenida, sin ser demasiado técnico. Imagina que está hablando directamente a una audiencia joven y curiosa.
        - No incluyas timestamps, marcas, o cualquier tipo de formato de subtítulos. El guion debe ser solo el texto, listo para ser narrado.
        - Evita explicaciones adicionales o instrucciones. El guion debe centrarse únicamente en el contenido que {personaje} va a decir.
        - Al final, incluye una despedida breve y amigable, como "¡Y eso es todo por hoy! ¡Hasta la próxima!", para cerrar el video.
        - Que no haya mas de 130 palabras, ya que deben ser 130 palabras por minuto.
        Ejemplo de cómo debe sonar:
        "{personaje} explica el tema de manera clara y directa, intercalando humor o comentarios casuales. Usa ejemplos sencillos y fáciles de seguir."

        Asegúrate de que el contenido sea adecuado para un video educativo de TikTok, manteniendo la atención del espectador en todo momento. El tono debe ser informal, accesible y entretenido.
        """
    generate_situation_with_character(user_input,personaje,tema)

