#!/usr/bin/python
import sys

# cd python/src/p7_distinct_v1_reducer/
# python3 reducer.py < test_data_for_reducer.txt

(lastKey) = None

for line in sys.stdin:
    (key) = line.strip().split("\t")[0]
    if lastKey and lastKey != key:
        print(lastKey)
        (lastKey) = key
    else:
        (lastKey) = key
if lastKey:
    print(lastKey)
