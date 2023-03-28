import sys

# dictionary to hold data for each player
players = {}

# read each line from standard input
# test = ['101127\t18,3,19,3', '101127\t18,3,19,3', '101127\t18,3,40,1']
# for line in test:
for line in sys.stdin:
    # split the line into player name and shot data
    player, shot_data = line.strip().split("\t")

    # split the shot data into shot distance, defender distance, shot clock, and shot result
    shot_dist, def_dist, clock, shot_result = shot_data.split(',')

    # get the current data for the player, or initialize with empty lists if not found
    current = players.get(player, [[],[],[],[]])

    # try to convert the shot data to float and int, and append to the current data for the player
    try:
        current[0].append(round(float(shot_dist), 4))
        current[1].append(round(float(def_dist), 4))
        current[2].append(round(float(clock), 4))
        current[3].append(int(shot_result))
        players[player] = current
    except ValueError:
        # if any of the conversions fail, skip the line
        pass

# loop through the players and their data, and calculate averages for each shot attribute
for player, data in sorted(players.items(), key=lambda x: x[0]):
    shot_dist_avg = round(sum(data[0]) / len(data[0]), 4)
    close_def_avg = round(sum(data[1]) / len(data[1]), 4)
    shot_clock_avg = round(sum(data[2]) / len(data[2]), 4)
    shot_rate = round(float(sum(data[3])) / len(data[3]), 4)

    # output the player name and shot averages, separated by tabs
    print("{}\t{},{},{},{}".format(player, shot_dist_avg, close_def_avg, shot_clock_avg, shot_rate))