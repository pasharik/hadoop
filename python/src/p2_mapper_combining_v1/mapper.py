#!/usr/bin/python
import sys

for line in sys.stdin:
    a = {}
    for token in line.strip().split(" "):
        if token:
            if a.get(token):
                a[str(token)] += 1
            else:
                a[str(token)] = 1
    for k in a.items():
        print(k[0] + '\t' + str(k[1]))
