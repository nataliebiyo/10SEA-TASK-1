import json

try:
    with open("user_history.json", "r") as f:
        user_history = json.loads(f.read())
        print('read')
        print(user_history)
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Error decoding JSON.")
