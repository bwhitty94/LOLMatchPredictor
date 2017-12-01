from flask import Blueprint, jsonify, request
from predictionData import generate_prediction
from pastGames import game1, game2, game3

predict_api = Blueprint('predict_api', __name__)


@predict_api.route("/get", methods=["POST"])
def get_prediction():
    data = request.json
    team = data['team']

    predict = generate_prediction(team)
    return jsonify(value=predict)


@predict_api.route("/past", methods=["POST"])
def get_past_prediction():
    data = request.json
    game_num = int(data['gameNum'])


    team = game3

    if game_num == 1:
        team = game1
    elif game_num == 2:
        team = game2

    predict = generate_prediction(team)
    return jsonify(blueTeam=team[0:5], redTeam=team[5:10], value=predict)
