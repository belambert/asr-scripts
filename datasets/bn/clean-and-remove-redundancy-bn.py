#!/usr/bin/python

import sys
import re
import string
import itertools

sphinx_file=sys.argv[1]
sphinx_lines = []
sphinx_tokens = []


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
    trans = trans.replace("-", " ")
    trans = trans.replace(".", "")
    trans_tokens = trans.split()
    trans_tokens = filter(lambda x: not noise_token_p(x), trans_tokens)
    trans_tokens = map(remove_alt_pron, trans_tokens)
    sphinx_lines.append([id_tokens[0], id_tokens[1], id_tokens[2], id, trans_tokens])

sphinx_lines.sort(key=lambda x: x[1])
sphinx_lines.sort(key=lambda x: x[0])


prev_end = 0
prev_filename = None

for i in range(len(sphinx_lines)):
    line = sphinx_lines[i]
    filename = line[0]
    begin = line[1]
    end = line[2]
    if begin + 4 < prev_end and filename == prev_filename:
        sphinx_lines[i] = None
    else:
        prev_end = end
        prev_filename = filename

sphinx_lines = filter(lambda x: x != None, sphinx_lines)

for line in sphinx_lines:
    id = line[3]
    tokens = line[4]
    if len(tokens) > 0:
        print "%s (%s)"%(' '.join(tokens), id)


