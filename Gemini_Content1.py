from config import key
import requests
from mic_to_test1 import mic1  # Importing mic1 function from the second code file

def chat1(chat):
    system_message = "I'm an AI assistant known as JADE, here to assist you."
    message_text = system_message + " " + chat
    message = {"role": "user", "parts": [{"text": message_text}]}
    data = {"contents": [message]}
    api_key = "AIzaSyDVTKI80bMig6faJ_10zfgQEzFRixJ5V5g"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    response = requests.post(url, json=data)

    t1 = response.json()
    generated_text = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print("Generated Text:", generated_text)


# chat = mic1()
# chat1(chat)


chat = mic1()  #mic1() function from second_code_file.py returns speech input
chat1(chat)
