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

def connectStuff(name: str , region: str):
    #region = "na1"
    APIKey = "RGAPI-02519475-aee0-4911-be95-d69941921f3a"
    newfile = open("newfile.txt", "w+")
    number_matches = 0
    summoner = requestSummonerData(region, str(name), APIKey)
    print(summoner)

    for j in range(0,1):

        summonerName = []
        summonerId = []
        accountId = []
        championId = []
        tmpString = ""
        isError = False

        #for i in range(0,10):
           #summonerName.append(summ) ## gets summoner name from a match
           #summonerId.append(participantIdentities[i]["player"]["summonerId"]) ##gets summonerID allows us to then fetch there past information
           #accountId.append(participantIdentities[i]["player"]["accountId"]) ## gets account ID from a match
           #championId.append(participant[i]["championId"])  # gets champion ID number
           #summonerRank = data["matches"][0]["participants"][0]["highestAchievedSeasonTier"] # gets the Summoner Rank

        summonerId = summoner["id"]
        #print(summoner_list1)

        for i in  range(0, 1):
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
             #wins = rankedData[0]['entries'][k]['wins']
             #losses = rankedData[0]['entries'][k]['losses']
             tier = rankedData[0]['tier']
             rank = rankedData[0]['entries'][k]['rank']
            except (IndexError):
                tmpString = ""
                print('found an IndexError')
                isError = True;
                continue
            #win_ratio = wins / (wins + losses)
            #print("wins:" + '{:4}'.format(str(wins)) + " losses:" + '{:4}'.format(str(losses))+ " win ratio:" + str(win_ratio))

            print("Tier:" + '{:5}'.format(str(tier)) + " Rank:" + '{:5}'.format(str(rank)))
            tmpString += ('{0:.6}'.format(str(tier)) + ",")

        if (isError):
            continue
        newfile.write(tmpString)
        print(tmpString)


        blue_team = data["matches"][j]["teams"][0]["win"]
        result = 1 if blue_team == 'Win' else 0
        newfile.write(str(result) + "\n")


        print(j)
        number_matches += 1
        print(number_matches)
        time.sleep(2)
        if( number_matches >= 8 ):
            number_matches = 0
            time.sleep(130)


if __name__ == "__main__":
    connectStuff("Kalturi", "na1")