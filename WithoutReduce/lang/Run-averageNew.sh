#!/bin/bash

# for i in  {43..43}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

# for i in  {48..56}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

# for i in  {58..65}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

for i in  `seq $1 $2`
do
	./averageNew.sh $i fail > Avg/failAvg-$i.txt
	./averageNew.sh $i pass > Avg/passAvg-$i.txt
done
