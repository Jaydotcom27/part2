#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import math

# Requested players
players = {
    201935: "Harden-James",
    2544: "James-LeBron",
    201939: "Curry-Stephen",
    101108: "Paul-Chris"
}

initial_centroids = sys.argv[1].strip().split(';')

centroids = [line.strip().split(',') for line in initial_centroids]

# Helper function to compute euclidean distance 
def calc_euc_dist(a, b):
    total = [math.pow(u-v, 2) for u,v in zip(a, b)]
    return math.sqrt(sum(total))

for line in sys.stdin:
    line = line.strip()
    player, data = line.split('\t')
    if not players.get(int(player)):
        continue
    temp_values = data.split(',') # shot_dist_avg, close_def_avg, shot_clock_avg, shot_rate
    values = temp_values[:-1]
    shot_rate = temp_values[-1]
    distances = []

    # Once again finding minimum distance to centroid and positioning player 
    for i in range(len(centroids)):
        a = [float(val ) for val in values]
        b = [float(c) for c in centroids[i]]
        dist = calc_euc_dist(a, b)
        distances.append(dist)
    cluster = distances.index(min(distances))
    new_values = [str(round(el,4)) for el in a]
    
    # Outputing Player, cluster and rate
    print('{}\t{}-{:.2%}'.format(players.get(int(player)), cluster+1, float(shot_rate)))
