#!/usr/bin/python
import sys

# Subtract elements B from A
# cd python/src/p16_reducer_difference/
# python3 reducer.py < test_data_for_reducer.txt

oldLastKey = None
(lastKey, lastValue) = (None, None)

for line in sys.stdin:
    item = line.strip().split("\t")
    key = item[0]
    value = item[1]
    if lastKey and lastKey != key:
        if ((not oldLastKey) or (oldLastKey != lastKey)) and (lastValue == 'A'):
            print(lastKey)
        oldLastKey = lastKey
        (lastKey, lastValue) = (key, value)
    else:
        oldLastKey = lastKey
        (lastKey, lastValue) = (key, value)

if lastKey:
    if ((not oldLastKey) or (oldLastKey != lastKey)) and (lastValue == 'A'):
        print(lastKey)
