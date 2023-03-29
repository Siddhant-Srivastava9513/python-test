

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
   for j in range(0,4):
      print('')
      print(list(response[item].values())[j])




