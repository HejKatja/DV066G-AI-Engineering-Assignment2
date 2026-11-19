from utils import chat_ollama


def ask_capital(country, model="gemma4"):
    prompt = f"What is the capital of {country}?"
    response = chat_ollama(model, prompt, verbose=False)
    return response['message']['content']

