#!/usr/bin/python

import sys
import string
import lisp

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

def remove_alt_pron2(str):
    
    if len(str) < 3:
        return str
    elif  str[-3] == '(' and str[-1] == ')' and str[-2].isdigit():
        return str[0:-3]
    else:
        return str

f = open(sys.argv[1])

for line in f:
    tokens = line.split()
    # Remove disfluencies
    tokens = filter(lambda x: not x.startswith("++") and not x.endswith("++") , tokens)
    # Remove sentence boundaries
    tokens = filter(lambda x: not lisp.string_equal(x,"<s>") and not lisp.string_equal(x,"</s>"), tokens)
    tokens = filter(lambda x: not lisp.string_equal(x,"<s>") and not lisp.string_equal(x,"</s>") and not lisp.string_equal(x,"<sil>"), tokens)
    #if "A. B. C." in line:
    #    print line
    #    print tokens
    tokens = map(remove_alt_pron2, tokens)

    #if "A. B. C." in line:
    #    print tokens


    # Only print it if there's something left (besides the ID)
    #if "A. B. C." in line:
    if len(tokens) > 1:
        new_string = string.join(tokens, ' ')
        if "A B C" in new_string:
            print line
            print new_string


