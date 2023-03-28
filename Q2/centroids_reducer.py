#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import random

groups = [[],[],[],[]]

# test = ['1\t18,3,19,3', '3\t18,3,19,3', '4\t18,3,40,1']
# for line in test:
for line in sys.stdin:
    key, val = line.strip().split('\t') # val = {SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}
    key = int(key)
    groups[key-1].append(val)

for i in range(len(groups)):
    if groups[i]:
        index = random.randrange(0, len(groups[i]))
        centroid = groups[i][index]
        centroid = centroid.split(",")[:-1]
        print('{}\t{}'.format(i+1, ",".join(centroid)))
