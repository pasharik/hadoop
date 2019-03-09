#!/usr/bin/python
import sys

# Brute-force permutation of all elements in every line
# cd python/src/p11_cross_correlation_mapper_stripes/
# python3 mapper.py < test_data_for_mapper.txt


def emit(elem, map):
    print(elem + '\t', end='')
    i = 0
    for k in map.items():
        if i > 0:
            print(',', end='')
        print(k[0] + ':' + str(k[1]), end='')
        i += 1
    print()
    return

for line in sys.stdin:
    a = line.strip().split(" ")

    for i in range(len(a)):
        m = {}
        for j in range(len(a)):
            if a[i] != a[j]:
                if m.get(a[j]):
                    m[a[j]] += 1
                else:
                    m[a[j]] = 1
        emit(a[i], m)
