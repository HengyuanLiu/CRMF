cd ../../gson
mvn clean package -Dmaven.test.skip=true -X -Dmaven.javadoc.skip=true -Dcommons.animal-sniffer.version=1.14 > ../test/test_for_methodcallfrequency/MvnCompile-log.txt 2>&1
cd ../test/test_for_methodcallfrequency