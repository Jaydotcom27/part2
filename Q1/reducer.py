#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
from operator import itemgetter

defenders = {}

# We iterate over all the lines on the standard input
for line in sys.stdin:
    pair, shooting_data = line.strip().split('\t')
    _, defender = pair.split('-')
    shots, successful = map(int, shooting_data.split(','))

    # The data for each defender is updated, or added if that particular one does not exist yet
    if defender not in defenders:
        defenders[defender] = [0, 0]
    defenders[defender][0] += shots
    defenders[defender][1] += successful

# Hit rate calculation
hit_rates = []
for defender, stats in defenders.items():
    shots, successful = stats
    if shots >= 10:
        hit_rate = successful / shots
        hit_rates.append((defender, hit_rate, shots))

# We sort in ascending order
hit_rates.sort(key=itemgetter(1))

# Printing top 15 defenders with lower hit rates
for defender, hit_rate, shots in hit_rates[:15]:
    print(f"{defender}\t{hit_rate:.2%}\t{shots:,d}")