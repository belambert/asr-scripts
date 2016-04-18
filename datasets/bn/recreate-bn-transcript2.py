#!/usr/bin/python

import sys
import re
import string
import itertools

sphinx_file=sys.argv[1]
ldc_file=sys.argv[2]

ldc_lines = []
sphinx_lines = []

ldc_tokens = []
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
    

# Read the LDC file
for line in open(ldc_file).readlines():    
   if not line[0] == "<":
       line = line[:-1]
       line = line.upper()
       line = line.replace("_", " ")
       line = line.replace("-", " ")
       
       tokens = line.split()
       tokens = filter(lambda x: not noise_token_p(x), tokens)
       ldc_lines.append(line)
       ldc_tokens.extend(tokens)

# Read the Sphinx file -- try #1
# for line in open(sphinx_file).readlines():
#     line = line[:-1]
#     tokens = line.split()
#     tokens = tokens[:-1]
#     sphinx_lines.append(line)
#     sphinx_tokens.extend(tokens)

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
    sphinx_lines.append([id_tokens[0], id_tokens[1], id, trans_tokens])

sphinx_lines.sort(key=lambda x: x[1])
sphinx_lines.sort(key=lambda x: x[0])

sphinx_tokens = map(lambda x: x[3], sphinx_lines)
#sphinx_tokens = sum(sphinx_lines, [])
print sphinx_tokens[0:10]
sphinx_tokens = list(itertools.chain(*sphinx_tokens))

print "LDC tokens: %d"%len(ldc_tokens)
print "Sphinx tokens: %d"%len(sphinx_tokens)

print "LDC tokens: %s"%ldc_tokens[0:10]
print "Sphinx tokens: %s"%sphinx_tokens[0:10]

error_token = None

for i in range(0,len(ldc_tokens)):
    ldc_token = ldc_tokens[i]
    sphinx_token = sphinx_tokens[i]
    if ldc_token != sphinx_token:
        print "LDC: %s  Sphinx: %s"%(ldc_token, sphinx_token)
        error_token = i
        break                         

if error_token:
    for i in range(error_token - 10, error_token + 10):
        if i == error_token:
            print "***%3d LDC: %20s Sphinx: %20s***"%(i, ldc_tokens[i], sphinx_tokens[i])
        else:
            print "   %3d LDC: %20s Sphinx: %20s"%(i, ldc_tokens[i], sphinx_tokens[i])
