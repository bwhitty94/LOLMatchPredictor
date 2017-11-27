import requests
import time
import ChampWins


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

def connectStuff(team):
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
    region = "na1"
    APIKey = "RGAPI-1ca7f033-2221-4f4f-ab5a-52c389340ec4"
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
                    if(int(rankedData[0]['entries'][k]['playerOrTeamId']) == int(summonerId[i])):
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
                tmpString = ""
                print('found an IndexError')
                isError = True
                continue
            #win_ratio = wins / (wins + losses)
            #print("wins:" + '{:4}'.format(str(wins)) + " losses:" + '{:4}'.format(str(losses))+ " win ratio:" + str(win_ratio))
            #print("Tier:" + '{:5}'.format(str(tier)) + " Rank:" + '{:5}'.format(str(rank)))
            #tmpString += ('{0:.6}'.format(str(win_ratio)) + ",")

        if (isError):
            continue

        tmpString = str(teamArrayOne).strip("[]") + ", "
        tmpString += winLossOne
        tmpString += str(champ_winrate[0:5]).strip("[]") + ", "
        tmpString += str(teamArrayTwo).strip("[]") + ", "
        tmpString += winLossTwo
        tmpString += str(champ_winrate[5:10]).strip("[]") + ", "
        currentmatchfile.write(tmpString)


        number_matches += 1
        print("We went through the list of players Ben!: Successful Exit")
        time.sleep(2)


 # keep this in incase you want to change this function
        if( number_matches >= 8 ):
            number_matches = 0
            time.sleep(130)

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
    print(myTeamTest)
    connectStuff(myTeamTest)