#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

# This scripts is checking for convergence or to check if the centroids are no longer changing
old, new = sys.argv[1:]
old = [round(float(val), 2) for val in old.split(',')]
new = [round(float(val), 2) for val in new.split(',')]

equal = sum(1 for x, y in zip(old, new) if x == y) # Zip iterates over both lists simultaneously 

# 3 because we have 3 dimensions for the centroids from our original data
print(1 if equal == 3 else 0)