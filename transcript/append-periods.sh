#!/bin/sh

awk ' { printf("%s .", $0); print(""); }' $1 
