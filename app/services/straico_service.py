import requests
import json

url = "https://api.straico.com/v1/prompt/completion"


headers = {
  'Authorization': 'Bearer TY-AX7LCpGWb1qEh7DSGOV1ucPX3EhV1YwNoANr2IY89j3J6B5C',
  'Content-Type': 'application/json'
}


def generate_response(message_body, wa_id, name):
    payload = json.dumps({
    "models": [
        #"anthropic/claude-3.7-sonnet:thinking",
        "meta-llama/llama-4-maverick"
    ],
    "message": "Contexto",


    

    #Cargar archivo para contexto
    "file_urls": [
        "url a reemplazar"
    ]
    })
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


print(generate_response("Hola, que hora es", None, "Felipe"))


def generaurl():
    files=[
  ('file',('galaxy.jpg', open('C:/Users/GATOTEC18/Downloads/galaxy.jpg','rb'), 'image/jpeg'))
]
headers = {
  # 'Content-Type': 'multipart/form-data'  # Esta línea se comenta o elimina
}
