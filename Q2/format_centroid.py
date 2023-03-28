#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys


initial_centroids = sys.argv[1:]
centroids = []

for centroid in initial_centroids:
    _, c = centroid.strip().split('\t')
    centroids.append(c)
print(';'.join(centroids))
