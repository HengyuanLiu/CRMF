#!/bin/bash
IFS=$'\n'
for i in `ls .`
do
	if [[ $i =~ math.*.txt ]];then
		for line in `cat $i | tr -d '\r' `
		do
			if [[ $line =~ .*=.* ]];then
				if [[ ${line#*=} -ge 1000 ]];then
					num=${line#*=}
					num=`echo "scale=5;$num/1000" | bc`
					if [[ `echo "$num > 999" | bc` -eq 1  ]];then
						num=`echo "scale=5;$num/1000" | bc`
					fi
					echo ${line%=*}=$num >> ${i%.txt*}-t.txt
				else
					echo  $line >> ${i%.txt*}-t.txt
				fi
			else
				echo  $line >> ${i%.txt*}-t.txt
			fi
		done
	fi
done

