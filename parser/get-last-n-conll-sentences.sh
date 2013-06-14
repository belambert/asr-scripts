#!/usr/bin/python

import sys

file = sys.argv[1]
count_target = int(sys.argv[2])
count = 0
lines = open(file).readlines()
lines_to_print = []

for line in reversed(lines):
    if line == "":
        count += 1
    if count == count_target:
        break
    lines_to_print.append(line)


for line in reversed(lines_to_print):
    print line
  




