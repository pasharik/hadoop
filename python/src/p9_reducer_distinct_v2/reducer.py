#!/usr/bin/python
import sys

# cd python/src/p9_reducer_distinct_v2/
# python3 reducer.py < test_data_for_reducer.txt

(lastKey) = None
a = {}
arr_with_dups = []


def exclude_duplicates(arr):
    return list(dict.fromkeys(arr))


def fill_map(list1):
    for l in list1:
        if a.get(l):
            a[l] += 1
        else:
            a[l] = 1
    return

for line in sys.stdin:
    (key, val) = line.strip().split("\t")
    if lastKey and lastKey != key:
        fill_map(exclude_duplicates(arr_with_dups))
        (lastKey) = key
        arr_with_dups = [val]
    else:
        arr_with_dups.append(val)
        (lastKey) = key
if lastKey:
    fill_map(exclude_duplicates(arr_with_dups))

for k in a:
    print(k + '\t' + str(a[k]))
