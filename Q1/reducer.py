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



# import sys
# from operator import itemgetter

# defenders = {}

# # Iterate over lines from stdin
# for line in sys.stdin:
#     pair, shooting_data = line.strip().split('\t')
#     _, defender = pair.split('-')
#     shots, successful = map(int, shooting_data.split(','))

#     # Update current defender's stats
#     if defender not in defenders:
#         defenders[defender] = [0, 0]
#     defenders[defender][0] += shots
#     defenders[defender][1] += successful

# # Compute hit rates for each defender
# hit_rates = []
# for defender, stats in defenders.items():
#     shots, successful = stats
#     if shots >= 10:
#         hit_rate = successful / shots
#         hit_rates.append((defender, hit_rate, shots))

# # Sort defenders by hit rate (ascending order)
# hit_rates.sort(key=itemgetter(1))

# # Print the 5 defenders with the lowest hit rates
# for defender, hit_rate, shots in hit_rates[:5]:
#     print(f"{defender}\t{hit_rate:.2%}\t{shots:,d}")