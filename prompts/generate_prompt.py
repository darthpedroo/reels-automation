import json
import requests

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = 'llama3.2:3b'  # TODO: update this for whatever model you wish to use

def generate(prompt, context):
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True)
    r.raise_for_status()

    full_response = ""  # To store the concatenated text response

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        # the response streams one token at a time, print that as we receive it
        print(response_part, end='', flush=True)

        # Append each part of the response to the full text
        full_response += response_part

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return full_response  # Return the full response as text

def generate_situation_with_character(user_input,personaje,tema):
    context = []  # the context stores a conversation history, you can use this to make the model more context aware
    if not user_input:
        exit()
    print()
    full_response = generate(user_input, context)

    # Save the full text response to a JSON file
    with open('prompts/generated_text_response.json', 'r+', encoding='utf-8') as f:
        
        try:
            # Load existing data
            data = json.load(f)
        except json.JSONDecodeError:
            # If the file is empty or invalid, initialize an empty list
            data = []
        
        new_video = {
            "voz": personaje,
            "tema": tema ,
            "name": f"{tema}.mp3",
            "response": full_response}
        
    
        data.append(new_video)
        f.seek(0)
        f.truncate()
        json.dump(data, f)
        

    return full_response
