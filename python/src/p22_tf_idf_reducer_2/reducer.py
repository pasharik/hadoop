#!/usr/bin/python
import sys

# cd python/src/p22_tf_idf_reducer_2/
# python3 reducer.py < test_data_for_reducer.txt

lastKey = None
cnt = 0
doc_tf_buf = []


def do_print(key, count, arr):
    for el in arr:
        print(key + '#' + el[0] + '\t' + el[1] + '\t' + str(count))
    return


for line in sys.stdin:
    arr1 = line.strip().split("\t")
    key = arr1[0]
    arr2 = arr1[1].split(';')
    if lastKey and lastKey != key:
        do_print(lastKey, cnt, doc_tf_buf)
        cnt = 0
        doc_tf_buf = []
    lastKey = key
    cnt += 1
    doc_tf_buf.append((arr2[0], arr2[1]))
if lastKey:
    do_print(lastKey, cnt, doc_tf_buf)
