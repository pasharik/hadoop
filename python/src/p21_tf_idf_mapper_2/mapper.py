#!/usr/bin/python
import sys

# Out: (word, (doc_id;tf;1)
# cd python/src/p21_tf_idf_mapper_2/
# python3 mapper.py < test_data_for_mapper.txt

for line in sys.stdin:
    arr = line.strip().split('\t')
    print(arr[0] + '\t' + arr[1] + ';' + arr[2] + ';1')
