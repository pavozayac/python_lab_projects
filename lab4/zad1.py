def generuj(months: list[str], days: list[str], times: list[str]=[]):
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

if __name__ == '__main__':
    generuj(['styczeń', 'luty'], ['pn-wt', 'pt'], ['r', 'w'])