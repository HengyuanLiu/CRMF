#!/bin/bash

for line in `cat susMethod-old/susMethod$1.txt | tr -d '\r' `
do
	if [[ ! ${line%.*} =~ .*\$.* ]];then
		echo ${line%.*} >> susClass/susClass$1-t.txt
	fi
done

sort -u susClass/susClass$1-t.txt > susClass/susClass$1.txt
rm -rf susClass/susClass$1-t.txt