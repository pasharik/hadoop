#!/usr/bin/python
import sys

# cd python/src/p1_streaming/
# python3 mapper.py < test_data_for_mapper.txt | sort > test_data_for_reducer.txt

for line in sys.stdin:
    for token in line.strip().split(" "):
        if token: print(token + '\t1')
