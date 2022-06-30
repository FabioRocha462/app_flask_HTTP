import requests

#método POST

api_url = "http://127.0.0.1:8090/countries"
todo = {"id":5,"name": "Brazil",'capital':"Brazilia","area":129393}
response = requests.post(api_url,json=todo)
print(response.json())
print(response.status_code)
