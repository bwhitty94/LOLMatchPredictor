import cassiopeia as cass

cass.apply_settings("cassSettings.json")

summoner = cass.get_summoner(name="nightblue3")
id = summoner.id

print(id)

summonerPosition = cass.get_league_positions(summoner, "NA")

print(summonerPosition[0])
