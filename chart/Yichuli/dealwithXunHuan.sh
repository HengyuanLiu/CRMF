#!/bin/bash



for i in `ls .`
do
	if [[ $i =~ chart[0-9].*.txt ]];then
		for line in `cat $i`
		do
			if [[ $line =~ .*=.* ]] && [[ ${line#*=} -gt 70 ]];then
				num=${line#*=}
				num=$(($num/70))
				echo ${line%=*}=$num >> ../Yichuli-new/$i
			else
				echo $line >> ../Yichuli-new/$i
			fi
		done
	fi
done

