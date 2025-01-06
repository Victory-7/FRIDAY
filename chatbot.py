from transformers import pipeline

chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def chat_with_user(input_text):
    response = chatbot(input_text)
    return response[0]['generated_text']
