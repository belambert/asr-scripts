#!/bin/bash

if [ $# != 2 ]; then
   echo "usage: $0 <hyp> <corr>"
   exit 1
fi

hyp=$1
corr=$2

#MACHINE=`~/bin/machine_type.csh`
align=/usr0/home/belamber/thesis/scripts/align
align=~/thesis/scripts/align

#$align -def $corr -hyp $hyp >&! $hyp.align
# Once to print to the screen
# $align -def $corr -hyp $hyp
# Second time to print to a file.
$align -def $corr -hyp $hyp > $hyp.align

grep -i accuracy $hyp.align

exit 0
