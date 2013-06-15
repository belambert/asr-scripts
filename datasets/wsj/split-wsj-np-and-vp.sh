#!/usr/bin/python

import sys
import string
import re

if len(sys.argv) != 4:
    print "Usage: %s <merged file> <np file> <vp file>"%sys.argv[0]
    exit(-1)

punctuation_tokens = [ ",COMMA",
                      ".PERIOD",
                      "\"DOUBLE-QUOTE",
                      "-HYPHEN",
                      ".POINT",
                      "%PERCENT",
                      "--DASH",
                      "&AMPERSAND",
                      ":COLON",
                      ")RIGHT-PAREN",
                      "(LEFT-PAREN",
                      ";SEMI-COLON",
                      "?QUESTION-MARK",
                      "'SINGLE-QUOTE",
                      "...ELLIPSIS",
                      "/SLASH",
                      "}RIGHT-BRACE",
                      "{LEFT-BRACE",
                      "!EXCLAMATION-POINT",
                      "+PLUS",
                      "=EQUALS",
                      "#SHARP-SIGN",
                      "-MINUS"]

# This would probably be faster with a hashtable or "dict"
def vp_string_p(str):
    tokens = str.split()
    for punc_token in punctuation_tokens:
        if punc_token in tokens:
            return True
    return False


f = open(sys.argv[1])
lines = f.readlines()

np = open(sys.argv[2],"w")
vp = open(sys.argv[3],"w")

for line in lines:
    if vp_string_p(line):
        vp.write(line)
    else:
        np.write(line)



