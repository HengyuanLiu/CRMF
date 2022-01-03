#!/bin/bash
average_sum=0
average_n=0
for i in `ls .`
do
	if [[ ! $i =~ chart[0-9].*-.*TS.txt ]] &&  [[  $i =~ chart[0-9].*.txt ]] ;then
		n=0
		all=0
		for line in `cat $i`
		do
			if [[ $line =~ .*=.* ]];then
				num=${line#*=}
				if [[ $num -ge ${1} ]];then
					n=$(($n+1))
				fi
				all=$(($all+1))
			fi
		done
		average=`echo "scale=10;$n/$all" | bc`
		average_sum=`echo "$average_sum + $average" | bc`
		average_n=$(($average_n+1))
	fi
done
echo ${1} `echo "scale=10;$average_sum/$average_n" | bc` >> finalAns.txt