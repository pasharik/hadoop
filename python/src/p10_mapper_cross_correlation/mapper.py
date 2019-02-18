#!/usr/bin/python
import sys

# Brute-force permutation of all elements in every line
# cd python/src/p10_mapper_cross_correlation/
# python3 mapper.py < test_data_for_mapper.txt

for line in sys.stdin:
    a = line.strip().split(" ")

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] != a[j]:
                print(a[i] + ',' + a[j] + '\t1')
