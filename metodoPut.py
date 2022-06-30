import requests

#método PUT
api_url = "http://127.0.0.1:8090/countries/1"
todo = {'id':1,'name':'Brasil','capital':'Brasilia','area':'27800000'}
response = requests.put(api_url,json=todo)
print(response.json())
print(response.status_code)