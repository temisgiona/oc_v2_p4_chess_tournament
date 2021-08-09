#~/FlaskAPI/test_auth.py

import requests
import json
from datetime import datetime

timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

BASE = "http://localhost:5000/" 

#Signup
print("Signup :")
response = requests.put(BASE + "flaskAPI/auth/signup/", {"email": "user@email.com", "password": "userpasswd"})
print(response.json())
input()

#Login
print("Login :")
response = requests.put(BASE + "flaskAPI/auth/login/", {"email": "user@email.com", "password": "userpasswd"})
print(response.json())
token = response.json()['token']
headers = {'Authorization':'Bearer ' + str(token)}
print(token)
input()

#Insert data
print("Insert data :")
response = requests.put(BASE + "flaskAPI/sensordata/", {"timestamp": timestamp, "temperature": 21, "pressure": 1011, "humidity": 204}, headers = headers)
print(response.json())
id = response.json()['id']
input()

#Retrieve data
print("Retrieve data :")
response = requests.get(BASE + "flaskAPI/sensordata/" + id, headers = headers)
print(response.json())
input()

#Delete data
print("Delete data :")
response = requests.delete(BASE + "flaskAPI/sensordata/" + id, headers={'Authorization': token})
print(response)