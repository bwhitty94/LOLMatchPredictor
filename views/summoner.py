from flask import Blueprint, request, jsonify, json, abort
import cassiopeia as cass
from cassiopeia import Champion

summoner_api = Blueprint('summoner_api', __name__)


@summoner_api.route("/find", methods=['GET'])
def find_summoner():
    data = request.args
    name = data['name']

    summoner = cass.get_summoner(name=name)
    blue_team = get_champions(summoner.current_match.blue_team.participants)
    red_team = get_champions(summoner.current_match.red_team.participants)


    # blueChamps = get_champions(blue_team)
    # red_champs = get_champions(red_team)

    if not summoner.exists:
        abort(404, ["Summoner not found"])

    if not summoner.current_match.exists:
        abort(404, ["Match not found"])

    return jsonify(summoner=name, currentMatchId=summoner.current_match.id, blueTeam=blue_team, redTeam=red_team)


# return a list of Champion objects from a list of participants (team)
def get_champions(team):
    champions = []
    image_base_url = "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/"

    for participant in team:
        champ = Champion(id=participant.champion.id)
        image = image_base_url + champ.image.full.split(".")[0] + "_0.jpg"

        champions.append({"summoner": participant.summoner.name, "id": champ.id, "name": champ.name, "imageUrl": image})

        print(champ.image)

    return champions
