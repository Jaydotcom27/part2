#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import random

groups = [[],[],[],[]]

# Testing code
# test = ['1\t18,3,19,3', '3\t18,3,19,3', '4\t18,3,40,1']
# for line in test:

# Initially grouping based on the previous random distribution
for line in sys.stdin:
    key, val = line.strip().split('\t') 
    key = int(key)
    groups[key-1].append(val)

# Selecting a random point from each group and updating centroids
for i in range(len(groups)):
    if groups[i]:
        index = random.randrange(0, len(groups[i]))
        centroid = groups[i][index]
        centroid = centroid.split(",")[:-1]
        print('{}\t{}'.format(i+1, ",".join(centroid)))
