import json


# Return True if id existe in waiters.json
def connexion(id):
    with open('src/json/waiters.json') as f:
        data = json.load(f)
    for x in data:
        if id == x["id"]:
            return True
    return False

