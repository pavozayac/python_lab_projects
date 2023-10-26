time_map: dict[str, list[int]] = dict()

# If the command is not any of the options, the program just asks again
cmd = input('Please input the command: a for adding an activity time, s for showing activities, t for top 3 and e for exit.\n')

while cmd != 'e':
    match cmd:
        case 'a':
            name: str = input('Activity name: ')
            try:
                time: int = int(input('Time spent: '))
            except ValueError:
                print('Time spent needs to be an integer value. \n')
                continue

            if name in time_map:
                time_map[name].append(time)
            else:
                time_map[name] = [time]
        case 's':
            for key, item in time_map.items():
                print(key + ': ' + str(item))
        case 't':
            top3 = sorted(time_map.items(),
                          key=lambda i: sum(i[1]), reverse=True)[0:3]

            for key, item in top3:
                print(key + ': ' + str(item))

    cmd = input(
        'Please input the command: a for adding an activity time, s for showing activities, t for top 3 and e for exit.\n')
