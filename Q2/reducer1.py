#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
players = {}

# Testing code
# test = ['101127\t18,3,19,3', '101127\t18,3,19,3', '101127\t18,3,40,1']
# for line in test:
for line in sys.stdin:
    player, shot_data = line.strip().split("\t")
    shot_dist, def_dist, clock, shot_result = shot_data.split(',')
    current = players.get(player, [[],[],[],[]])
    try:
        # Appending all found data (and rounding) for each player
        current[0].append(round(float(shot_dist), 4))
        current[1].append(round(float(def_dist), 4))
        current[2].append(round(float(clock), 4))
        current[3].append(int(shot_result))
        players[player] = current
    except ValueError:
        pass

# Generating averages for each bucket and final reducing
for player, data in sorted(players.items(), key=lambda x: x[0]):
    shot_dist_avg = round(sum(data[0]) / len(data[0]), 4)
    close_def_avg = round(sum(data[1]) / len(data[1]), 4)
    shot_clock_avg = round(sum(data[2]) / len(data[2]), 4)
    shot_rate = round(float(sum(data[3])) / len(data[3]), 4)
    print("{}\t{},{},{},{}".format(player, shot_dist_avg, close_def_avg, shot_clock_avg, shot_rate))
