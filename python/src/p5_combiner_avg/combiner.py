#!/usr/bin/python
import sys

#Combine sub-sums

(lastKey, sum, count) = (None, 0, 0)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    value = value.split(";")[0]
    if lastKey and lastKey != key:
        print(lastKey + '\t' + str(sum) + ';' + str(count))
        (lastKey, sum, count) = (key, int(value), 1)
    else:
        (lastKey, sum, count) = (key, sum + int(value), count + 1)
if lastKey:
    print(lastKey + '\t' + str(sum) + ';' + str(count))
