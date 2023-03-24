'''
    IPL-DATASET PROBLEM-2
'''
import csv
import itertools
import matplotlib.pyplot as plt


def top_rcb_batsmen(file):
    '''Getting top rcb batsmen'''
    plyr = {}
    with open(file, 'r', encoding='utf8') as file_delivery:
        deliveries = csv.DictReader(file_delivery)
        for delivery in deliveries:
            if delivery['batting_team'] == 'Royal Challengers Bangalore':
                if delivery['batsman'] not in plyr:
                    plyr[delivery['batsman']] = 0
                plyr[delivery['batsman']] += int(delivery['total_runs'])
    sorted_plyr = dict(sorted(plyr.items(), key=lambda x: x[1], reverse=True))
    players = dict(itertools.islice(sorted_plyr.items(), 10))
    return players


def plotting_bar_graph(dict_):
    '''Plotting bar graph for givrn dictionary'''
    plt.bar(dict_.keys(), dict_.values())
    plt.xlabel('Top 10 RCB batsmen')
    plt.ylabel('Runs scored')
    plt.gcf().autofmt_xdate()
    plt.show()


def execute():
    '''Executing all the functions'''
    d_f = 'deliveries.csv'
    rcb_batsmen = dict(top_rcb_batsmen(d_f))
    plotting_bar_graph(rcb_batsmen)


execute()
