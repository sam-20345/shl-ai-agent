import json

with open("data/catalogue.json", encoding="utf-8") as f:
    data = json.load(f)

print(data[0])