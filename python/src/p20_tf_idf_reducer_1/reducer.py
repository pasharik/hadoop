#!/usr/bin/python
import sys

# cd python/src/p20_tf_idf_reducer_1/
# python3 reducer.py < test_data_for_reducer.txt

lastKey = None
cnt = 0
ar = None

for line in sys.stdin:
    key = line.strip().split("\t")[0]
    if lastKey and lastKey != key:
        print(ar[0] + '\t' + ar[1] + '\t' + str(cnt))
        cnt = 0
    ar = key.split('#')
    lastKey = key
    cnt += 1
if lastKey:
    print(ar[0] + '\t' + ar[1] + '\t' + str(cnt))
