def read_file(file_name):
    import csv
    data = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            data.append(row)
    return data


# Report functions
#how many name in the file. output:number
def count_games(file_name):
    data = read_file(file_name)
    return len(data)


def decide(file_name, year):
    data = read_file(file_name)
    for row in data:
        if row[2] == str(year):
            return True
    return False


def get_latest(file_name):
    data = read_file(file_name)
    game_name = data[0][0]
    game_release = data[0][2]
    for row in data:
        if int(game_release) < int(row[2]):
            game_name = row[0]
            game_release = row[2]
    return game_name


def count_by_genre(file_name, genre):
    pass


def get_line_number_by_title(file_name, title):
    pass

# nice to have functions
def sort_abc(file_name):
    pass


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass
