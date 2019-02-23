#!/usr/bin/python
import sys

# Output only URL. E.g. can get list of unique URLs after reduce
# cd python/src/p13_mapper_url/
# python3 mapper.py < test_data_for_mapper.txt

for line in sys.stdin:
    a = line.split('\t')
    print(a[2], end='')

