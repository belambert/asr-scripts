#!/usr/bin/python

import sys

file=sys.argv[1]

#transcripts = []
id_table = {}

for line in open(file):
    line = line[:-1]
    pivot=line.rfind("(")
    trans = line[:pivot]
    id = line[pivot+1:-1]
    if id not in id_table:
	id_table[id] = True
	print line
    else:
	pass

