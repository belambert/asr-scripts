#!/usr/bin/python

import sys
import collections

if len(sys.argv) != 2:
    print "Usage: %s <filename>"%sys.argv[0]

file=sys.argv[1]

id_table = {}
trans_table = {}

for line in open(file):
    line = line[:-1]
    pivot=line.rfind("(")
    trans = line[:pivot]
    id = line[pivot+1:-1]

    id1, id2 = id.split()

    # The speech type code
    code = id1[3]

    if id2 not in id_table and code == 'c' and trans not in trans_table :
        id_table[id2] = True
        trans_table[trans] = True
        print line

