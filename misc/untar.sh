#!/bin/sh

#tar_bin=bsdtar
tar_bin=tar

parallel=0

if [ $# -ne 0 ]; then
    files=$@
else
    files=`ls *.tar`
fi

echo "Untarring files:"
for file in $files; do
    echo "$file"
done


if [ $parallel -eq 1 ]; then
    # The "parallel" version...
    for file in $files; do
	    destination=results/`basename $file .tar`
	    if [ ! -e $destination ]; then
	        echo "Starting untar in background for file: $file"
	        nohup $tar_bin -xf $file &
	    fi
    done
else
    # This is the non-parallel version
    for file in $files; do
	    destination=results/`basename $file .tar`
	    #echo $destination
	    if [ ! -e $destination ]; then
	        echo "Working on $file..."
	        $tar_bin -xf $file
	    fi
    done
fi





