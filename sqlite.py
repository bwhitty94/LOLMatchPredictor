import json
from pprint import pprint

with open('Data\matches1.json') as data_file:
    data = json.load(data_file)
    duration = data["matches"][1]["gameDuration"]
    redTeam_Champ = data["matches"][0]["participantIdentities"][2]["player"]["summonerId"]

pprint(redTeam_Champ)