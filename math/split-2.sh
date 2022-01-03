#!/bin/bash
#需要输入2个参数，第一个参数为需要分流为pass/fail的版本号 ，第二个参数为第一个测试用例集的名字，比如RetryRunnerTest

function Isfail(){
	tempFlag=0
	for line in `cat mathFailedTestsuites.txt | tr -d '\r'`
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


# #以org.apache.commons.math.ArgumentOutsideDomainExceptionTest为开始的测试用例集
# i=$1
# pf=$(Isfail $i "ArgumentOutsideDomainExceptionTest")

# touch Yichuli/math${i}-passTS.txt #pass----0
# touch Yichuli/math${i}-failTS.txt #fail----1
# for line in ` cat Yichuli/math$i.txt | tr -d '\r'`
# do
	
# 	if [[ $line =~ .*\=.* ]];then
# 		echo $line >> Yichuli/math${i}-${pf}TS.txt
# 	else
# 		pf=$(Isfail $i $line)
# 		echo >> Yichuli/math${i}-${pf}TS.txt
# 		echo $line >> Yichuli/math${i}-${pf}TS.txt
# 		fi
# done


i=$1
pf=$(Isfail $i $2) #适用于math37以后版本

touch Yichuli/math${i}-passTS.txt #pass----0
touch Yichuli/math${i}-failTS.txt #fail----1
for line in ` cat Yichuli/math$i.txt | tr -d '\r'`
do
	
	if [[ $line =~ .*\=.* ]];then
		echo ${line} >> Yichuli/math${i}-${pf}TS.txt
	else
		pf=$(Isfail $i ${line})
		echo >> Yichuli/math${i}-${pf}TS.txt
		echo ${line} >> Yichuli/math${i}-${pf}TS.txt
		fi
done



