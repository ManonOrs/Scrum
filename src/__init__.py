# def add(a, b):
#     return a + b
import json

def connexion(id):
    if id == 1:
        return True
    else:
        return False

print(connexion(1))

with open('src/waiters.json') as f:
   data = json.load(f)

if "id" in data:
    print("Key exist in JSON data")
    print(data["name"])
else:
    print("Key doesn't exist in JSON data")