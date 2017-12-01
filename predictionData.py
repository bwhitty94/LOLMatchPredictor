import requests
import ChampWins
import numpy
import Run_keras
from flask import Blueprint
from APIKey import APIKey, region

predict_api = Blueprint('predict_api', __name__)


def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v3/positions/by-summoner/" + ID + "?api_key=" + APIKey
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


def parseTier(rankedData, teamArray):
    rankModifier = 0

    if rankedData:
        tier = rankedData[0].get('tier', 'SILVER')
        rank = rankedData[0].get('rank', 'V')
    else:
        tier = "SILVER"
        rank = "V"

    if str(rank) == "I":
        rankModifier = -1
    if str(rank) == "V":
        rankModifier = 1
    modefiedRank = tierSwitch(str(tier))+ rankModifier
    teamArray[modefiedRank] = teamArray[modefiedRank] + 1
    return teamArray


def win_loss_ratio(rankedData):
    if rankedData:
        wins = rankedData[0].get('wins', 1)
        losses = rankedData[0].get('losses', 1)
    else:
        wins = 1
        losses = 1

    return wins/(wins + losses)


def generate_prediction(team):
    print(team)

    summonerId = []
    championId = []
    winLossOne = ""
    winLossTwo = ""
    teamArrayOne = [0] * 9
    teamArrayTwo = [0] * 9

    #this is the format of whats coming in "team"
    #champions.append({"summoner": participant.summoner.name, "id": champ.id, "name": champ.name, "imageUrl": image})
    for e in range(0,10):
        summonerId.append(team[e]["summonerId"])
        championId.append(team[e]["id"])

    currentmatchfile = open("currentmatchfile.txt", "w+")
    number_matches = 0

    champWins = ChampWins.getChampWinrates()
    champ_winrate = []
    for j in range(0,1):
        isError = False

        for i in range(0, 10):
            rankedData = requestRankedData(region, str(summonerId[i]), APIKey)
            champ_winrate.append(champWins[championId[i]])

            try:
                if i < 5:
                    parseTier(rankedData, teamArrayOne)
                    winLossOne += (str('{0:.4g}'.format(win_loss_ratio(rankedData))) + ", ")
                else:
                    parseTier(rankedData, teamArrayTwo)
                    winLossTwo += (str('{0:.4g}'.format(win_loss_ratio(rankedData))) + ", ")
            except (IndexError):
                print('found an IndexError')
                isError = True
                continue
        if (isError):
            continue

        tmpString = str(teamArrayOne).strip("[]") + ", "
        tmpString += winLossOne
        tmpString += str(champ_winrate[0:5]).strip("[]") + ", "
        tmpString += str(teamArrayTwo).strip("[]") + ", "
        tmpString += winLossTwo
        tmpString += str(champ_winrate[5:10]).strip("[]")
        currentmatchfile.write(tmpString)
        currentmatchfile.flush()

        number_matches += 1
        thing = numpy.loadtxt("currentmatchfile.txt",delimiter =",")
        thing_2= thing[0:38]

        return Run_keras.predictMatch(thing_2)
