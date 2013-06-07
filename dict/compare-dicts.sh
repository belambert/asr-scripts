#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print "Usage: %s <dict1> <dict2>"%sys.argv[0]
    exit(-1)


dict_file1 = sys.argv[1]
dict_file2 = sys.argv[2]

dict_table = {}
dict_table_coverage = {}

def remove_alt_pron(str):
    if str[-1] == ')' and str[-3] == '(':
        str = str[:-3]
    return str

def line_to_canonical_tuple(line):
    tokens = line.split()
    tokens[0] = remove_alt_pron(tokens[0])
    tokens_tuple = tuple(tokens)
    return tokens_tuple

for line in open(dict_file1):
    if len(line) > 0:
        line_tuple = line_to_canonical_tuple(line)
        dict_table[line_tuple] = True

dict1_not_in_dict2_count = 0
dict2_not_in_dict1_count = 0

for line in open(dict_file2):
    if len(line) > 0:
        line_tuple = line_to_canonical_tuple(line)
        if dict_table.get(line_tuple):
            dict_table_coverage[line_tuple] = True
        else:
            print "Dict2 entry not in dict1: %s"%str(line_tuple)
            dict2_not_in_dict1_count += 1

for line_tuple in dict_table.keys():
    if not dict_table_coverage.get(line_tuple):
        print "Dict1 entry not in dict2: %s"%str(line_tuple)
        dict1_not_in_dict2_count += 1    

print "# of dict1 not in dict2: %d"%dict1_not_in_dict2_count
print "# of dict2 not in dict1: %d"%dict2_not_in_dict1_count



