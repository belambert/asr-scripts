#!python

import sys

filename = sys.argv[1]

def remove_numbers(str):    
    return filter(lambda x: not x.isdigit(), str)

for line in open(filename):
    tokens = line.split()    
    word = tokens[0]
    word = word.lower()
    phones = tokens[1:]
    # Remove the numbers from the phones
    phones = map(remove_numbers, phones)
    phone_string = ' '.join(phones)
    phone_string = phone_string.upper()
    print "%s\t%s"%(word, phone_string)
        
    
