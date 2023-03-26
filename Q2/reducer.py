#!/usr/bin/env python

import sys

# initialize the counts for each zone to 0
zone_counts = [0] * 3

# initialize the current player ID and zone tuple to None
current_player = None
current_zone = None

for line in sys.stdin:
    # split the line into player ID and zone tuple
    player, zone = line.strip().split('\t')
    
    # convert the zone tuple to a list of counts
    counts = zone.strip('()').split(',')
    
    # if this is the first record or a new player, output the counts for the previous player
    if current_player and player != current_player:
        if current_player == '101108' or current_player == '2544' or current_player == '201935' or current_player == '201939':
            print(current_player + '\t' + '\t'.join(str(x) for x in zone_counts))
            # reset the counts for the new player
            zone_counts = [0] * 3
        
    # update the current player ID and zone tuple
    current_player = player
    current_zone = zone
    
    # update the counts for each zone
    for i in range(len(counts)):
        zone_counts[i] += int(counts[i])

# output the counts for the players matching the required IDs
if current_player == '101108' or current_player == '2544' or current_player == '201935' or current_player == '201939' or current_player:
    print(current_player + '\t' + '\t'.join(str(x) for x in zone_counts))