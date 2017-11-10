import json
import requests
from pprint import pprint
import matchCollection
import cassiopeia as cass
import leagues

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v3/leagues/by-summoner/" + ID + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

with open('Data\matches1.json') as data_file:
    data = json.load(data_file)
    duration = data["matches"][0]["gameDuration"]
    matches = data["matches"]
    Id = data["matches"][0]
    region = "na1"
    APIKey = "RGAPI-4e8e60d9-da17-425a-bdd5-15ac360a2a13"

    ## Ranks
    ## [Bronze,Silver,Gold,Platinum,Diamond,Master,Challenger] = [1,2,4,8,16,32,64]
    ## The first three piece of information will go into match collection to look at the history of that person
    participantIdentities = matches[0]["participantIdentities"]
    participant = matches[0]["participants"]
    summonerName = []
    summonerId = []
    accountId = []
    championId = []

    for i in range(0,10):
        summonerName.append(participantIdentities[i]["player"]["summonerName"]) ## gets summoner name from a match
        summonerId.append(participantIdentities[i]["player"]["summonerId"]) ##gets summonerID allows us to then fetch there past information
        accountId.append(participantIdentities[i]["player"]["accountId"]) ## gets account ID from a match
        championId.append(participant[i]["championId"])  # gets champion ID number
        #summonerRank = data["matches"][0]["participants"][0]["highestAchievedSeasonTier"] # gets the Summoner Rank

    summoner_list1 = [summonerName, summonerId, accountId, championId]
    print(summoner_list1)

    for i in  range(0, 10):
        summonerData = requestSummonerData(region, summonerName[i], APIKey)
        rankedData = requestRankedData(region, str(summonerId[i]), APIKey)
        wins = rankedData[0]['entries'][1]['wins']
        losses = rankedData[0]['entries'][1]['losses']
        win_ratio = wins / (wins + losses)
        print("wins:" + '{:4}'.format(str(wins)) + " losses:" + '{:4}'.format(str(losses))+ " win ratio:" + str(win_ratio))

    ##check who won
    # blue_team = data["matches"][0]["teams"][0]["win"]
    #
    # if blue_team == 'Win':
    #     blue_team = 1
    # else :
    #     blue_team = 0

    # pprint(summoner_list1)