#!/usr/bin/env python

import sys
from collections import defaultdict

# Set up empty dictionary to hold player data
player_data = defaultdict(int)

# Read through each line of input
for line in (1,3,4):
    n = 0
    while (n < 11):
        print('test', 'test')
        n += 1



    # Split line into components
#     player, shot_dist, def_dist, shot_clock, shots_made, total_shots = line.strip().split('\t')
    
#     # Convert values to integers
#     shot_dist = int(shot_dist)
#     def_dist = int(def_dist)
#     shot_clock = int(shot_clock)
#     shots_made = int(shots_made)
#     total_shots = int(total_shots)

#     # Check if player is already in dictionary
#     if player not in player_data:
#         player_data[player] = {'zone_1': [0, 0], 'zone_2': [0, 0], 'zone_3': [0, 0], 'zone_4': [0, 0]}

#     # Check which zone the shot falls into and update the appropriate count
#     if shot_dist <= 10 and def_dist <= 2 and shot_clock >= 20:
#         player_data[player]['zone_1'][0] += shots_made
#         player_data[player]['zone_1'][1] += total_shots
#     elif shot_dist <= 10 and def_dist <= 2 and shot_clock < 20:
#         player_data[player]['zone_2'][0] += shots_made
#         player_data[player]['zone_2'][1] += total_shots
#     elif shot_dist > 10 and def_dist <= 2 and shot_clock >= 20:
#         player_data[player]['zone_3'][0] += shots_made
#         player_data[player]['zone_3'][1] += total_shots
#     else:
#         player_data[player]['zone_4'][0] += shots_made
#         player_data[player]['zone_4'][1] += total_shots

# # Loop through each player and determine their best shooting zone based on hit rate
# for player in player_data:
#     zone_hits = [
#         (1, player_data[player]['zone_1'][0] / player_data[player]['zone_1'][1]) if player_data[player]['zone_1'][1] != 0 else (1, 0),
#         (2, player_data[player]['zone_2'][0] / player_data[player]['zone_2'][1]) if player_data[player]['zone_2'][1] != 0 else (2, 0),
#         (3, player_data[player]['zone_3'][0] / player_data[player]['zone_3'][1]) if player_data[player]['zone_3'][1] != 0 else (3, 0),
#         (4, player_data[player]['zone_4'][0] / player_data[player]['zone_4'][1]) if player_data[player]['zone_4'][1] != 0 else (4, 0),
#     ]
#     zone_hits.sort(key=lambda x: x[1], reverse=True)
#     print(f"{player}\t{zone_hits[0][0]}")