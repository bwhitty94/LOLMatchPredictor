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

def tierSwitch(argument):
    switcher = {
        "BRONZE"    : 1,
        "SILVER"    : 2,
        "GOLD"      : 3,
        "PLATINUM"  : 4,
        "DIAMOND"   : 5,
        "MASTER"    : 6,
        "CHALLENGER": 7
    }
    return switcher.get(argument, "Invalid tier")

def parseTier(rankedData, index, teamArray):
    rankModifier = 0
    tier = rankedData[0]['tier']
    rank = rankedData[0]['entries'][index]['rank']

    if (str(rank) == "I"):
        rankModifier = -1
    if (str(rank) == "V"):
        rankModifier = 1
    modefiedRank = tierSwitch(str(tier))+ rankModifier
    teamArray[modefiedRank] = teamArray[modefiedRank] + 1
    return teamArray

def win_loss_ratio(rankedData, k):
    wins = rankedData[0]['entries'][k]['wins']
    losses = rankedData[0]['entries'][k]['losses']
    return wins/(wins + losses)



with open('Data\matches1.json') as data_file:
    #matches2.json
    #
    data = json.load(data_file)
    duration = data["matches"][0]["gameDuration"]
    matches = data["matches"]
    Id = data["matches"][0]
    region = "na1"
    APIKey = "RGAPI-9433113f-5b8e-4746-9fd5-57f96570e88c"
    newfile = open("newfile.txt", "w+")

    ## Ranks
    ## [Bronze,Silver,Gold,Platinum,Diamond,Master,Challenger] = [1,2,4,8,16,32,64]
    ## The first three piece of information will go into match collection to look at the history of that person

    number_matches = 0
    for j in range(0,1):

        participantIdentities = matches[j]["participantIdentities"]
        participant = matches[j]["participants"]
        summonerName = []
        summonerId = []
        accountId = []
        championId = []

        winLossOne = ""
        winLossTwo = ""
        teamArrayOne = [0] *9
        teamArrayTwo = [0] *9

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
                if (i < 5):
                    parseTier(rankedData, i, teamArrayOne)
                    winLossOne += (str('{0:.4g}'.format(win_loss_ratio(rankedData, i))) + ", ")
                else:
                    parseTier(rankedData, i, teamArrayTwo)
                    winLossTwo += (str('{0:.4g}'.format(win_loss_ratio(rankedData, i))) + ", ")
            except (IndexError):
                print('found an IndexError')
                isError = True
                continue
        if (isError):
            continue

        tmpString = str(teamArrayOne).strip("[]") + ", "
        tmpString += winLossOne
        tmpString += str(teamArrayTwo).strip("[]") + ", "
        tmpString += winLossTwo
        newfile.write(tmpString)

        blue_team = data["matches"][j]["teams"][0]["win"]
        result = 1 if blue_team == 'Win' else 0
        newfile.write( str(result) + "\n")


        print(j)
        number_matches += 1
        print(number_matches)
        time.sleep(1)
        if( number_matches >= 8 ):
            number_matches = 0
            time.sleep(130)
