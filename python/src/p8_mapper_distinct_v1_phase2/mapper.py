#!/usr/bin/python
import sys

# Distinct value - unique items count - stage 2 mapper
# cd python/src/p8_mapper_distinct_v1_phase2/
# python3 mapper.py < test_data_for_mapper.txt

for line in sys.stdin:
    tokens = line.strip().split(",")
    f = tokens[1]
    print(f + '\t1')
