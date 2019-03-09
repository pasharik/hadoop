#!/usr/bin/python
import sys

# Filter only logs related to 'user10'
# cd python/src/p12_selection_mapper/
# python3 mapper.py < test_data_for_mapper.txt


for line in sys.stdin:
    if '\tuser10\t' in line:
        print(line, end='')
