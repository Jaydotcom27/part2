#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

# This scripts is checking for convergence or to check if the centroids are no longer changing
old = sys.argv[1]
old = [round(float(v),2) for v in old.strip().split(',')]
new = sys.argv[2]
new = [round(float(v),2) for v in new.strip().split(',')]

equal = 0
for i in range(len(old)):
    if old[i] == new[i]:
        equal += 1

# 3 because we have 3 dimensions for the centroids from our original data
print(1 if equal == 3 else 0)
