#!/usr/bin/python
import sys

# Join two sets
# cd python/src/p18_repartition_join_reducer/
# python3 reducer.py < test_data_for_reducer.txt

query_arr = {}
url_arr = {}

def cortasian_emit(usr, arr1, arr2):
    for a1 in arr1:
        for a2 in arr2:
            print(usr + '\t' + a1 + '\t' + a2)
    return


for line in sys.stdin:
    a = line.strip().split('\t')
    b = a[1].split(':')
    user_ = a[0]
    type_ = b[0]
    value_ = b[1]
    if type_ == 'url':
        if url_arr.get(user_):
            url_arr[user_].append(value_)
        else:
            url_arr[user_] = [value_]
    else:
        if query_arr.get(user_):
            query_arr[user_].append(value_)
        else:
            query_arr[user_] = [value_]


for user_id in query_arr:
    qq = query_arr[user_id]
    if url_arr.get(user_id):
        uu = url_arr[user_id]
        cortasian_emit(user_id, qq, uu)
