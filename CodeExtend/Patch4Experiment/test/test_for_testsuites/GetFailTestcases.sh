cp ../../failing_tests ./failing_tests
rm -rf ./failtestcases.txt
for line in `cat ./failing_tests | tr -d '\r'`
do 
    if [[ $line =~ "::" ]]; then
        testline=${line#*\ }
        testsuite=${testline%::*}
        testcase=${testline#*::}
        echo ${testsuite}::${testcase} >> ./failtestcases.txt
    fi
done
rm -rf ./failing_tests