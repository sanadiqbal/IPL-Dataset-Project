''' IPL DATASET PROBLEM-6:MATCHES WON PER TEAM PER YEAR'''
import csv
import matplotlib.pyplot as plt


def matches_won_byteam_in_season(match_file):
    '''Calculating the match won by a given team per year'''
    winner = {}
    with open(match_file, 'r', encoding='utf8') as file_:
        matches = csv.DictReader(file_)
        for match in matches:
            if match['winner'] not in winner:
                winner[match['winner']] = {}
            if match['season'] not in winner[match['winner']]:
                winner[match['winner']][match['season']] = 0
            winner[match['winner']][match['season']] += 1
    return winner


def plotting_stack_bar(winner):
    '''Plotting stacked bar for all the teams for all the years'''
    teams = list(winner)
    wins_all_teams_per_year = []
    for team in teams:
        wins_one_team_per_year = []
        for year in range(2008, 2018):
            if str(year) in winner[team]:
                wins_one_team_per_year.append(winner[team][str(year)])
            else:
                wins_one_team_per_year.append(0)
        wins_all_teams_per_year.append(wins_one_team_per_year)
    bot = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    for i, team in enumerate(teams):
        plt.bar(year,
                wins_all_teams_per_year[i],
                bottom=bot,
                label=f'{i}:{team}')
        for j in range(10):
            bot[j] = bot[j] + wins_all_teams_per_year[i][j]
    plt.xlabel('Seasons')
    plt.ylabel('Matches won per team')
    plt.title('Matches won per team per season')
    plt.legend()
    plt.show()


def execute():
    '''Executing all the files'''
    file = 'matches.csv'
    team_matches_won_season = matches_won_byteam_in_season(file)
    plotting_stack_bar(team_matches_won_season)


execute()
