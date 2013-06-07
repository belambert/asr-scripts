#!/usr/bin/python

import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    f = open(filename)
else:
    f = sys.stdin

dict = {}


for line in f:
    tokens = line.split()
    for token in tokens:
        dict[token] = True

words = dict.keys()

words.sort()

for word in words:
    print word
