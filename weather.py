import requests
import json
from pprint import pprint

api_key='1b4ba2abbe57cb51a299f2a1c620f80b'
city_name="Tashkent"
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

res=requests.get(url)
data=res.json()
pprint(data)

#1b4ba2abbe57cb51a299f2a1c620f80b