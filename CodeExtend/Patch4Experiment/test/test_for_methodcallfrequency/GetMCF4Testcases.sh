#!/usr/bin/env bash
# $1 version
# entity granularity: method
# test granularity: test suite
rm -rf ./MCF4Testcases.txt
rm -rf ./TimeoutTestsuite.txt
for testline in `cat ../test_for_testsuites/testcases.txt`;
do 
    echo ------------------------------------------------------ >> ./MCF4Testcases.txt
    echo "${testline}" >> ./MCF4Testcases.txt
    testsuite=${testline%::*}
    testcase=${testline#*::}
    cd ../../
    bash ./test/test_for_methodcallfrequency/GetMCF4SingleTestcase.sh $1 $testsuite $testcase
    cd ./test/test_for_methodcallfrequency
done
