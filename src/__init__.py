import json


def add(a, b):
    return a + b


def connexion(id):
    with open('src/waiters.json') as f:
        data = json.load(f)
    for x in data:
        if id == x["id"]:
            return True
    return False
