import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', type=str, nargs='+', help='nazwy miesięcy')
parser.add_argument('-d', type=str, nargs='+', help='zakresy dni ze zbioru {pn, wt, śr, czw, pt, sb, nd} w postaci (np.) pn lub pn-wt')
parser.add_argument(
   '-t', type=str, default=10, nargs='+', help='pory dnia do skombinowania'
)

args = parser.parse_args()

def make_combinations(months, days, times):
    if months is None:
        print('Należy wprowadzić przynajmniej jeden miesiąc.')
        return

    if days is None:
        print('Należy wprowadzić przynajmniej jeden dzień.')
        return

    if times is None:
        times = []

    if len(months) != len(days):
        print('Liczba parametrów miesięcy i zakresów dni musi być równa.')

    else:
        day_num = {
            'pn': 0,
            'wt': 1,
            'śr': 2,
            'czw': 3,
            'pt': 4,
            'sb': 5,
            'nd': 6,
        }
        dlist = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
        timecount = 0

        for i, month in enumerate(months):
            daystring: str = days[i]

            first, *second = daystring.split('-')

            if len(second) < 1:
                time = 'r' if timecount >= len(times) else times[timecount]
                time = 'rano' if time == 'r' else 'wieczorem'

                print(f'{month} {dlist[day_num[first]]} {time}')

                timecount += 1
            else:
                for i in dlist[day_num[first]:day_num[second[0]]+1]:
                    time = 'r' if timecount >= len(times) else times[timecount]
                    time = 'rano' if time == 'r' else 'wieczorem'

                    print(f'{month} {i} {time}')

                    timecount += 1

make_combinations(args.m, args.d, args.t)