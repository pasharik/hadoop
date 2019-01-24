#!/usr/bin/python
import sys

#Count on single lined in document

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
