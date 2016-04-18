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
       line = line.replace("{", " ")
       line = line.replace("}", " ")       
       line = line.replace("[", " ")
       line = line.replace("]", " ")
       tokens = line.split()
       tokens = filter(lambda x: not noise_token_p(x), tokens)
       ldc_lines.append(line)
       ldc_tokens.extend(tokens)

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
    trans_tokens = trans.split()
    trans_tokens = filter(lambda x: not noise_token_p(x), trans_tokens)
    trans_tokens = map(remove_alt_pron, trans_tokens)
    sphinx_lines.append([id_tokens[0], id_tokens[1], id_tokens[2], id, trans_tokens])

sphinx_lines.sort(key=lambda x: x[1])
sphinx_lines.sort(key=lambda x: x[0])


prev_end = 0
prev_filename = None

print "BEFORE: %d"%len(sphinx_lines)

#for line in sphinx_lines:
for i in range(len(sphinx_lines)):
    line = sphinx_lines[i]
    filename = line[0]
    begin = line[1]
    end = line[2]
    if begin + 4 < prev_end and filename == prev_filename:
        #print prev_end
        #print prev_filename
        #print line
        #sphinx_lines.remove(line)
        sphinx_lines[i] = None
    else:
        prev_end = end
        prev_filename = filename

sphinx_lines = filter(lambda x: x != None, sphinx_lines)

print "AFTER: %d"%len(sphinx_lines)

sphinx_tokens = map(lambda x: x[4], sphinx_lines)
print sphinx_tokens[0:10]
sphinx_tokens = list(itertools.chain(*sphinx_tokens))

print "LDC tokens: %d"%len(ldc_tokens)
print "Sphinx tokens: %d"%len(sphinx_tokens)

print "LDC tokens: %s"%ldc_tokens[0:10]
print "Sphinx tokens: %s"%sphinx_tokens[0:10]

remove_char_set = ["@", "*", "\"", "!", "^", ",", ".", "%", "?", "+", "'"]

def fuzzy_string_match(str1, str2):
    for char in remove_char_set:
        str1 = str1.replace(char, "")
        str2 = str2.replace(char, "")
    return str1 == str2


ldc_matches=[None]*len(sphinx_tokens)

error_token = None
ldc_index = 0
sphinx_index = 0

count_limit = 1597896
non_match_limit = 5000
sphinx_total = len(sphinx_tokens)
while ldc_index < count_limit:
    sphinx_token = sphinx_tokens[sphinx_index]
    ldc_token = ldc_tokens[ldc_index]
    

    if fuzzy_string_match(ldc_token, sphinx_token):
        ldc_index += 1
        sphinx_index += 1
        ldc_matches[sphinx_index] = ldc_token
        print "   MATCH: %25s == %25s    (%d of %d)"%(sphinx_token, ldc_token, sphinx_index, sphinx_total)
    else:
        non_match_counter = 0
        while not fuzzy_string_match(ldc_token, sphinx_token) and ldc_index < count_limit:
            print "NO MATCH: %25s != %25s    (%d of %d)"%(sphinx_token, ldc_token, sphinx_index, sphinx_total)
            ldc_index += 1
            ldc_token = ldc_tokens[ldc_index]
            non_match_counter += 1
            if non_match_counter > non_match_limit:
                print "Stopping due to more than %d consecutive non-matches!"%non_match_limit
                quit()
        print "   MATCH: %25s == %25s    (%d of %d)"%(sphinx_token, ldc_token, sphinx_index, sphinx_total)
        sphinx_index += 1
        ldc_index += 1
        ldc_matches[sphinx_index] = ldc_token

print "LDC index:    %d"%ldc_index
print "Sphinx index: %d"%sphinx_index
