''' IPL DATA-SET-5  '''
import csv
import matplotlib.pyplot as plt


def matches_per_year(match_file):
    '''
    Calculating the total number of matches per year
    '''
    match_dict = {}
    with open(match_file, 'r', encoding='utf8') as f_m:
        match = csv.DictReader(f_m)
        for row in match:
            if row['season'] not in match_dict:
                match_dict[row['season']] = 0
            match_dict[row['season']] += 1
    number_of_matches = dict(sorted(match_dict.items(), key=lambda kv: kv[0]))
    return number_of_matches


def plotting(dict_):
    '''Plotting for the given dictionary'''
    plt.bar(dict_.keys(), dict_.values())
    plt.gcf().autofmt_xdate()
    plt.show()


def execute():
    '''Executing all the files'''
    file = 'matches.csv'
    matches = matches_per_year(file)
    plotting(matches)


execute()
