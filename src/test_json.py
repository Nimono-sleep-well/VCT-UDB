import json

with open("../resource/text/team_roaster/Roaster.json") as f:
    jason = json.load(f)
    print(jason["eg"]["player"][2])
    
    