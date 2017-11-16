import json
import requests
import time
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
    APIKey = "RGAPI-5f7751d0-2d0d-4313-b26b-08c642a72245"
    newfile = open("newfile.txt", "w+")

    ## Ranks
    ## [Bronze,Silver,Gold,Platinum,Diamond,Master,Challenger] = [1,2,4,8,16,32,64]
    ## The first three piece of information will go into match collection to look at the history of that person

    number_matches = 0
    for j in range(0,100):

        participantIdentities = matches[j]["participantIdentities"]
        participant = matches[j]["participants"]
        summonerName = []
        summonerId = []
        accountId = []
        championId = []
        tmpString = ""
        isError = False

        for i in range(0,10):
            summonerName.append(participantIdentities[i]["player"]["summonerName"]) ## gets summoner name from a match
            summonerId.append(participantIdentities[i]["player"]["summonerId"]) ##gets summonerID allows us to then fetch there past information
            accountId.append(participantIdentities[i]["player"]["accountId"]) ## gets account ID from a match
            championId.append(participant[i]["championId"])  # gets champion ID number
            #summonerRank = data["matches"][0]["participants"][0]["highestAchievedSeasonTier"] # gets the Summoner Rank

        summoner_list1 = [summonerName, summonerId, accountId, championId]
        #print(summoner_list1)

        for i in  range(0, 10):
            rankedData = requestRankedData(region, str(summonerId[i]), APIKey)
            k = 0
            isId = False
            while (isId == False  ):
                try:
                    if(int(rankedData[0]['entries'][k]['playerOrTeamId']) == summonerId[i]):
                        isId = True
                except (IndexError):
                    k += 1
                    print(k)
                    print('found an IndexError')
                    if (k >= 201):
                        isId = True
                    continue
                k += 1
                if(k >= 201):
                   isId = True
            k -= 1
            try:
             wins = rankedData[0]['entries'][k]['wins']
             losses = rankedData[0]['entries'][k]['losses']
            # print(rankedData[0]['tier'])
            # print(rankedData[0]['entries'][1]['rank'])
            except (IndexError):
                tmpString = ""
                print('found an IndexError')
                isError = True;
                continue
            win_ratio = wins / (wins + losses)
            #print("wins:" + '{:4}'.format(str(wins)) + " losses:" + '{:4}'.format(str(losses))+ " win ratio:" + str(win_ratio))
            tmpString += ('{0:.5}'.format(str(win_ratio)) + ",")
        if (isError):
            continue
        newfile.write(tmpString)

        blue_team = data["matches"][j]["teams"][0]["win"]
        result = 1 if blue_team == 'Win' else 0
        newfile.write(str(result) + "\n")

        print(j)
        number_matches += 1
        print(number_matches)
        time.sleep(1)
        if( number_matches >= 8 ):
            number_matches = 0
            time.sleep(130)

        # pprint(summoner_list1)