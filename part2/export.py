'''
PART2
'''

from reports import *

FILE_NAME = 'game_stat.txt'

# Export functions
def write_line(file_handler, line):
    file_handler.writelines(str(line) + '\n')

export = open('export.txt', 'w')
write_line(export, get_most_played(FILE_NAME))
export.close()
