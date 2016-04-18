#!/usr/bin/python

import sys

file = sys.argv[1]

dis_list = ['UM', 'UH-HUM', 'UH', 'UH-HUH', 'HUH', 'UH-HUM', 'UH-UH', 'UH-OH', 'UH-', 'HUH-UH',
            'UHUH', 'YUH', 'UM-HUH', 'BUH', 'NUH', 'UHM', 'UH-AH', 'UH-HU', 'EUH', 'MH-UH', 'HUH', 'U-HUH', 'DUH',
            'MHM',  'UMM', 'UM-HUM', 'UMHUM', 'UM-', 'DUH-', 'UH-HU-', 'HUH-HUM', 'HUH-', 
            'UHHH', "'UH-UH'", 'MH-UH', 'PUH-', 'UHF', '-HUH', 'AHUH', 'UH-HM',
            'HM', 'HMM', 'M-HM', 'UHM', 'MM-HM', 'HM-HM', 'HMH', 'HM-MM', 'MHMH', "'HM",
            'UH-HUHS', 'HUH-HUH',
            'MM', 'ERM']

for line in open(file):
    tokens = line.split()
    for i in range(len(tokens)):
        token = tokens[i]
        if token in dis_list:
            tokens[i] = "++%s++"%token
        if token[0] == '[' and token[-1] == ']':
            tokens[i] = "++%s++"%token[1:-1]
    new_line = ' '.join(tokens)
    print new_line
    
