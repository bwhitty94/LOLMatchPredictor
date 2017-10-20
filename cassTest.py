import cassiopeia as cass
import random

cass.apply_settings("cassSettings.json")


def test():
    print("hey")
    summoner = cass.get_summoner(name="xbenny")
    print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                              level=summoner.level,
                                                                              region=summoner.region))

    champions = cass.get_champions()
    random_champion = random.choice(champions)
    #history = cass.get_match_history(summoner,"north_america",0)
    print("He enjoys playing champions such as {name}.".format(name=random_champion.name))

    return
