#!/usr/bin/python
import sys

# Count inside each line in document
# cd python/src/p2_mapper_combining_v1/
# python3 mapper.py < test_data_for_mapper.txt

for line in sys.stdin:
    a = {}
    for token in line.strip().split(" "):
        if token:
            if a.get(token):
                a[token] += 1
            else:
                a[token] = 1
    for k in a.items():
        print(k[0] + '\t' + str(k[1]))
