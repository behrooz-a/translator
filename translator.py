import gradio as gr
import ollama

def format_history(msg: str):
    chat_history = [{"role": "system", "content": "You are an expert translator that translates English text to French and vice versa. Just translate and do not ask a question unless you did not understand the words or sentences."}]
    chat_history.append({"role": "user", "content": msg})
    return chat_history

def translate(text):
    chat_history = format_history(text)
    response = ollama.chat(model='llama3.1', stream=True, messages=chat_history)
    translated_text = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        translated_text += token
    return translated_text

with gr.Blocks() as demo:
    with gr.Row():
        gr.Image("EN.png", label="Icon")  
    with gr.Row():
        gr.Interface(
            fn=translate,
            inputs=gr.Textbox(label="Enter text to translate/ Saisissez le texte à traduire"),
            outputs=gr.Textbox(label="Translated text/ Texte traduit")
            
        )


