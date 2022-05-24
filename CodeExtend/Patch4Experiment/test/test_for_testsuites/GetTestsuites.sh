# test extract the test suites of lang 1
cp ../../all_tests ./all_tests

sed -i 's/^.*(//g' all_tests
sed -i 's/)//g' all_tests
sort -u all_tests > testsuites.txt
rm -rf all_tests