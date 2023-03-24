''' IPL DATASET PROBLEM-4 : STACKED BAR CHART OF MATCHES PLAYED BY TEAM PER SEASON'''
import csv
import matplotlib.pyplot as plt


def matches_played_per_team_year(matches_file):
    '''Calculating matches played by each team per season'''
    match_team_season = {}
    with open(matches_file, 'r', encoding='utf8') as file_:
        matches = csv.DictReader(file_)
        for match in matches:
            if match['team1'] not in match_team_season:
                match_team_season[match['team1']] = {}
            if match['team2'] not in match_team_season:
                match_team_season[match['team2']] = {}
            if match['season'] not in match_team_season[match['team1']]:
                match_team_season[match['team1']][match['season']] = 0
            if match['season'] not in match_team_season[match['team2']]:
                match_team_season[match['team2']][match['season']] = 0
            match_team_season[match['team1']][match['season']] += 1
            match_team_season[match['team2']][match['season']] += 1
    return match_team_season


def plotting_stacked_bar(dict_):
    '''Plotting stacked bar chart of matches played by each team per season'''
    teams = list(dict_)
    match_all_team_year = []
    for team in teams:
        match_each_team_year = []
        for year in range(2008, 2018):
            if str(year) in dict_[team]:
                match_each_team_year.append(dict_[team][str(year)])
            else:
                match_each_team_year.append(0)
        match_all_team_year.append(match_each_team_year)
    year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    bot = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, team in enumerate(teams):
        plt.bar(year, match_all_team_year[i], bottom=bot, label=f'{i}:{team}')
        for j in range(10):
            bot[j] = bot[j] + match_all_team_year[i][j]
    plt.xlabel('Seasons')
    plt.ylabel('Matches played by each teams')
    plt.title('Matches played by each team per season')
    plt.legend()
    plt.show()


def execute():
    '''Executing all the files'''
    file = 'matches.csv'
    match_team_year = matches_played_per_team_year(file)
    plotting_stacked_bar(match_team_year)


execute()
