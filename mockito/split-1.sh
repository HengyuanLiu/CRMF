#!/bin/bash
#需要输入4个参数，前两个时版本号起始和末尾，第三是日志时间戳，比如1 5 09171923。第4个参数表示开始的测试类的名字，比如RetryRunnerTest
pro=mockito
i=$1
flag=0
for line in ` cat ${pro}${1}-${2}-output${3}.txt | tr -d '\r'`
do
	if [ $i -gt $2 ];then
		echo "$i > $2"
		break
	fi
	touch Yichuli/${pro}${i}.txt
	
			
	if [[ $line = $4 ]];then
		if [[ $flag -eq 0 ]];then
			flag=1
			echo $4 >> Yichuli/${pro}${i}.txt

		elif [[ $flag -eq 1 ]];then
			i=$(($i+1))
			echo $4 >> Yichuli/${pro}${i}.txt
		fi
	else

		if [[ $line =~ org\..*\=[0-9].* ]];then
			echo ${line#*org.mockito.} >> Yichuli/${pro}${i}.txt

		elif [[ ! $line =~ ^org.*\=M[0-9].* ]];then
			echo >> Yichuli/${pro}${i}.txt
			echo ${line#*org.mockito.} >> Yichuli/${pro}${i}.txt
			
		fi
	fi
done 