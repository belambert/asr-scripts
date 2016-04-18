#!/usr/bin/python

import sys

file = sys.argv[1]

line_counter = 0
sentence_counter = 1
lc_root_count = 0
uc_root_count = 0
total_count = 0
count_single_lc_only = 0
count_single_uc_only = 0
count_multiple_lc_only = 0
count_multiple_uc_only = 0
other = 0

for line in open(file):
    line = line[:-1]
    line_counter += 1
    if line == "":
        if lc_root_count == 1 and uc_root_count == 0:
            count_single_lc_only += 1

        elif lc_root_count == 0 and uc_root_count == 1:
            count_single_uc_only += 1

        elif lc_root_count > 1 and uc_root_count == 0:
            count_multiple_lc_only += 1

        elif lc_root_count == 0 and uc_root_count > 1:
            count_multiple_uc_only += 1

        else:
            other += 1

        if lc_root_count + uc_root_count != 1:
            print "#LC root = %d   #UC root = %d   (line: %d, sent: %d)"%(lc_root_count, uc_root_count, line_counter, sentence_counter)

        total_count += 1

        lc_root_count = 0
        uc_root_count = 0
        sentence_counter += 1
    else:
        tokens = line.split()
        if tokens[7] == 'ROOT':
            uc_root_count += 1
        if tokens[7] == 'root':
            lc_root_count += 1

print "%s\t\t%s"%('total_count', total_count)
print""
print "%s\t\t%s"%('count_single_lc_only', count_single_lc_only)
print "%s\t\t%s"%('count_single_uc_only', count_single_uc_only)
print""
print "%s\t\t%s"%('count_multiple_lc_only', count_multiple_lc_only)
print "%s\t\t%s"%('count_multiple_uc_only', count_multiple_uc_only)
print""
print "%s\t\t%s"%('other', other)



