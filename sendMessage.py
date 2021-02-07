import requests
import json
from pprint import pprint

def sendMessage():
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":1091584118,
        "text":"telegram bot"
    }
    res=requests.get(url,params=p)

token='1690220485:AAFtkQoAYsn2FQ-UqzqRSxWk-WlHitTbWo0'

sendMessage()
