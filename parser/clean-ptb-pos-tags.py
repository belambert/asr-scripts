#!/usr/bin/python

import sys,os

if len(sys.argv) != 2:
    print "Usage: %s <ptb file>"%os.path.basename(sys.argv[0])
    exit(1)

file = sys.argv[1]

separator = '_'


def clean_token (token):
    word, pos = token.split(separator)
    # If there is a caret in the POS tag, remove it...
    # If there are multiple carets, just use the first tag.
    if '^' in pos:
        pos = filter(lambda x: x != '', pos.split('^'))[0]
    return "%s%s%s"%(word, separator, pos)

with open(file) as f:
    for line in f:
        tokens = line.split()
        tokens = map(clean_token, tokens)
        

        # For some reason it seems that the POS tagger wants the line to 
        # end with a space...
        # This doesn't seem to be strictly true, but adding the space seems to
        # fix some bug...
        line="%s "%' '.join(tokens)
        print line
