import json
from pprint import pprint

with open('Data\matches1.json') as data_file:
    data = json.load(data_file)
    duration = data["matches"][0]["gameDuration"]
    Id = data["matches"][0]["participants"][0]
    ## Ranks
    ## [Bronze,Silver,Gold,Platinum,Diamond,Master,Challenger] = [1,2,4,8,16,32,64]
    ##

    summonerId = data["matches"][0]["participantIdentities"][1]["player"]["summonerId"] ##gets summonerID allows us to then fetch there past information
    championId = data["matches"][0]["participants"][0]["championId"]
    SummonerRank = data["matches"][0]["participants"][0]["highestAchievedSeasonTier"]
   

pprint(SummonerRank)