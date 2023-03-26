#!/usr/bin/env python

import sys

# Define the ranges for shot distance, closest defender distance, and shot clock
shot_dist_ranges = [(0, 5), (5, 15), (15, 25), (25, 100)]
defender_dist_ranges = [(0, 2), (2, 4), (4, 6), (6, 100)]
shot_clock_ranges = [(0, 6), (6, 12), (12, 18), (18, 25)]

# Initialize the counts for each zone to zero
zone_counts = [[0 for _ in range(4)] for _ in range(4)]

# Process each input record from the mapper
for line in sys.stdin:
    # Parse the player id and the zone counts from the input record
    player_id, shot_dist_zone, defender_dist_zone, shot_clock_zone = line.strip().split('\t')
    shot_dist_zone, defender_dist_zone, shot_clock_zone = int(shot_dist_zone), int(defender_dist_zone), int(shot_clock_zone)
    
    # Update the count for the corresponding zone
    zone_counts[shot_dist_zone][defender_dist_zone*4+shot_clock_zone] += 1

# Output the player id and the counts for each zone
for i, counts in enumerate(zone_counts):
    print(str(i+1) + '\t' + '\t'.join(str(x) for x in counts))