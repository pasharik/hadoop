#!/usr/bin/python
import sys

# Distinct value - unique items count - stage 1 mapper
# cd python/src/p6_distinct_v1_mapper/
# python3 mapper.py < test_data_for_mapper.txt

for line in sys.stdin:
    tokens = line.strip().split("\t")
    f = tokens[0]
    values = tokens[1].split(",")
    for v in values:
        print(f + ',' + v + '\t1')
