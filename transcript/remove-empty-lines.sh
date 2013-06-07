#!/usr/bin/python

import sys
import re

transcript_file = sys.argv[1]

for line in open(transcript_file).readlines():
    line = line[:-1]
    if len(line) != 0:
        print line


