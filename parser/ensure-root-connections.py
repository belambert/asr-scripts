#!/usr/bin/python

import sys

file=sys.argv[1]


with open(file) as f:
    for line in f:
        tokens = line.split()
        if len(tokens) > 0:
            parent = tokens[6]
            parent_type = tokens[7]
            if parent == '0':
                if parent_type != 'root' and parent_type != 'erased':
                    # Then we need to set it to root
                    sys.stderr.write('Changing root pointer type to root from: %s\n'%parent_type)
                    tokens[7] = 'root'
        print '\t'.join(tokens)

