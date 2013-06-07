#!/usr/bin/python

import sys
import re

filename=sys.argv[1]
f = open(filename)

for line in f:
    if line.startswith('<Episode'):
        m = re.search(" Filename=(\S*) ", line)
        filename = m.group(1)
        filename = filename.replace(".sph", "")
        print filename
                      
