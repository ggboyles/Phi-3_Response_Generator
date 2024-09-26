# this script reads prompts from 'prompts.txt' and saves
# the responses to 'responses.txt' using Phi-3 through Ollama


import ollama

# function that gets response from Phi-3 model
def get_response(prompt, model='phi3'):
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

# reads prompts from 'prompts.txt' file
with open("prompts.txt", "r") as file:
    prompts = file.readlines()

# opens a file to save responses
with open("responses.txt", "w") as outfile:
    for prompt in prompts:
        # gets response from the model
        response = get_response(prompt.strip())
        
        # writes prompt and response to 'responses.txt'
        outfile.write(f"Prompt: {prompt.strip()}\nResponse: {response}\n\n")

print("Responses saved to responses.txt")
