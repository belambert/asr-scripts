#!/usr/bin/python

import sys

if len(sys.argv != 3):
    print "%s -n <filename>"%sys.argv[0]
    exit(1)

file = sys.argv[1]
count_target = int(sys.argv[2][1:])
count = 0

# This one is a little more complex than conll-head.sh... because
# we have to count from the end.
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
  




