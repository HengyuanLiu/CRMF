#!/bin/bash



for i in `ls .`
do
	if [[ $i =~ time[0-9].*.txt ]];then
		for line in `cat $i`
		do
			if [[ $line =~ .*=.* ]] && [[ ${line#*=} -gt 70000 ]];then
				num=${line#*=}
				num=$(($num/70000))
				echo ${line%=*}=$num >> ../Yichuli-new/$i
			else
				echo $line >> ../Yichuli-new/$i
			fi
		done
	fi
done

