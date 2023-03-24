'''
    IPL DATASET PROBLEM-8
'''
import csv
import itertools
import matplotlib.pyplot as plt


def economical_bowlers(match_file, d_f):
    '''Getting top 10 economical bowlers in 2015'''
    bowler = {}
    match_list = []
    with open(match_file, 'r', encoding='utf8') as f_m:
        matches = csv.DictReader(f_m)
        for match in matches:
            if match['season'] == '2015':
                match_list.append(match['id'])
    with open(d_f, 'r', encoding='utf8') as f_d:
        deliveries = csv.DictReader(f_d)
        for delivery in deliveries:
            if delivery['match_id'] in match_list:
                if delivery['bowler'] not in bowler:
                    bowler[delivery['bowler']] = 0
                bowler[delivery['bowler']] += int(
                    delivery['total_runs']) - int(delivery['bye_runs']) - int(
                        delivery['legbye_runs'])
    sorted_bowler = dict(sorted(bowler.items(), key=lambda kv: kv[1]))
    top10_econ_bowler = dict(itertools.islice(sorted_bowler.items(), 10))
    return top10_econ_bowler


def plot_bar(dict_):
    '''Plotting bar chart of given dictionary'''
    plt.bar(dict_.keys(), dict_.values())
    plt.xlabel('Top 10 economic bowlers in 2015')
    plt.ylabel('Economy')
    plt.gcf().autofmt_xdate()
    plt.show()


def execute():
    '''Executing all the files'''
    mfile = 'matches.csv'
    dfile = 'deliveries.csv'
    top_10_econ_bowl = economical_bowlers(mfile, dfile)
    plot_bar(top_10_econ_bowl)


execute()
