import cassiopeia as cass
#http://cassiopeia.readthedocs.io/en/latest/
from cassiopeia import Summoner

#already set API key in config file
cass.set_default_region("NA")

will = Summoner(name = "lordironwilliam")
print(will.region)