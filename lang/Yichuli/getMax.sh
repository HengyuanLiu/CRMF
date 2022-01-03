#!/bin/bash

for i in `ls .`
do
	if [[ ! $i =~ lang[0-9].*-.*TS.txt ]] &&  [[  $i =~ lang[0-9].*.txt ]] ;then
		max=0
		n=0
		all=0
		for line in `cat $i`
		do
			if [[ $line =~ .*=.* ]];then
				num=${line#*=}
				if [[ $num -ge 700 ]];then
					n=$(($n+1))
				fi
				# if [[ $num -gt $max ]];then
				# 	max=$num
				# fi
				all=$(($all+1))
			fi
		done
		# echo $i $max >> Max.txt
		echo $i $n $all   `echo "scale=10;$n/$all" | bc` >> CountforOver700.txt
		
	fi
done
