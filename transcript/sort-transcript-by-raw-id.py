#!/usr/bin/python

import sys

file=sys.argv[1]
transcripts = []

for line in open(file):
    line = line[:-1]
    pivot=line.rfind("(")
    trans = line[:pivot]
    id = line[pivot+1:-1]
    transcripts.append([line, trans, id])

transcripts.sort(key=lambda x: x[2])

for line, trans, id in transcripts:
    print line
