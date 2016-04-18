#!/usr/bin/python

import sys
import os
import blambert_util as bl

if len(sys.argv) != 3:
    print "Usage: %s <id file> <folder>"%os.path.basename(sys.argv[0])
    exit(1)

id_file = sys.argv[1]
folder = sys.argv[2]

# Read in the ID's
with open(id_file) as f:
    ids = f.readlines()

# Put all the ID's in a hash table
id_table = {}
for id in ids:
    id = id.strip()
    id_table[id] = True

# List the files in the given folder...
files = os.listdir(folder)
files = filter(lambda x: x.endswith(".nbest"), files)

print "Number of files: %s"%len(files)

# Count what we need to delete...
in_table_count = 0
not_in_table_count = 0
ids_to_delete = []

for file in files:
    file = file.replace(".nbest", "")
    if id_table.get(file):
        in_table_count += 1
    else:
        not_in_table_count += 1
        ids_to_delete.append(file)

print "IDs to be deleted: %s"%ids_to_delete
print "IDs to keep: %s"%in_table_count
print "IDs to delete: %s"%not_in_table_count

# Confirm that we want to delete all of these...?!?!
if bl.ask_ok("OK to delete %d n-best lists?"%not_in_table_count, retries=4, complaint='Yes or no, please!'):
    # Do the actual deletion...
    for id in ids_to_delete:
        for suffix in [".nbest", ".nbest.2tag", ".nbest.2tag.tagged", ".nbest.scores"]:
            filename = folder + "/" + id + suffix
            #print filename
            #os.delete(filename)
            os.remove(filename)

print "Finished."
