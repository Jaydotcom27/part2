#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

vals = sys.argv[1:]
old = sys.argv[1]
old = [round(float(v),2) for v in old.strip().split(',')]
new = sys.argv[2]
new = [round(float(v),2) for v in new.strip().split(',')]

equal = 0
for i in range(len(old)):
    if old[i] == new[i]:
        equal += 1

if equal == 3:
    print(1)
else:
    print(0)
