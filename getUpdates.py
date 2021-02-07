import requests
import json
import pprint

token='1690220485:AAFtkQoAYsn2FQ-UqzqRSxWk-WlHitTbWo0'
url=f'https://api.telegram.org/bot{token}/getUpdates'

r=requests.get(url=url)
data=r.json()
updates=data["result"]

for update in updates:
    pprint(update)