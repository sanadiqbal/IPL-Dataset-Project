'''
    IPL-DATASET PROBLEM-7
'''
import csv
import matplotlib.pyplot as plt


def extra_run_per_team_2016(match_file, deliveries_file):
    '''
    Calculating extra runs conceded by each team in 2016
    '''
    match_2016 = []
    extra_run = {}
    with open(match_file, 'r', encoding='utf8') as file1:
        matches = csv.DictReader(file1)
        for match in matches:
            if match['season'] == '2016':
                match_2016.append(match['id'])
    with open(deliveries_file, 'r', encoding='utf8') as file2:
        deliveries = csv.DictReader(file2)
        for delivery in deliveries:
            if delivery['match_id'] in match_2016:
                if delivery['bowling_team'] not in extra_run:
                    extra_run[delivery['bowling_team']] = 0
                extra_run[delivery['bowling_team']] += int(
                    delivery['extra_runs'])

    return extra_run


def plot_bar_graph(dict_):
    '''
    Plotting the bar graph for the given dictionary
    '''

    plt.bar(dict_.keys(), dict_.values())
    plt.xlabel('Teams')
    plt.ylabel('Extra runs conceded in 2016')
    plt.gcf().autofmt_xdate()
    plt.show()


MATCHES_FILE = 'matches.csv'
DELIVERIES_FILE = 'deliveries.csv'
extra_run_values = extra_run_per_team_2016(MATCHES_FILE, DELIVERIES_FILE)
plot_bar_graph(extra_run_values)
