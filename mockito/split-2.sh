#!/bin/bash
#需要输入2个参数，第一个参数为需要分流为pass/fail的版本号 ，第二个参数为第一个测试用例集的名字，比如RetryRunnerTest

function Isfail(){
	tempFlag=0
	for line in `cat mockitoFailedTestsuites.txt | tr -d '\r'`
	do
		# echo $line
		if [ $tempFlag -eq 1 ];then

			if [[ $line =~ ^[0-9].* ]];then
				# echo $line
				echo "pass" #pass
				break;
			else
				if [[ $2 = $line ]];then
					# echo $line
					echo "fail" #fail
					break;
				fi
			fi
		fi

		if [ $1 = $line ];then
			tempFlag=1
		fi
	done
	
}


pro=mockito
i=$1
pf=$(Isfail $i $2) 

touch Yichuli/${pro}${i}-passTS.txt #pass----0
touch Yichuli/${pro}${i}-failTS.txt #fail----1
for line in ` cat Yichuli/${pro}$i.txt | tr -d '\r'`
do
	
	if [[ $line =~ .*\=.* ]];then
		echo ${line} >> Yichuli/${pro}${i}-${pf}TS.txt
	else
		pf=$(Isfail $i ${line})
		echo >> Yichuli/${pro}${i}-${pf}TS.txt
		echo ${line} >> Yichuli/${pro}${i}-${pf}TS.txt
		fi
done



