#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import random

# test = ['1\t18,3,19,3', '3\t18,3,19,3', '4\t18,3,40,1']
# for line in test:
for line in sys.stdin:
    key, values = line.strip().split('\t')
    line_key = random.randint(1,4)
    print('{}\t{}'.format(line_key, values))
