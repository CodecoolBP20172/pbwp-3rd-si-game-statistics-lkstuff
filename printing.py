import pprint
from reports import *

FILE_NAME = "game_stat.txt"
pp = pprint.PrettyPrinter()


# Printing functions
pp.pprint(count_games(FILE_NAME))
pp.pprint(decide(FILE_NAME, 2004))
pp.pprint(get_latest(FILE_NAME))
