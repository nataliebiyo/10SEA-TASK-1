import json
import os

def read_history():
    file_path = os.path.join(os.path.dirname(__file__), "user_history.json")
    with open(file_path, "r") as file:
        history = json.load(file)
    return history

print("read")
print(read_history())