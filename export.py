from reports import *

FILE_NAME = "game_stat.txt"


# Export functions
def write_line(file_handler, line):
    file_handler.writelines(str(line) + "\n")


export = open('export.txt', "w")
write_line(export, count_games(FILE_NAME))
write_line(export, decide(FILE_NAME, 2004))
export.close()
