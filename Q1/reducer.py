#!/usr/bin/python
# --*-- coding:utf-8 --*--

import sys
from operator import itemgetter

defenders = {}

# loop through input from stdin
for line in sys.stdin:
    # get data from input line and split it
    pair, shooting_data = line.strip().split('\t')
    _, defender = pair.split('-')
    shots_taken, made = shooting_data.split(',')
    
    # check if defender already exists in the dictionary and update their shot and successful shots count
    current = defenders.get(defender, [0, 0])
    try:
        current[0] += int(shots_taken) 
        current[1] += int(made)
        defenders[defender] = current
    except ValueError:
        pass

# create list of rates for defenders who have 10 or more shots
rates = []
for key, value in defenders.items():
    if value[0] < 10:
        continue
    rate = float(value[1]) / value[0]
    shots_taken = value[0]
    rates.append([key, rate, shots_taken])

# sort list of rates by the rate value
rates.sort(key=itemgetter(1))

# print the top 10 defenders with the lowest rate, meaning; most unwanted defender
for defender, rate, shots_taken in rates[:10]:
    print('{}\t{:.2%}\t{:,d}'.format(defender, rate, shots_taken))