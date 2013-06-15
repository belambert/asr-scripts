#!/usr/bin/python

import sys
import string
import blambert_util as bl

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

#remove_punc_p = True
remove_punc_p = False

discard_punctuated_sentences = True

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines:
    tokens = line.split()
    new_tokens = []
    eligible_sentence = True
    for token in tokens[:-1]:
        # If it's a noise marker, ignore it.
        if token.startswith('++') and token.endswith('++'):
            pass
        # If it's punctuation, normalize it
        elif token[0] in string.punctuation:
            if discard_punctuated_sentences:
                eligible_sentence = False
            elif not remove_punc_p:
                new_token = string.join([' ' if x in string.punctuation else x for x in token], "")
                new_token = new_token.split()
                for token_part in new_token:
                    new_tokens.append(token_part)
        # O/w it's a normal word
        else:
            # We don't want to remove all punctuation... just the trailing punctuation...
            # Actually, we'll just remove a trailing period (as in MR. MRS. U. S. A.)
            if token[-1] == '.':
                token = token[:-1]                
            new_tokens.append(token)
    new_tokens.append(tokens[-1])

    
    if eligible_sentence and len(new_tokens) > 1:
        line = string.join(new_tokens, ' ')
        # replace any ".'" with just an apostrophe
        line.replace(".'", "'")
        print line
