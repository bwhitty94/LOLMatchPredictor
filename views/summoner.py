from flask import Blueprint, request, jsonify, json, abort
import cassiopeia as cass
from cassiopeia import Champion
import settings
summoner_api = Blueprint('summoner_api', __name__)


@summoner_api.route("/find", methods=['GET'])
def find_summoner():
    data = request.args
    name = data['name']

    summoner = cass.get_summoner(name=name)
    blue_team = summoner.current_match.blue_team.participants

    player1 = Champion(id=blue_team[0].champion.id).name

    if not summoner.exists:
        abort(404, ["Summoner not found"])

    if not summoner.current_match.exists:
        abort(404, ["Match not found"])

    return jsonify(summoner=name, current_match_id=summoner.current_match.id, champ=player1)
