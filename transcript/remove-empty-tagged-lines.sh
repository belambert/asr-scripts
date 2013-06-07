#!/usr/bin/python

import sys
import re

transcript_file = sys.argv[1]

for line in open(transcript_file).readlines():
    line = line[:-1]
    m = re.match("\s*(.*)\s*\((.+)\)", line)
    trans = m.group(1)
    id = m.group(2)
    if len(trans) != 0:
        print line


