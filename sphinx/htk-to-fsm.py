#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Usage: `basename $0` htk-lattice-file"
    exit 0
fi
file=$1
dirname=`dirname $file`
basename=$dirname/`basename $file .htk.lat`

lattice-tool -read-htk -in-lattice $file -out-lattice $basename.pfsg.lat
pfsg-to-fsm symbolfile=$basename.syms $basename.pfsg.lat > $basename.fsm.lat

#rm $basename.pfsg.lat
