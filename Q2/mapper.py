#!/usr/bin/env python
import sys
import csv

# define the ranges for shot distance, closest defender distance, and shot clock
shot_dist_ranges = [(0, 5), (5, 15), (15, 25), (25, 100)]
defender_dist_ranges = [(0, 2), (2, 4), (4, 6), (6, 100)]
shot_clock_ranges = [(0, 6), (6, 12), (12, 18), (18, 25)]

# function to map values to the correct range
def map_range(value, ranges):
    for i, r in enumerate(ranges):
        if value >= r[0] and value < r[1]:
            return i
    return len(ranges)

# read input data
# file = open('E:\@FORDHAM\BigData\shot_logs.csv', 'r')
header = sys.stdin.readline()
# reader = csv.reader(file)
reader = csv.reader(sys.stdin)
next(reader)

# process each shot record
for row in reader:
    if row[15]:
        player = row[15]
    if row[11]:
        shot_dist = float(row[11])
    if row[16]:
        defender_dist = float(row[16])
    if row[8]:
        shot_clock = float(row[8])
    
    # map shot distance, closest defender distance, and shot clock to the correct range
    shot_dist_zone = map_range(shot_dist, shot_dist_ranges)
    defender_dist_zone = map_range(defender_dist, defender_dist_ranges)
    shot_clock_zone = map_range(shot_clock, shot_clock_ranges)
    
    # output player name and tuple of zone counts
    print(player, (shot_dist_zone, defender_dist_zone, shot_clock_zone))

# file.close()
