#!/usr/bin/python

import sys
import collections

file = sys.argv[1]
pos = sys.argv[2]

counts = collections.defaultdict(int)

for line in open(file):
    line = line[:-1]
    tokens = line.split()
    for token in tokens:
        word,p = token.split("_")
        if pos == p:
            counts [word] += 1
            
items = counts.items()
items = sorted(items, key=lambda x: x[1], reverse=True)

for key,value in items:
    print "%20s %10d"%(key,value)
