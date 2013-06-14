#!/usr/bin/python

import sys

file = sys.argv[1]

count_target = int(sys.argv[2])

count = 0

for line in open(file):
    line = line[:-1]
    if line == "":
        count += 1
    if count == count_target:
        break
    print line
