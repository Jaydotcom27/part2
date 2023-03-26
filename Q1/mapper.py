#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import csv

# Read the header from the input and discard it
header = sys.stdin.readline()

# Iterate over the remaining input lines using the csv reader
for line in csv.reader(sys.stdin, quotechar='"'):
    # Extract the shooter, defender, and success information from the line
    shooter = line[-1]
    defender = line[15]
    made = 1 if line[13].strip() == 'made' else 0
    
    # Only process the line if it contains both shooter and defender information
    if shooter and defender:
        # Create a key-value pair to be emitted by the mapper
        # The key is a string with the format 'shooter_id-defender_id'
        # The value is a string with the format '1,success'
        # The '1' indicates that a shot was attempted
        # The 'success' variable is 1 if the shot was successful and 0 otherwise
        key = '{}-{}'.format(shooter, defender)
        value = '1,{}'.format(made)
        print('{}\t{}'.format(key, value))