import sys
from collections import defaultdict
from operator import itemgetter

defenders = defaultdict(lambda: [0, 0])

for line in sys.stdin:
    pair, shooting_data = line.strip().split('\t')
    _, defender = pair.split('-')
    shots, successful = map(int, shooting_data.split(','))
    defenders[defender][0] += shots
    defenders[defender][1] += successful

rates = [[key, value[1]/value[0], value[0]] for key, value in defenders.items() if value[0] >= 10]
rates.sort(key=itemgetter(1))

for defender, rate, shots in rates[:5]:
    print('{}\t{:.2%}\t{:,d}'.format(defender, rate, shots))