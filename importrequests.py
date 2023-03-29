import requests
import json
url="https://gorest.co.in/public/v2/users"
thislist=[]
respons=requests.get(url)
response=respons.json()
count=0
for i in response:
   count=count+1;
for item  in range(0,count-1):
   print(' ')
   print('')
   print('name:',list(response[item].values())[1])
   print('id:',list(response[item].values())[0])
   print('email address:',list(response[item].values())[2])
  
  


