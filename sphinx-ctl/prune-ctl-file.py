#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print "Usage: %s <id file> <ctl file>"%sys.argv[0]
    exit(-1)

id_file = sys.argv[1]
ctl_file = sys.argv[2]

ids = open(id_file).readlines()
ids = map(lambda x: x[:-1], ids)
id_table = {}
id_used_table = {}

for id in ids:
    id_table[id] = True

for line in open(ctl_file):
    line = line[:-1]
    tokens = line.split()
    id = tokens[-1]
    if id_table.get(id):
        print line
        id_used_table[id] = True
