#!/bin/bash
pro=lang
for line in `cat Yichuli/${pro}$1-failTS.txt | tr -d '\r' `
do
	if [[  $line =~ ^.*\=.* ]];then
		if [[ ! $line =~ .*\$.* ]];then
			echo ${line%=*} >> susMethod/susMethod$1-t.txt
		fi
	fi
done

sort -u susMethod/susMethod$1-t.txt > susMethod/susMethod$1.txt
rm -rf susMethod/susMethod$1-t.txt