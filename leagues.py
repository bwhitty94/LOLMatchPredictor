import cassiopeia as cass
from cassiopeia.data import Queue
from cassiopeia.core import Summoner
cass.apply_settings("cassSettings.json")


def print_leagues(summoner_name: str, region: str):
    summoner = Summoner(name=summoner_name, region=region)
    leagues = summoner.leagues
    print("Listing all summoners in {leagues.fives.name}")
    for entry in leagues.fives:
        # print(entry.summoner.name, entry.wins, leagues.fives.tier, entry.division)
        win_rate = entry.wins / entry.losses
        if (summoner.name == entry.summoner.name):
            print(entry.summoner.name, win_rate, entry.wins, entry.losses)
            # entry.wins gets you what you;re looking for



    #print("Name:", summoner.name)
    #print("ID:", summoner.id)

    #positions = cass.get_league_positions(summoner, region=region)
    #positions = summoner.league_positions

    #if positions.fives.promos is not None:
        # If the summoner is in their promos, print some info
     #  print("Promos progress:", positions.fives.promos.progress)
      # print("Promos wins", positions.fives.promos.wins)
       #print("Promos losses:", positions.fives.promos.losses)
       #print("Games not yet played in promos:", positions.fives.promos.not_played)
       #print("Number of wins required to win promos:", positions.fives.promos.wins_required)
    #else:
     #    print("The summoner is not in their promos.")

    #print("Name of leagues this summoner is in:")
    #for league in positions:
    #    print(league.name)
    #print()

    # leagues = cass.get_leagues(summoner)
    leagues = summoner.leagues
    #print("Name of leagues this summoner is in (called from a different endpoint):")
    #for league in leagues:
    #    print(league.name)
    #print()

    #print()
    #print("Challenger League name:")
    #challenger = cass.get_challenger_league(queue=Queue.ranked_solo, region=region)
    #print(challenger.name)

if __name__ == "__main__":
    print_leagues("Kalturi", "NA")