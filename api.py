import requests
url="https://gorest.co.in/public/v2/users"
response=requests.get(url)
print(response.json())