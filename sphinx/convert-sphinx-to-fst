#!/usr/bin/python

import sys,os
#import lattice
from lattice import *

###############################################################
### I/O #######################################################
###############################################################

### Get the file names from the command line
if len(sys.argv) < 2:
    print 'Usage: %s <sphinx lattice>+ ' % sys.argv[0]
    exit()

for sphinx_file in sys.argv[1:]:
    print "Converting %s"%sphinx_file
    # Create an instance of this class -- can pass more information through constructor variables
    # dag = lattice.Dag()
    dag = Dag()

    # Loads a lattice file into the DAG - can be either gzipped or just a .lat lattice file
    dag.sphinx2dag(sphinx_file)
    dag.dag2fsa(sphinx_file+".fst")




