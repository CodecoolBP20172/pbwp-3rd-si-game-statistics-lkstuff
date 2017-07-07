'''
PART2
'''


def read_file(file_name):
    import csv
    data = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            data.append(row)
    return data


# 1  What is the title of the most played game (i.e. sold the most copies)?
def get_most_played(file_name):
        data = read_file(file_name)
        game_name = data[0][0]
        game_sold = data[0][1]
        for row in data:
            if int(game_sold) < int(float(row[1])):
                game_name = row[0]
                game_sold = row[1]
        return game_name



# 2 How many copies have been sold total?
def sum_sold(file_name):
    data = read_file(file_name)
    pass


# 3 What is the average selling?
def  get_selling_avg(file_name):
    data = read_file(file_name)
    pass


# 4 How many characters long is the longest title?
def count_longest_title(file_name):
    data = read_file(file_name)
    pass


# 5 What is the average of the release dates?
def get_date_avg(file_name):
    data = read_file(file_name)
    pass


# 6 What properties has a game?
def get_game(file_name, title):
    data = read_file(file_name)
    pass


# nice to have
# 1 How many games are there grouped by genre?
def  count_grouped_by_genre(file_name):
    data = read_file(file_name)
    pass


# 2 What is the date ordered list of the games?
def get_date_ordered(file_name):
    data = read_file(file_name)
    pass
