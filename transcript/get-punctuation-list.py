#!/usr/bin/python

import sys
import string
import blambert_util as bl
from collections import defaultdict


if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

must_occur_twice = True
print_counts = False
print_normalized = False

punc_table = defaultdict(int)
punc_table_normalized = defaultdict(int)

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines:
    tokens = line.split()
    new_tokens = []
    for token in tokens[:-1]:
        # If it's a noise marker, ignore it.
        if token.startswith('++') and token.endswith('++'):
            pass
        # If it's punctuation...  normalize it(?)
        elif token[0] in string.punctuation:
            #punc_table[token[0]] += 1
            punc_table[token] += 1
            punc_table_normalized[token[1:]] += 1
        # O/w it's a normal word
        else:
            pass

#for punc, count in punc_table.items():
#    print "%s  %s" % (punc, count)



if print_normalized:
    counts = punc_table_normalized.items()
    counts = sorted(counts, key=lambda x: x[1], reverse=True)
    for punc, count in counts:
        if not must_occur_twice or count > 1:
            if print_counts:
                print "%s  %s" % (punc, count)
            else:
                print "%s" % punc
else:
    counts = punc_table.items()
    counts = sorted(counts, key=lambda x: x[1], reverse=True)
    for punc, count in counts:
        if not must_occur_twice or count > 1:
            if print_counts:
                print "%s  %s" % (punc, count)
            else:
                print "%s" % punc


