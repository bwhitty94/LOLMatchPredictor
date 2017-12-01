from flask import Blueprint, request, jsonify
from summonerTeam import get_teams
from APIKey import APIKey, region


summoner_api = Blueprint('summoner_api', __name__)


@summoner_api.route("/find", methods=['GET'])
def get_summoner():
    try:
        data = request.args
        name = data['name']
        teams = get_teams(region, name, APIKey)

        return jsonify(blueTeam=teams[0:5], redTeam=teams[5:10])

    except KeyError as e:
        cause = e.args[0]

        if cause == 'id':
            error = "Summoner " + name + " not found!"
        elif cause == 'participants':
            error = "Summoner is not currently in a match!"
        else:
            error = "idk"
            print("cause:")
            print(cause)

        return jsonify(error=error)