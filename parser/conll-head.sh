#!/usr/bin/python

import sys

if len(sys.argv != 3):
    print "%s -n <filename>"%sys.argv[0]
    exit(1)

file = sys.argv[1]
count_target = int(sys.argv[2][1:])
count = 0

for line in open(file):
    line = line[:-1]
    if line == "":
        count += 1
    if count == count_target:
        break
    print line
