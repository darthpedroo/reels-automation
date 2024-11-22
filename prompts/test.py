import os
import json

# Verificar si el archivo existe
file_path = "prompts/generated_text_response.json"
if not os.path.exists(file_path):
    print("XD")
    # Crear un archivo JSON vacío con una lista inicial
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)
else:
    print("EXISTE")

with open('prompts/generated_text_response.json', 'r+', encoding='utf-8') as f:
    pass