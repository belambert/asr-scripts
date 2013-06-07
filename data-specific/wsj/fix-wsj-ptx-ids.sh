#!/usr/bin/python

import sys

file=sys.argv[1]

for line in open(file):
    line = line[:-1]
    pivot = line.rfind("(")
    trans = line[:pivot]
    id = line[pivot+1:-1]
    id_parts = id.split()
    true_id = id_parts[0]
    trans = trans.strip()
    print "%s (%s)"%(trans, true_id)
