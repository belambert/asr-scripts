#!/bin/sh

folder=$1

cd $folder

printp -gaufn means > means.txt
printp -mixwfn mixture_weights > mixture_weights.txt
printp -tmatfn transition_matrices > transition_matrices.txt
printp -gaufn variances > variances.txt

cd -
