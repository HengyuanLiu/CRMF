test_for_class
bash ./getAllclassName.sh gson 5

test_for_testsuites
bash ./GetTestsuites.sh

test_for_buggylines
bash get_buggy_lines.sh Gson 5 ./

test_for_method
bash ./GetMethod4Buggylines.sh ../../src/main/java/org/apache/commons/gson/archivers/zip/ZipArchiveInputStream.java 239

test_for_method_all
bash ./GetAllMethod.sh
<!-- java -classpath . -Dencoding=UTF-8 push.Getmethod org.apache.commons.gson.archivers.zip.AbstractUnicodeExtraField -->

test_for_testresults
bash ./GetFailedTestsuites.sh 

test_for_covinfo
1. test/test_for_buggylines/get_buggy_lines.sh
2. get sourelines FLD analysis java-parser
3. do what following:
mkdir -p /home/rs/Work/extract/gson_5_buggy/test/test_for_covinfo/covinfo; \
./job.sh \
--project Gson \
--bug 5 \
--output_dir /home/rs/Work/extract/gson_5_buggy/test/test_for_covinfo/covinfo \
--tool developer > /home/rs/Work/extract/gson_5_buggy/test/test_for_covinfo/log.txt 2>&1

<!-- mkdir -p gzoltars/Gson/5; \
./job.sh \
--project Gson \
--bug 5 \
--output_dir gzoltars/Gson/5 \
--tool developer > gzoltars/Gson/5/log.txt 2>&1 -->

test_for_methodcallfrequency

mvn clean package -DskipTests

cd ./test/test_for_methodcallfrequency
bash ./GetMCF.sh