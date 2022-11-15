import json
world_cup_file = open("data/world_cup_2018.json")
data = world_cup_file.read()
world_cup_data = json.load(data)
