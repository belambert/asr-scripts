#!/usr/bin/python

import sys

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
    if id not in id_table and trans not in trans_table:
	id_table[id] = True
	trans_table[trans] = True
	print line
    else:
	pass

