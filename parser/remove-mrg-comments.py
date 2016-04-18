#!/usr/bin/python

import sys

file = sys.argv[1]

for line in open(file):
    line = line[:-1]
    if not line.startswith("*x*") and not line.startswith("( (CODE ") and line != "":
        print line
