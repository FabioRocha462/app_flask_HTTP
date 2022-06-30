import json
import requests

api_url = "http://127.0.0.1:8090/countries/4"
response = requests.delete(api_url)
print(response.json())
print(response.status_code)