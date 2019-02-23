#!/usr/bin/python
import sys

# Intersection of two sets - only elements which are in both sets
# cd python/src/p15_reducer_intersection/
# python3 reducer.py < test_data_for_reducer.txt

lastKey = None

for line in sys.stdin:
    key = line.strip().split("\t")[0]
    if lastKey and lastKey == key:
        print(key)
    lastKey = key

