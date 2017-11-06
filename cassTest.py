import cassiopeia as cass
import random
from cassiopeia.core import Summoner, MatchHistory, Match

cass.apply_settings("cassSettings.json")


def test():
    print("hey")
    summoner = cass.get_summoner(name="xbenny") #beastmodekg is another account
    print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                              level=summoner.level,
                                                                              region=summoner.region))

    champions = cass.get_champions()
    random_champion = random.choice(champions)

    print("He enjoys playing champions such as {name}.".format(name=random_champion.name))


    return
