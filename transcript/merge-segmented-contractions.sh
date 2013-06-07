#!/usr/bin/python

import sys
import string
import blambert_util as bl
import re

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()

substitution_pairs = [[" 'VE", "'VE"],
                      [" 'S", "'S"],
                      [" 'RE", "'RE"],
                      [" 'LL", "'LL"],
                      [" N'T", "N'T"],
                      [" 'D", "'D"],
                      [" 'M", "'M"],
                      [" ' ", "' "],
                      [" CAN NOT ", " CANNOT "],
                      ["Y' ALL", "Y'ALL"],
                      ["` TIS", "'TIS"]]

for line in lines:
    line = line[:-1]
    for [before, after] in substitution_pairs:
        #line = line.replace("YOU 'VE", "YOU'VE")
        line = line.replace(before, after)
    line = re.sub("^CAN NOT", "CANNOT", line, count=1)
    print line
