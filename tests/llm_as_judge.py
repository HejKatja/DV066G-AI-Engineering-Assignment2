from utils import chat_ollama

def llm_as_a_judge_agrees(country, answer, expected): 
    prompt = (f"Question: What is the capital of {country}?\n"
              f"Expected answer: {expected}\n"
              f"Given answer: {answer} \n\n"
              f"Does the given answer agree with the expected answer? "
              f"Extra details are fine as long as they do not contradict it. Reply with only YES or NO.")
    verdict = chat_ollama("gemma4", prompt, verbose=False)['message']['content']
    return verdict.strip().upper().startswith("YES")
              