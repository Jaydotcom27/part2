#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
from operator import itemgetter

defenders = {}

for line in sys.stdin:
    pair, shooting_data = line.strip().split('\t')
    _, defender = pair.split('-')
    shots, successful = shooting_data.split(',')
    current = defenders.get(defender, [0, 0])
    try:
        current[0] += int(shots) 
        current[1] += int(successful)
        defenders[defender] = current
    except ValueError:
        pass

rates = []
for key, value in defenders.items():
    if value[0] < 10:
        continue
    rates.append([key, float(value[1])/value[0], value[0]])
rates.sort(key=itemgetter(1))

for defender, rate, shots in rates[:5]:
    print('{}\t{:.2%}\t{:,d}'.format(defender, rate, shots))
