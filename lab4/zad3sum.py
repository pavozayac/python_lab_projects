import csv
import pathlib
import os

def sum() -> int:
    sum = 0
    
    current = pathlib.Path(os.getcwd())

    for file in current.glob('*/*/*/Solutions.csv'):
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            
            for line in reader:
                if line[0] == 'A':
                    sum += int(line[2][:-1])

    return sum

if __name__ == '__main__':
    print(sum())
