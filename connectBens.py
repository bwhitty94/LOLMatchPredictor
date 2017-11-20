import requests
import time

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v3/leagues/by-summoner/" + ID + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def connectStuff(team):
    summonerId = []
    #this is the format of whats coming in "team"
    #champions.append({"summoner": participant.summoner.name, "id": champ.id, "name": champ.name, "imageUrl": image})
    for e in range(0,10):
        summonerId.append(team[e]["summonerId"])
    region = "na1"
    APIKey = "RGAPI-7d5fb1a7-399c-4289-9801-54d1dde10d3e"
    currentmatchfile = open("currentmatchfile.txt", "w+")
    number_matches = 0


    for j in range(0,1):

        tmpString = ""
        isError = False

        for i in  range(0, 10):
            rankedData = requestRankedData(region, str(summonerId[i]), APIKey)
            k = 0
            isId = False
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
             wins = rankedData[0]['entries'][k]['wins']
             losses = rankedData[0]['entries'][k]['losses']
             #tier = rankedData[0]['tier']
             #rank = rankedData[0]['entries'][k]['rank']
            except (IndexError):
                tmpString = ""
                print('found an IndexError')
                isError = True;
                continue
            win_ratio = wins / (wins + losses)
            print("wins:" + '{:4}'.format(str(wins)) + " losses:" + '{:4}'.format(str(losses))+ " win ratio:" + str(win_ratio))
            #print("Tier:" + '{:5}'.format(str(tier)) + " Rank:" + '{:5}'.format(str(rank)))
            tmpString += ('{0:.6}'.format(str(win_ratio)) + ",")

        if (isError):
            continue
        currentmatchfile.write(tmpString)
        print(tmpString)

        number_matches += 1
        print("We went through the first five players Ben: Successful Exit")
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