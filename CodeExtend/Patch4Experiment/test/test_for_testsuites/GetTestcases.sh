# test extract the test suites of lang 1
cp ../../all_tests ./all_tests
rm -rf ./testcases.txt
for line in `cat ./all_tests`
do 
    testcase=${line%%\(*}
    testsuite=${line#*\(}
    testsuite=${testsuite%\)*}
    echo ${testsuite}::${testcase} >> ./testcases.txt
done
rm -rf all_tests
