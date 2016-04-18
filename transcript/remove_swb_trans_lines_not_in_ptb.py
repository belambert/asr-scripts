#!/usr/bin/python

import sys

file = sys.argv[1]

with open(file) as f:
    for line in f:
        line = line[:-1]
        if line != "[silence]":
            print line
