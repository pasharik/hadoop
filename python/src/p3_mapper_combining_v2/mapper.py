#!/usr/bin/python
import sys

#Count on ALL lined in document

a = {}

for line in sys.stdin:
    for token in line.strip().split(" "):
        if token:
            if a.get(token):
                a[str(token)] += 1
            else:
                a[str(token)] = 1

for k in a.items():
    print(k[0] + '\t' + str(k[1]))
