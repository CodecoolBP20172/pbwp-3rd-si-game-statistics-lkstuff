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
write_line(export, sum_sold(FILE_NAME))
write_line(export, get_selling_avg(FILE_NAME))
write_line(export, count_longest_title(FILE_NAME))
write_line(export, get_date_avg(FILE_NAME))
export.close()
