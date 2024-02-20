import requests

url = 'http://localhost:5000/users/1'

response = requests.delete(url)

print(response.status_code)