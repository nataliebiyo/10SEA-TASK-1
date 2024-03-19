import json

location = input("---> ")

try:
    with open("user_history.json", "r") as f:
        user_history = json.load(f)
    print(user_history)
except FileNotFoundError:
    print("File 'user_history.json' not found.")
except json.JSONDecodeError:
    print("Error decoding JSON from file.")

user_history[location] = "weather"


print("\nupdated")
with open("user_history.json", "w") as f:
    json.dump(user_history, f, indent=4)

for x, y in user_history.items():
    print(x, y)

#print(user_history)