#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import math

initial_centroids = sys.argv[1].strip().split(';')

centroids = [line.strip().split(',')[:-1] for line in initial_centroids]

def getDistance(a, b):
    total = [math.pow(u-v, 2) for u,v in zip(a, b)]
    return math.sqrt(sum(total))

for line in sys.stdin:
    line = line.strip()
    player, data = line.split('\t')
    values = data.split(',') # shot_dist_avg, close_def_avg, shot_clock_avg
    values = values[:-1]
    distances = []
    for i in range(len(centroids)):
        a = [float(val ) for val in values]
        b = [float(c) for c in centroids[i]]
        dist = getDistance(a, b)
        distances.append(dist)
    cluster = distances.index(min(distances))
    new_values = [str(round(el,4)) for el in a]
    print('{}\t{}'.format(cluster+1, ','.join([str(s) for s in values])))
