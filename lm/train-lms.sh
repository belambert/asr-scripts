#!/bin/sh

#echo "Counting the raw n-gram LMs..."
#ngram-count -sort -text lm-train-np-unique.txt -order 3 -vocab vocab-np-20k.txt -lm lm-3gram-20k-np.lm
#ngram-count -sort -text lm-train-np-unique.txt -order 3 -vocab vocab-np-64k.txt -lm lm-3gram-64k-np.lm
#ngram-count -sort -text lm-train-vp-unique.txt -order 3 -vocab vocab-vp-20k.txt -lm lm-3gram-20k-vp.lm
#ngram-count -sort -text lm-train-vp-unique.txt -order 3 -vocab vocab-vp-64k.txt -lm lm-3gram-64k-vp.lm

#ngram-count -sort -text lm-train-np.txt -order 3 -lm lm-3gram-np.lm -write-vocab vocab-np-all.txt
#ngram-count -sort -text lm-train-vp.txt -order 3 -lm lm-3gram-vp.lm -write-vocab vocab-vp-all.txt

#echo "Interpolating the models that include punctuation vs. those that don't..."
#ngram -vocab vocab-20k-nvp.txt -lm lm-3gram-20k-nvp.lm -mix-lm lm-3gram-20k-vp.lm -lambda 0.5 -write-lm lm-3gram-20k-interp.lm
#ngram -vocab vocab-64k-vp.txt -lm lm-3gram-64k-nvp.lm -mix-lm lm-3gram-64k-vp.lm -lambda 0.5 -write-lm lm-3gram-64k-interp.lm

echo "Adding dummy backoff weights..."
for file in `ls *.lm`; do echo $file; add-dummy-bows $file > `basename $file .lm`.bow.lm; done

echo "Sorting LMs..."
for file in `ls *.bow.lm`; do echo $file; sort-lm $file > `basename $file .lm`.sorted.lm; done

#echo "Converting to binary lm 'dmp' format..."
#for lm in `ls *.bow.sorted.lm`; do echo $lm; lm3g2dmp $lm .; done