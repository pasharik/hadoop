#!/usr/bin/python
import sys

# Count across ALL lines in document
# cd python/src/p3_combining_v2_mapper/
# python3 mapper.py < test_data_for_mapper.txt

a = {}

for line in sys.stdin:
    for token in line.strip().split(" "):
        if token:
            if a.get(token):
                a[token] += 1
            else:
                a[token] = 1

for k in a.items():
    print(k[0] + '\t' + str(k[1]))
