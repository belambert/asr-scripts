#!/usr/bin/python

import sys, re

file = sys.argv[1]

with open(file) as f:
    file_string = f.read()


file_string = re.sub('\n', ' ', file_string)
all_tokens = file_string.split()

for i in range(1,len(all_tokens)):
    print all_tokens[i],
    if i % 1 == 0:
        print ''



