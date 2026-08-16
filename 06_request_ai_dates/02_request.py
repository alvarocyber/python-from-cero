# Como hacer peticiones a API´s con Python
# con y sin dependencias

#1. Sin dependencias (dificil)
import urllib.request
import json

api_post = "https://jsonplaceholder.typicode.com/posts/"

try:
    response = urllib.request.urlopen(api_post)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")


# 2. Con dependencias (request)
import requests

print("\n GET:")
api_post = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_post)
json = response.json()
print(json[0])

# 3. Post
print("\n POST:")
try:
    responce = requests.post("https://jsonplaceholder.typicode.com/posts/",
        json = {
            "title": "alvaro",
            "body": "cyber", 
            "userId": 5
        }
            )
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# 3. Put
print("\n Put:")
try:
    responce = requests.put("https://jsonplaceholder.typicode.com/posts/",
        json = {
            "title": "alvaro",
            "body": "cyber", 
            "userId": 5,
            "id":1
        }
            )
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")


key = "Your api key"
# Usar API de openAI
def call_openai_gpt(prompt, key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    data = {
        "model":"gpt-4o-mini",
        "mesagges":[{"role": "user","content":prompt}]  
    }

    response = requests.post(url,json=data,headers=headers)
    return response.json()

api_response = call_openai_gpt("Esctibe un breve poema sobre la programacion",key)
print(api_response["choices"][0]["message"]["content"])

#Llamar a la api de deekseek
key = "sk-479a5c6ce18646df98550f7fafb35c4a"

def call_deepseek(prompt, key):
    url = "https://api.deepseek/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    data = {
        "model":"deepseek-chat",
        "mesagges":[{"role": "user","content":prompt}]  
    }

    response = requests.post(url,json=data,headers=headers)
    return response.json()

api_response = call_openai_gpt("Esctibe un breve poema sobre la programacion",key)
print(api_response["choices"][0]["message"]["content"])