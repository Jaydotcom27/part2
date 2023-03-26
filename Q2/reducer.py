#!/usr/bin/env python

from operator import itemgetter
import sys

# Define the zones and their boundaries
zones = {
    "zone1": {"shot_dist": (0, 5), "close_def_dist": (0, 2), "shot_clock": (0, 7)},
    "zone2": {"shot_dist": (0, 5), "close_def_dist": (2, 4), "shot_clock": (0, 7)},
    "zone3": {"shot_dist": (5, 10), "close_def_dist": (0, 2), "shot_clock": (0, 7)},
    "zone4": {"shot_dist": (5, 10), "close_def_dist": (2, 4), "shot_clock": (0, 7)},
}

# A dictionary to hold the total shots and successful shots for each player and zone
player_zone_stats = {}

# Process each input record
for line in sys.stdin:
    # Extract the player, zone, and shot stats from the input record
    player_zone, shot_stats = line.strip().split('\t')
    player, zone = player_zone.split('-')
    shots, successful = map(int, shot_stats.split(','))

    # Check if the player exists in the stats dictionary and add them if not
    if player not in player_zone_stats:
        player_zone_stats[player] = {z: {"shots": 0, "successful_shots": 0} for z in zones}

    # Check which zone the shot belongs to and update the stats dictionary accordingly
    for zone_name, zone_bounds in zones.items():
        if (zone_bounds["shot_dist"][0] <= shot_dist <= zone_bounds["shot_dist"][1] and
            zone_bounds["close_def_dist"][0] <= close_def_dist <= zone_bounds["close_def_dist"][1] and
            zone_bounds["shot_clock"][0] <= shot_clock <= zone_bounds["shot_clock"][1]):
            player_zone_stats[player][zone_name]["shots"] += shots
            player_zone_stats[player][zone_name]["successful_shots"] += successful
            break

# Output the stats for each player and their most successful zone
for player, zones_stats in player_zone_stats.items():
    best_zone = max(zones_stats.items(), key=lambda x: x[1]["successful_shots"]/x[1]["shots"])[0]
    print("{}\t{}\t{}".format(player, best_zone, zones_stats[best_zone]["successful_shots"]/zones_stats[best_zone]["shots"]))