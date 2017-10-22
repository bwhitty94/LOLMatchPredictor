import json
from pprint import pprint
import matchCollection

with open('Data\matches1.json') as data_file:
    data = json.load(data_file)
    duration = data["matches"][0]["gameDuration"]
    Id = data["matches"][0]#["participants"][0]
    ## Ranks
    ## [Bronze,Silver,Gold,Platinum,Diamond,Master,Challenger] = [1,2,4,8,16,32,64]
    ## The first three piece of information will go into match collection to look at the history of that person
    summonerName = data["matches"][0]["participantIdentities"][1]["player"]["summonerName"] ## gets summoner name from a match
    summonerId = data["matches"][0]["participantIdentities"][1]["player"]["summonerId"] ##gets summonerID allows us to then fetch there past information
    accountId = data["matches"][0]["participantIdentities"][1]["player"]["accountId"] ## gets account ID from a match

    summonerRank = data["matches"][0]["participants"][0]["highestAchievedSeasonTier"] # gets the Summoner Rank
    championId = data["matches"][0]["participants"][0]["championId"]  # gets champion ID number

    matchCollection.print_newest_match(summonerName, accountId, summonerId, "NA")



pprint(summonerId)