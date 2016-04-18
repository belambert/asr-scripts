#!/usr/bin/python

import sys,os
#import lattice
from lattice import *
from lattice_ben import *
import subprocess

###############################################################
### I/O #######################################################
###############################################################

### Get the file names from the command line
if len(sys.argv) < 2:
    print 'Usage: %s <sphinx lattice>+ ' % sys.argv[0]
    exit()

#pruning_weight="%s"%100000
#pruning_weight=sys.argv[1]

for file in sys.argv[1:]:
    print "Reading file %s"%file
    # Create an instance of this class -- can pass more information through constructor variables
    dag = Dag()

    # Loads a lattice file into the DAG - can be either gzipped or just a .lat lattice file
    if file.endswith(".s3.lat"):
        dag.sphinx2dag(file)
    elif file.endswith(".htk.lat"):
        dag.htk2dag(file)
    elif file.endswith(".fsm.lat"):
        dag.fsm2dag(file)
    else: print "Error, unknown filetype."
    dag.remove_unreachable()
    
    fst_file=file+".fst"
    syms_file=file+".syms"

    print "Saving in FST format"
    dag.dag2fsa(fst_file, syms_file)    
    binary_fst=file+".bin.fst"
    det_fst=file+".det.fst"

    print "Compiling to binary FST: %s"%binary_fst
    subprocess.call(["fstcompile", "--acceptor","--keep_isymbols", "--keep_osymbols", "--isymbols=" + syms_file, fst_file, binary_fst])

    subprocess.call(["fstinfo", binary_fst])

    print "Determinizing: %s"% det_fst
    subprocess.call(["fstdeterminize", binary_fst, det_fst])
    subprocess.call(["fstinfo", det_fst])

    print "Drawing..."
    subprocess.call(["fstdraw", "--acceptor", "--isymbols=" + syms_file, binary_fst, file + ".dot"])
    subprocess.call(["fstdraw", "--acceptor", "--isymbols=" + syms_file, det_fst, file + ".det.dot"])

    print "Plotting postscript..."
    with open(file + ".ps","w") as f:
        p = subprocess.Popen(["dot", "-Tps", file + ".dot"], stdout=f)
        time.sleep(10.0)
        if p.poll() is None:
            time.sleep(20.0)
            if p.poll() is None:
                p.kill()
                print "Dot could not complete in time."
    with open(file + ".det.ps","w") as f:
        p = subprocess.Popen(["dot", "-Tps", file + ".det.dot"], stdout=f)
        time.sleep(10.0)
        if p.poll() is None:
            time.sleep(20.0)
            if p.poll() is None:
                p.kill()
                print "Dot could not complete in time."

    os.remove(fst_file)
    os.remove(syms_file)
    os.remove(binary_fst)
    os.remove(det_fst)
    os.remove(file + ".dot")
    os.remove(file + ".det.dot")

    #subprocess.call(["fstinfo", binary_fst])
    #subprocess.call(["fstinfo", det_fst]) 
    #subprocess.call(["fstprune", "--weight="+pruning_weight, binary_fst, pruned_fst])



