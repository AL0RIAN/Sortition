import json

def read_variable():
    with open('shared_variable.json', 'r') as f:
        return json.load(f)

def write_variable(value):
    with open('shared_variable.json', 'w') as f:
        json.dump(value, f)