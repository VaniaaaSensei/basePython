from . import config
import requests, json, random

apikey = random.choice(config.groq_apikey)
prompt = "Hi, Saya adalah WhatsApp bot berbasis Pemograman Python yang di rancang oleh Fizzxy Dev, tugas saya adalah membantu menjawab pesan yang anda berikan"

def chat(msg):
    headers = {
        "Authorization": f"Bearer {apikey}",
        "Content-Type": "application/json"
    }

    data = {
        "messages":[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": msg,
            }
        ],
        "model": "llama3-8b-8192"
    }

    post = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data).json()

    return post["choices"][0]["message"]["content"]