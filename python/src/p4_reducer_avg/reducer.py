#!/usr/bin/python
import sys

#Count average
# cd python/src/p4_reducer_avg/
# python3 reducer.py < test_data_for_reducer.txt

(lastKey, sum, count) = (None, 0, 0)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        print(lastKey + '\t' + str(round(sum / count)))
        (lastKey, sum, count) = (key, int(value), 1)
    else:
        (lastKey, sum, count) = (key, sum + int(value), count + 1)
if lastKey:
    print(lastKey + '\t' + str(round(sum / count)))
