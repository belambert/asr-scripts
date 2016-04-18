#!/usr/bin/python

import sys

if len(sys.argv) !=3:
    print "Usage %s <trans file> <id file>"%sys.argv[0]
    exit(-1)

trans_file = sys.argv[1]
ctl_file = sys.argv[2]

id_table = {}
for line in open(ctl_file):
    line = line[:-1]
    id_table[line]= True

for line in open(trans_file):
    line = line[:-1]
    pivot = line.rfind("(")
    id = line[pivot+1:-1]
    trans = line[:pivot-1]
    if id not in id_table:
        print line
