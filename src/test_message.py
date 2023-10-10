import requests
from dotenv import load_dotenv
import os

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")


def send_whatsapp_message():
    url = "https://graph.facebook.com/v17.0/117559018102316/messages"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN,
        "Content-Type": "application/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "to": YOUR_PHONE_NUMBER,
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }
    response = requests.post(url, headers=headers, json=data)
    return response


# Call the function
response = send_whatsapp_message()
print(response.status_code)
print(response.json())
