from flask import Blueprint, request, jsonify, json, abort
import cassTest
summoner_api = Blueprint('summoner_api', __name__)


@summoner_api.route("/find", methods=['GET'])
def find_summoner():
    data = request.args
    name = data['name']
    print(name)
    cassTest.test()
    return name