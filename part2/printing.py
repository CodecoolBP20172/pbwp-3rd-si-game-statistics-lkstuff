'''
PART2
'''
import pprint
from reports import *

FILE_NAME = 'game_stat.txt'
pp = pprint.PrettyPrinter()


# Printing functions
pp.pprint(get_most_played(FILE_NAME))
pp.pprint(sum_sold(FILE_NAME))
