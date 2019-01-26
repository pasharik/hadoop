#!/usr/bin/python
import sys

#Count on ALL lined in document
# cd python/src/p3_mapper_combining_v2/
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
