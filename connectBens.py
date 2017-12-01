import requests
import time
import ChampWins
import settings
import numpy
import Run_keras
from flask import Blueprint, jsonify, request
import sys

predict_api = Blueprint('predict_api', __name__)

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


@predict_api.route("/get", methods=['POST'])
def connectStuff():
    data = request.json
    print("hello")
    sys.stdout.flush()
    team = data['team']

    myTeamTest2 = [{'id': 236, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Lucian_0.jpg', 'name': 'Lucian', 'summoner': 'Angeladaddy', 'summonerId': 31493105}, {'id': 9, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Fiddlesticks_0.jpg', 'name': 'Fiddlesticks', 'summoner': 'CrAsHBiTs', 'summonerId': 22009308}, {'id': 126, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Jayce_0.jpg', 'name': 'Jayce', 'summoner': 'Ebrithalia', 'summonerId': 40069399}, {'id': 53, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Blitzcrank_0.jpg', 'name': 'Blitzcrank', 'summoner': 'langtreezy', 'summonerId': 32422003}, {'id': 28, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Evelynn_0.jpg', 'name': 'Evelynn', 'summoner': 'ThePerfectBronze', 'summonerId': 66359111}, {'id': 127, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Lissandra_0.jpg', 'name': 'Lissandra', 'summoner': 'RuPaulogize', 'summonerId': 31660209}, {'id': 114, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Fiora_0.jpg', 'name': 'Fiora', 'summoner': 'Aneur', 'summonerId': 20298222}, {'id': 99, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Lux_0.jpg', 'name': 'Lux', 'summoner': 'The Buk Lau', 'summonerId': 21556685}, {'id': 15, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Sivir_0.jpg', 'name': 'Sivir', 'summoner': 'Nuhthane', 'summonerId': 22289695}, {'id': 43, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Karma_0.jpg', 'name': 'Karma', 'summoner': 'LuckyClicker', 'summonerId': 27352036}]

    print("what is this bullshit?")
    print(team == myTeamTest2)

    print(team)
    print(myTeamTest2)

    team = myTeamTest2

    summonerId = []
    championId = []
    winLossOne = ""
    winLossTwo = ""
    teamArrayOne = [0] * 9
    teamArrayTwo = [0] * 9

    #this is the format of whats coming in "team"
    #champions.append({"summoner": participant.summoner.name, "id": champ.id, "name": champ.name, "imageUrl": image})
    for e in range(0,10):
        print(team[e]["summonerId"])
        summonerId.append(team[e]["summonerId"])
        championId.append(team[e]["id"])
    region = "na1"
    APIKey = "RGAPI-5082f84e-572a-4fe0-8312-ea61e69bac22"
    currentmatchfile = open("currentmatchfile.txt", "w+")
    number_matches = 0

    champWins = ChampWins.getChampWinrates()
    champ_winrate = []
    for j in range(0,1):

        tmpString = ""
        isError = False


        for i in  range(0, 10):
            rankedData = requestRankedData(region, str(summonerId[i]), APIKey)
            k = 0
            isId = False
            champ_winrate.append(champWins[championId[i]])
            while (isId == False  ):
                try:
                    # print("test: " + str(rankedData[0]['entries'][k]['playerOrTeamId']) + " - " + str(summonerId[i]))
                    if(int(rankedData[0]['entries'][k]['playerOrTeamId']) == int(summonerId[i])):
                        isId = True
                except (IndexError):
                    k += 1
                    # print("" + str(k) + " - found an indexError" + str(rankedData[0]))
                    print(i)
                    # print('found an IndexError')
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
                tmpString = ""
                print('found an IndexError')
                isError = True
                continue
            #win_ratio = wins / (wins + losses)
            #print("wins:" + '{:4}'.format(str(wins)) + " losses:" + '{:4}'.format(str(losses))+ " win ratio:" + str(win_ratio))
            #print("Tier:" + '{:5}'.format(str(tier)) + " Rank:" + '{:5}'.format(str(rank)))
            #tmpString += ('{0:.6}'.format(str(win_ratio)) + ",")

        # if (isError):
        #     continue

        tmpString = str(teamArrayOne).strip("[]") + ", "
        tmpString += winLossOne
        tmpString += str(champ_winrate[0:5]).strip("[]") + ", "
        tmpString += str(teamArrayTwo).strip("[]") + ", "
        tmpString += winLossTwo
        tmpString += str(champ_winrate[5:10]).strip("[]")
        currentmatchfile.write(tmpString)
        currentmatchfile.flush()

        number_matches += 1
        print("We went through the list of players Ben!: Successful Exit")
        thing = numpy.loadtxt("currentmatchfile.txt",delimiter =",")
        thing_2= thing[0:38]

        # return Run_keras.predictMatch(thing_2)
        # return jsonify(value=Run_keras.predictMatch(thing_2))
        return jsonify(value=1)




if __name__ == "__main__":
    #[['TastyKakeKing2', 'xouchiesssx', 'hautala147', 'xPÃ\xadnny', 'McLovin1500', 'CypherNek', 'Ã?eath MÃ£rk',
    #  'Monkeyfightr', 'JasonXD', 'xoMajesty'],
    # [57005769, 19592759, 23035037, 38804535, 34202044, 36041723, 87822154, 30942910, 22668710, 32333042],
    # [218739531, 32286644, 36991143, 201694529, 48591434, 50650413, 239003617, 43053794, 36542700, 47191301],
    # [240, 29, 63, 64, 1, 24, 238, 432, 51, 17]]
    # champions.append({"summoner": participant.summoner.name, "id": champ.id, "name": champ.name, "imageUrl": image})
    myTeamTest = []
    myTeamTest.append({"summoner": "TastyKakeKing2", "id": 240, "name": "NoClue1","imageUrl": "image1", "summonerId": "57005769" })
    myTeamTest.append({"summoner": "xouchiesssx", "id": 29, "name": "NoClue2","imageUrl": "image2", "summonerId": "19592759"})
    myTeamTest.append({"summoner": "hautala147", "id": 63, "name": "NoClue3", "imageUrl": "image34", "summonerId": "23035037"})
    myTeamTest.append({"summoner": "McLovin1500", "id": 1, "name": "NoClue4", "imageUrl": "image4", "summonerId": "34202044"})
    myTeamTest.append({"summoner": "CypherNek", "id": 24, "name": "NoClue5", "imageUrl": "image5", "summonerId": "36041723"})
    myTeamTest.append({"summoner": "TastyKakeKing2", "id": 240, "name": "NoClue1", "imageUrl": "image1", "summonerId": "57005769"})
    myTeamTest.append({"summoner": "xouchiesssx", "id": 29, "name": "NoClue2", "imageUrl": "image2", "summonerId": "19592759"})
    myTeamTest.append({"summoner": "hautala147", "id": 63, "name": "NoClue3", "imageUrl": "image34", "summonerId": "23035037"})
    myTeamTest.append({"summoner": "McLovin1500", "id": 1, "name": "NoClue4", "imageUrl": "image4", "summonerId": "34202044"})
    myTeamTest.append({"summoner": "CypherNek", "id": 24, "name": "NoClue5", "imageUrl": "image5", "summonerId": "36041723"})

    myTeamTest2 = [{'id': 203, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Kindred_0.jpg', 'name': 'Kindred', 'summoner': 'Choerry', 'summonerId': 22042123}, {'id': 57, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Maokai_0.jpg', 'name': 'Maokai', 'summoner': 'Protechi', 'summonerId': 22687570}, {'id': 43, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Karma_0.jpg', 'name': 'Karma', 'summoner': 'GaoGao', 'summonerId': 22946266}, {'id': 22, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Ashe_0.jpg', 'name': 'Ashe', 'summoner': 'emeliorate', 'summonerId': 86409325}, {'id': 90, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Malzahar_0.jpg', 'name': 'Malzahar', 'summoner': 'OneseIf', 'summonerId': 170340}, {'id': 101, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Xerath_0.jpg', 'name': 'Xerath', 'summoner': 'Fockus', 'summonerId': 22787428}, {'id': 201, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Braum_0.jpg', 'name': 'Braum', 'summoner': 'LEE SlN BAYBEE', 'summonerId': 23162732}, {'id': 68, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Rumble_0.jpg', 'name': 'Rumble', 'summoner': 'Mysterìous', 'summonerId': 39877298}, {'id': 104, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Graves_0.jpg', 'name': 'Graves', 'summoner': 'godrjsdnd', 'summonerId': 52316360}, {'id': 119, 'imageUrl': 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Draven_0.jpg', 'name': 'Draven', 'summoner': 'ArrSEA', 'summonerId': 28949426}]


    print(myTeamTest2)
    Run_keras.buildModel()
    print(connectStuff(myTeamTest))
