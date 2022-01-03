#!/bin/bash

pro=mockito
for method in `cat susMethod/susMethod$1.txt | tr -d '\r'`
do 

	echo $method `grep -c $method Yichuli/${pro}$1.txt` >> MC/MC-${pro}$1.txt
	echo $method `grep -c $method Yichuli/${pro}$1-failTS.txt` >> SBFL/ef-${pro}$1.txt
	echo $method `grep -c $method Yichuli/${pro}$1-passTS.txt` >> SBFL/ep-${pro}$1.txt
done

