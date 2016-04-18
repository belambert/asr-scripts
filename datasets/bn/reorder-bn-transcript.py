#!/usr/bin/python

import sys
import re
import string
import itertools

sphinx_file=sys.argv[1]
sphinx_lines = []

def noise_token_p(str):
    if len(str) > 1 and str[0] == '+' and str[1] == '+' and str[-1] == '+' and str[-2] == '+':
        return True
    if str[0] == '{' and str[-1] == '}':
        return True
    if str[0] == '[' and str[-1] == ']':
        return True
    if str[0] == '#' and str[-1] == '#':
        return True
    if str == "EH" or str == "UH" or str == "UM" or str == "((" or str == "))":
        return True

def remove_alt_pron(str):
    if str[-1] == ')' and str[-3] == '(':
        str = str[:-3]
    return str

# Read the Sphinx file -- try #2
for line in open(sphinx_file).readlines():
    m = re.match("(.*)\((.+)\)", line)
    trans = m.group(1)
    id = m.group(2)
    id_tokens = id.split("_")
    id_tokens[1] = int(id_tokens[1])
    id_tokens[2] = int(id_tokens[2])
    trans = trans.replace("<s> ", "")
    trans = trans.replace("<sil> ", "")
    trans = trans.replace(" </s>", "")
    trans = trans.upper()
    trans_tokens = trans.split()
    trans_tokens = filter(lambda x: not noise_token_p(x), trans_tokens)
    trans_tokens = map(remove_alt_pron, trans_tokens)
    trans = ' '.join(trans_tokens)
    sphinx_lines.append([id_tokens[0], id_tokens[1], id, trans])

sphinx_lines.sort(key=lambda x: x[1])
sphinx_lines.sort(key=lambda x: x[0])

for (id0, id1, id, trans) in sphinx_lines:
    print "%s (%s)"%(trans, id)

