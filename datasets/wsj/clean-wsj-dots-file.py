#!/usr/bin/python

import sys
import string
import re

if len(sys.argv) != 2:
    print "Usage: %s <dot file>"%sys.argv[0]
    exit(-1)
filename = sys.argv[1]

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
                       "-MINUS",
                       "/SLASH",
                       ";SEMI-COLON",
                       "-DASH",
                       ",COMMA",
                       "\"UNQUOTES",
                       "\"QUOTES",
                       "(PARENS",
                       "--DASH",
                       ")END-PARENTHESES",
                       "\"QUOTE",
                       ")END-PARENS",
                       "`SINGLE-QUOTE",
                       "?QUESTION-MARK",
                       ")RIGHT-PAREN",
                       "\"CONTINUE-QUOTE",
                       "\"DOUBLE-QUOTE",
                       "'SINGLE-CLOSE-QUOTE",
                       "\"CLOSE-QUOTE",
                       "\"OPEN-QUOTE",
                       "(LEFT-PAREN",
                       "\"UNQUOTE",
                       ")PARENS",
                       "'SINGLE-QUOTE",
                       ")PARENTHESES",
                       "\"END-QUOTE",
                       "(PARENTHESES"]

def dot_noise_p(str):
    return str[0] == '[' and str[-1] == ']'

def remove_dot_noises (str):
    tokens = str.split()
    tokens = filter(lambda x: not dot_noise_p(x), tokens)
    return ' '.join(tokens)

def has_punctuation_p(str):
    tokens = str.split()
    for token in tokens:
        for punc in punctuation_tokens:
            if token == punc:
                return True
    return False

for line in open(filename):

    if "[bad_recording]" not in line:
        line = line[:-1]

        # Remove backslashes
        line = line.replace("\\", "")
        line = line.replace("<", "")
        line = line.replace(">", "")
        line = line.replace("*", "")
        line = line.replace(".", "")
        line = line.replace("!", "")
        line = line.replace(":", "")
        line = line.replace("`", "'")
        
        # In the WSJ transcripts, sometimes the inferred meaning of a partial
        # word is put in parens... e.g. " W(ED)- UNWED MOTHERS"... in this the
        # reader starts to say "WED" but catches themselves before finishing the word
        line = re.sub(r'\([A-Za-z]*\)', '', line)

        # Remove any tilde characters which appear to be able to come at the beginning and
        # end of any line (to denote a truncated recording?)
        line = line.replace("~ ", "")
        
        split_loc = line.rfind("(")
        first_half = line[0:split_loc]
        first_half = first_half.upper()
        second_half = line[split_loc:]
        line = "%s%s"%(first_half, second_half)
        line = remove_dot_noises(line)
        if not has_punctuation_p(line):
            print line
	
