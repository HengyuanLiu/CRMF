#!/bin/bash

# echo "./split-1.sh 71 99 09190906 org.apache.commons.math.ArgumentOutsideDomainExceptionTest"
# ./split-1.sh 71 99 09190906 org.apache.commons.math.ArgumentOutsideDomainExceptionTest
# echo "./split-1.sh 100 100 09191551 org.apache.commons.math.ArgumentOutsideDomainExceptionTest"
# ./split-1.sh 100 100 09191551 org.apache.commons.math.ArgumentOutsideDomainExceptionTest
# echo "./split-1.sh 101 101 09190949 org.apache.commons.math.ArgumentOutsideDomainExceptionTest"
# ./split-1.sh 101 101 09190949 org.apache.commons.math.ArgumentOutsideDomainExceptionTest
# echo "./split-1.sh 102 104 09191019 org.apache.commons.math.ArgumentOutsideDomainExceptionTest"
# ./split-1.sh 102 104 09191019 org.apache.commons.math.ArgumentOutsideDomainExceptionTest
# echo "./split-1.sh 105 106 09191019 org.apache.commons.math.FunctionEvaluationExceptionTest"
# ./split-1.sh 105 106 09191019 org.apache.commons.math.FunctionEvaluationExceptionTest


# for i in {71..104}
# do
# 	./split-2.sh $i ArgumentOutsideDomainExceptionTest
# done

# for i in 105 106
# do
# 	./split-2.sh $i FunctionEvaluationExceptionTest
# done

for i in {37..61}
do
	./split-2.sh $i MathExceptionTest
done