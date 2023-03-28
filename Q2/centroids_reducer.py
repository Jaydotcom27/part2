#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import random

groups = [[],[],[],[]]

for line in sys.stdin:
    key, val = line.strip().split('\t') # val = {SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}
    key = int(key)
    groups[key-1].append(val)

for i in range(len(groups)):
    index = random.randrange(0, len(groups[i]))
    centroid = groups[i][index]
    centroid = centroid.split(",")[:-1]
    print('{}\t{}'.format(i+1, ",".join(centroid)))
