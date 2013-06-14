#!/usr/bin/python

import sys

file = sys.argv[1]

count = 0

for line in open(file):
    line = line[:-1]
    if line == "":
        count += 1

print count
