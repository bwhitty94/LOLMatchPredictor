import py_gg

def getChampWinrates():

    py_gg.init("b8a9c9f65fc6ce5cb699cc8bc82e5427")
    data = py_gg.champions.all(options = {'limit':'1000'})

    champWins = {}
    champRolls = {}

    for champ in data:
        cId = champ['championId']
        if cId in champWins.keys():
            curTot = champWins[cId] * champRolls[cId]
            champRolls[cId] = champRolls[cId] + 1
            champWins[cId] = (curTot + champ['winRate']) / champRolls[cId]
        else:
            champWins[cId] = champ['winRate']
            champRolls[cId] = 1

    return champWins