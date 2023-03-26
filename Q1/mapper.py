#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import csv

# Iterate over the input lines from the CSV
for line in csv.reader(sys.stdin, quotechar='"'):
    # We extracted the shooter, defender, and success information from the line. 22nd, 16th and 14th positions respectively. 
    shooter = line[-1]
    defender = line[15]

    # We clean the made and missed to 1 or 0
    made = 1 if line[13].strip() == 'made' else 0
    
    # Only process the line if it contains both shooter and defender information
    if shooter and defender:
        # Created the KVP ((shooter, defender), (made))
        # The key is a string with the format 'shooter_id-defender_id'
        key = '{}-{}'.format(shooter, defender)
        value = '1,{}'.format(made)
        print('{}\t{}'.format(key, value))