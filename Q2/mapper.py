#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import csv

# Define the four comfortable zones based on the given matrix
zones = {
    'zone1': {
        'shot_dist': [0, 8],
        'close_def_dist': [0, 2],
        'shot_clock': [0, 7],
    },
    'zone2': {
        'shot_dist': [8, 16],
        'close_def_dist': [0, 2],
        'shot_clock': [0, 7],
    },
    'zone3': {
        'shot_dist': [16, 24],
        'close_def_dist': [0, 2],
        'shot_clock': [0, 7],
    },
    'zone4': {
        'shot_dist': [24, 100],
        'close_def_dist': [0, 2],
        'shot_clock': [0, 7],
    },
}

# Read the header row
header = sys.stdin.readline()

# Process each row of input data
for line in csv.reader(sys.stdin, quotechar='"'):
    # Extract the relevant fields from the input row
    player = line[21]
    shot_dist = float(line[17])
    close_def_dist = float(line[16])
    shot_clock = float(line[22])
    shot_made_flag = int(line[23])

    # Determine which comfortable zone the current shot belongs to
    for zone_name, zone in zones.items():
        if (
            zone['shot_dist'][0] <= shot_dist <= zone['shot_dist'][1] and
            zone['close_def_dist'][0] <= close_def_dist <= zone['close_def_dist'][1] and
            zone['shot_clock'][0] <= shot_clock <= zone['shot_clock'][1]
        ):
            # Emit a key-value pair for the current player and zone
            print(f"{player}\t{zone_name}\t{shot_made_flag}")
            break