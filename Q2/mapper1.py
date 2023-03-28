#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import csv

header = sys.stdin.readline()

for line in csv.reader(sys.stdin, quotechar='"'):
# Testing code
# with open('E:\@FORDHAM\BigData\shot_logs.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile, quotechar='"')
#     header = next(csvreader)
#     for line in csvreader:
        shooter = line[-1]
        shot_dist = line[11]
        def_dist = line[16]
        clock = line[8]
        made = 1 if line[13].strip() == 'made' else 0 # shot result
        if shooter and shot_dist and def_dist and clock:
            # KVP (shooter, (dist, def sift, clock, made))
            print('{}\t{},{},{},{}'.format(shooter, shot_dist, def_dist, clock, made))