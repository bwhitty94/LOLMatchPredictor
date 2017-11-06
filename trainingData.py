import json
from pprint import pprint
import matchCollection
import cassiopeia as cass
import leagues


with open('Data\matches1.json') as data_file:
    data = json.load(data_file)
    duration = data["matches"][0]["gameDuration"]
    Id = data["matches"][0]

    ## Ranks
    ## [Bronze,Silver,Gold,Platinum,Diamond,Master,Challenger] = [1,2,4,8,16,32,64]
    ## The first three piece of information will go into match collection to look at the history of that person
    participantIdentities = data["matches"][0]["participantIdentities"]
    participant = data["matches"][0]["participants"]
    summonerName = []
    summonerId = []
    accountId = []
    championId = []
    summoner_list1 = [[]]


    for i in range(0,10):
        summonerName.append(participantIdentities[i]["player"]["summonerName"]) ## gets summoner name from a match
        summonerId.append(participantIdentities[i]["player"]["summonerId"]) ##gets summonerID allows us to then fetch there past information
        accountId.append(participantIdentities[i]["player"]["accountId"]) ## gets account ID from a match
        #summonerRank = data["matches"][0]["participants"][0]["highestAchievedSeasonTier"] # gets the Summoner Rank
        championId.append(participant[i]["championId"])  # gets champion ID number
    print(summonerName)

    #
    #summoner_list1[0].append(summonerName[0])
    # summoner_list1.append(summonerId[0])
    # summoner_list1.append(accountId[0])
    # summoner_list1.append(championId[0])

    for j in range(0,0):
        for i in range(0,10):
             summoner_list1[j][i] = summonerName[i]
    #         summoner_list1[j].append(summonerId[0])
    #         summoner_list1[j].append(accountId[0])
    #         summoner_list1[j].append(championId[0])
    print(summoner_list1[0])

    #name = cass.get_summoner(name= summonerName[3])




    leagues.print_leagues(summonerName[0],"NA")
    leagues.print_leagues(summonerName[1], "NA")
    leagues.print_leagues(summonerName[2], "NA")
   # leagues.print_leagues(summonerName[3], "na1") ## I believe he does not play in NA throwing an error...
    leagues.print_leagues(summonerName[1], "NA")
    leagues.print_leagues(summonerName[1], "NA")

    # matchCollection.print_newest_match(summonerName, accountId, summonerId, "NA")
    blue_team = data["matches"][0]["teams"][0]["win"]

    if blue_team == 'Win':
        blue_team = 1
    else :
        blue_team = 0

pprint(summoner_list1)