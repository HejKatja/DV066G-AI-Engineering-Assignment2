import multiprocessing
import ollama

def chat_ollama(model, prompt, image=None, timeout_seconds=40, verbose=True):
    with multiprocessing.Pool(processes=1) as pool:
        if image is None:
            async_result = pool.apply_async(call_ollama_chat, (model, prompt))
        else:
            async_result = pool.apply_async(call_ollama_image, (model, prompt, image))
        try:
            if verbose: print(f"Prompting {model}: {prompt}")
            result = async_result.get(timeout=timeout_seconds)
            return result
        except multiprocessing.TimeoutError:
            if verbose: print(f"\tTimeout after {timeout_seconds} seconds.")
            pool.terminate()
            pool.join()
            return {'message': {'content': "Timeout."}}
        except Exception as e:
            if verbose: print(f"\tChat call failed: {e}")
            pool.terminate()
            pool.join()
            return {'message': {'content': "Failure."}}

def call_ollama_chat(current_model, prompt):
    return ollama.chat(model=current_model, messages=[{'role': 'user', 'content': prompt}])


def call_ollama_image(current_model, prompt, image):
    return ollama.chat(model=current_model, messages=[{'role': 'user', 'content': prompt, 'images': [image]}])
