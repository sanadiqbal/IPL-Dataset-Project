'''
    IPL DATASET PROBLEM-1
'''

import csv
import matplotlib.pyplot as plt


def total_run_scored(deliveries_file):
    '''
    Calculating total runs scored by each team
    '''
    run_by_team = {}
    with open(deliveries_file, 'r', encoding='utf8') as file:
        deliveries = csv.DictReader(file)
        for delivery in deliveries:
            if delivery['batting_team'] not in run_by_team:
                run_by_team[delivery['batting_team']] = 0
            run_by_team[delivery['batting_team']] += int(
                delivery['total_runs'])
    return run_by_team


def plotting_graph(dict_):
    '''Plotting the graph for given dictionary'''
    plt.plot(dict_.keys(), dict_.values(), marker='o')
    plt.xlabel('IPL Teams')
    plt.ylabel('Total runs scored')
    plt.gcf().autofmt_xdate()
    plt.show()


def execute():
    '''Execute all the files'''
    d_f = 'deliveries.csv'
    team_runs = total_run_scored(d_f)
    plotting_graph(team_runs)


execute()
