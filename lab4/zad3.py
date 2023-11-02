import argparse
import os
import pathlib
import csv
import random

parser = argparse.ArgumentParser()
parser.add_argument('-m', type=str, nargs='+', help='months names')
parser.add_argument('-d', type=str, nargs='+', help='ranges of days from the set {mon, tue, wed, thu, fri, sat, sun} in the form (e.g.) mon or mon-tue')

# I assumed that since the description of the task states that we are to create
# two subfolders 'morning' and 'evening' every time, the information about
# the time of  day becomes obsolete
# parser.add_argument(
#    '-t', type=str, default=10, nargs='+', help='times of day to combine'
# )

args = parser.parse_args()

def write_morning_evening(month: str, day: str):
    header = ['Model', 'Output value', 'Time of computation']

    for daytime in ['morning', 'evening']:
        filepath = pathlib.Path(os.getcwd(), month, day, daytime)

        try:
            filepath.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print(f'Path {filepath.name} already exists.')
            return
            

        with open(filepath.joinpath('Solutions.csv'), 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')

            writer.writerow(header)

            model = ['A', 'B', 'C'][random.randint(0, 2)]
            output = random.randint(0, 1000)
            time = f'{random.randint(0, 1000)}s'

            writer.writerow([model, output, time])

def make_combinations(months, days):
    if months is None:
        print('At least one month is required.')
        return

    if days is None:
        print('At least one day is required.')
        return

    if len(months) != len(days):
        print('The number of parameters describing days and months must be equal.')

    else:
        day_num = {
            'mon': 0,
            'tue': 1,
            'wed': 2,
            'thu': 3,
            'fri': 4,
            'sat': 5,
            'sun': 6,
        }

        dlist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        for i, month in enumerate(months):
            daystring: str = days[i]

            first, *second = daystring.split('-')

            if len(second) < 1:
                write_morning_evening(month, dlist[day_num[first]])

            else:
                for day in dlist[day_num[first]:day_num[second[0]]+1]:
                    write_morning_evening(month, day)

if __name__ == '__main__':
    make_combinations(args.m, args.d)