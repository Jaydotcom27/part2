#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import math

# Testing code
# initial_centroids = ['2.2,3.4,1.2;1.1,4.5,3.2;2.6,1.8,0.9']

initial_centroids = sys.argv[1].strip().split(';')
centroids = [line.strip().split(',')[:-1] for line in initial_centroids]

# Helper euclidian dist function
def calc_euc_dist(a, b):
    total = [math.pow(u-v, 2) for u,v in zip(a, b)]
    return math.sqrt(sum(total))

for line in sys.stdin:
    line = line.strip()
    player, data = line.split('\t')
    values = data.split(',') 
    values = values[:-1]
    distances = []

    # Checking distance between player data and centroid, assign player to closer centroid by finding min. 
    for i in range(len(centroids)):
        a = [float(val ) for val in values]
        b = [float(c) for c in centroids[i]]
        dist = calc_euc_dist(a, b)
        distances.append(dist)
    cluster = distances.index(min(distances))
    new_values = [str(round(el,4)) for el in a]
    print('{}\t{}'.format(cluster+1, ','.join([str(s) for s in values])))
