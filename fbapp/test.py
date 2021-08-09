import requests
import json
from datetime import datetime

timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

BASE = "http://localhost:5000/" 

#Insert a data point
print("Insert a data point :")
response = requests.put(BASE + "flaskAPI/sensordata/", {"id": "123", "timestamp": timestamp, "temperature": 21, "pressure": 1011, "humidity": 204})
print(response.json())
id = response.json()['id']
input()

#Retrieve all datas
print("Retrieve all datas :")
response = requests.get(BASE + "flaskAPI/sensordata/")
print(response.json())
input()

#Retrieve a data point using its ID
print("Retrieve a data point using its ID :")
response = requests.get(BASE + "flaskAPI/sensordata/" + id)
print(response.json())
input()

#Modify a data point
print("Modify a data point :")
response = requests.patch(BASE + "flaskAPI/sensordata/" + id, {"timestamp": timestamp, "temperature": 81, "pressure": 1032, "humidity": 215})
print(response.json())
input()

#Suppress a data point
print("Suppress a data point :")
response = requests.delete(BASE + "flaskAPI/sensordata/" + id)
print(response)