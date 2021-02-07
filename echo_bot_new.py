import requests
import json
from pprint import pprint


def getUpdates():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url)
    data=r.json()
    updates=data["result"]
    return updates

def sendMessage(chat_id,text):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":chat_id,
        "text":text
    }
    res=requests.get(url,params=p)

token='1690220485:AAFtkQoAYsn2FQ-UqzqRSxWk-WlHitTbWo0'

len_update=len(getUpdates())
last_len_update=len(getUpdates())

while True:
    last_len_update=len(getUpdates())
    last=getUpdates()[-1]
    last_id=last["message"]["chat"]["id"]
    last_text=last["message"]["text"]
    
    if len_update!=last_len_update:
        sendMessage(last_id,last_text)
        len_update=last_len_update
        
