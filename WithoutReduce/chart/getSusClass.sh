#!/bin/bash

for line in `cat susMethod/susMethod$1.txt | tr -d '\r' `
do
	echo ${line%.*} >> susClass/susClass$1-t.txt
done

sort -u susClass/susClass$1-t.txt > susClass/susClass$1.txt
rm -rf susClass/susClass$1-t.txt