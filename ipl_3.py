''''
  IPL-DATASET PROBLEM-3
'''
import csv
import matplotlib.pyplot as plt


def foreign_umpire(umpirefile):
    '''Calculating the total umpires for each country'''
    foreign_ump = {}
    with open(umpirefile, 'r', encoding='utf8') as file:
        for_emp = csv.DictReader(file)
        for umpire in for_emp:
            if umpire[' country'] != ' India':
                if umpire[' country'] not in foreign_ump:
                    foreign_ump[umpire[' country']] = 0
                foreign_ump[umpire[' country']] += 1
    return foreign_ump


def plot_bar(dict_):
    '''Plotting bar graph for dictionary'''
    plt.bar(dict_.keys(), dict_.values())
    plt.xlabel('Foreign Countries')
    plt.ylabel('Number of Umpires')
    plt.gcf().autofmt_xdate()
    plt.show()


def execute():
    '''Executing all the functions'''
    file_ = 'umpires.csv'
    ump = foreign_umpire(file_)
    plot_bar(ump)


execute()
