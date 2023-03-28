#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import random

for line in sys.stdin:
    key, values = line.strip().split('\t')
    line_key = random.randint(1,4)
    print('{}\t{}'.format(line_key, values))
