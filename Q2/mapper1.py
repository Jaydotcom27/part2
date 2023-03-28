#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import csv

header = sys.stdin.readline()

for line in csv.reader(sys.stdin, quotechar='"'):
    shooter = line[-1]
    shot_dist = line[11]
    def_dist = line[16]
    clock = line[8]
    made = 1 if line[13].strip() == 'made' else 0 # shot result
    if shooter and shot_dist and def_dist and clock:
        # key = shooter_id
        # value = {SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}
        print('{}\t{},{},{},{}'.format(shooter, shot_dist, def_dist, clock, made))
