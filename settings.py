import json


def getAPIKey():
    with open('cassSettings.json') as settings_file:
        settings = json.load(settings_file)
    return str(settings["pipeline"]["RiotAPI"])
