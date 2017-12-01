import requests

champion_list = None


def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()


def findCurrentGame(region, summonerId, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + summonerId + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()


def get_champ_key(champId):
    for key, value in champion_list.items():
        if value['id'] == champId:
            return key
    return None


def get_champ_name(champKey):
    return champion_list[champKey]['name']


def get_champ_image(champKey):
    image_base_url = "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/"
    return image_base_url + champKey + "_0.jpg"


def get_champ_list(region, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/static-data/v3/champions?locale=en_US&dataById=false&api_key=" \
          + APIKey
    global champion_list
    response = (requests.get(URL)).json()
    champion_list = response['data']


def create_teams(participants):
    blue_team = []
    red_team = []

    for p in participants:
        champId = p['championId']
        champKey = get_champ_key(champId)

        if p['teamId'] == 100:
            blue_team.append({"summoner": p['summonerName'], "id": champId, "name": get_champ_name(champKey),
                              "imageUrl": get_champ_image(champKey), "summonerId": p['summonerId']})
        else:
            red_team.append({"summoner": p['summonerName'], "id": champId, "name": get_champ_name(champKey),
                              "imageUrl": get_champ_image(champKey), "summonerId": p['summonerId']})

    return blue_team + red_team


def get_teams(region, name, APIKey):
    summoner = requestSummonerData(region, name, APIKey)
    game = findCurrentGame(region, str(summoner['id']), APIKey)
    get_champ_list(region, APIKey)
    teams = create_teams(game['participants'])

    return teams
