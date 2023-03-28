#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

# Taking initial centroids from cli arguments
initial_centroids = sys.argv[1:]
centroids = []

# Adding tabs and appending to centroid list, finally printing centroids separated by ;
for centroid in initial_centroids:
    _, c = centroid.strip().split('\t')
    centroids.append(c)
print(';'.join(centroids))
