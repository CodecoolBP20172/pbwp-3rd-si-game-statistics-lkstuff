from reports import *

FILE_NAME = "game_stat.txt"


# Export functions
export = open('export.txt', "w")
export.write(str(count_games(FILE_NAME)))
export.close()
