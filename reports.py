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
    pass


def get_latest(file_name):
    pass


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

    
