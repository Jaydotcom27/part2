#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import csv

header = sys.stdin.readline()

for line in csv.reader(sys.stdin, quotechar='"'):
    shooter = line[-1]
    defender = line[15]
    made = 1 if line[13].strip() == 'made' else 0
    if shooter and defender:
        # key = shooter_id,defender_id
        # value = 1 -> for shoot count, 1 if shoot success
        print('{}-{}\t{},{}'.format(shooter, defender, 1, made))
