#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

centroids = {}

# Testing code
# test = ['101127\t18,3,19,3', '101127\t18,3,19,3', '101127\t18,3,40,1']
# for line in test:
for line in sys.stdin:
    centroid, value = line.strip().split('\t')
    data = [round(float(v),4) for v in value.strip().split(",")]
    if centroids.get(centroid):
        centroids[centroid].append(data)
    else:
        centroids[centroid] = [data]

for key, val in centroids.items():
    shot_dist = []
    close_def = []
    shot_clock = []
    for row in val:
        shot_dist.append(row[0])
        close_def.append(row[1])
        shot_clock.append(row[2]) 
    
    # Iterates dictionary and calculates average for each of the 3 values
    shot_dist_avg = round(sum(shot_dist) / len(shot_dist), 4)
    close_def_avg = round(sum(close_def) / len(close_def), 4)
    shot_clock_avg = round(sum(shot_clock) / len(shot_clock), 4)
    print("{}\t{},{},{}".format(key, shot_dist_avg, close_def_avg, shot_clock_avg))
