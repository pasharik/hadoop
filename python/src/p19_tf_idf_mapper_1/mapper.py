#!/usr/bin/python
import sys
import re

# Out:  (word#doc_number    1)
# cd python/src/p19_tf_idf_mapper_1/
# python3 mapper.py < test_data_for_mapper.txt

for line in sys.stdin:
    doc_num = line.strip().split(':')[0]
    txt = line.strip().replace(doc_num + ':', '', 1)
    word_arr = re.findall('\\w+', txt)
    for word in word_arr:
        print(word + '#' + doc_num + '\t1')
