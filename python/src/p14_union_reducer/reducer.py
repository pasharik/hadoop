#!/usr/bin/python
import sys

# Union of two sets, i.e. just print all (unique) keys
# cd python/src/p14_union_reducer/
# python3 reducer.py < test_data_for_reducer.txt

lastKey = None

for line in sys.stdin:
    key = line.strip().split("\t")[0]
    if lastKey and lastKey != key:
        print(lastKey)
    lastKey = key
if lastKey:
    print(lastKey)

