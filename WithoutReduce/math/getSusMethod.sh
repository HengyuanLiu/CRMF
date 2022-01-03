#!/bin/bash

for line in `cat Yichuli/math$1-failTS.txt | tr -d '\r' `
do
	if [[  $line =~ ^.*\=.* ]];then
		echo ${line%=*} >> susMethod-old/susMethod$1-t.txt
	fi
done

sort -u susMethod-old/susMethod$1-t.txt > susMethod-old/susMethod$1.txt
rm -rf susMethod-old/susMethod$1-t.txt