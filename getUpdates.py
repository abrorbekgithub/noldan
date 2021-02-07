import requests
import json
from pprint import pprint


def getUpdates():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url)
    data=r.json()
    updates=data["result"]
    return updates

token='1690220485:AAFtkQoAYsn2FQ-UqzqRSxWk-WlHitTbWo0'

for update in getUpdates():
    pprint(update)