#!/bin/bash

# for i in  {2..10}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

for i in `seq $1 $2`
do
	./averageNew.sh $i fail > Avg/failAvg-$i.txt
	./averageNew.sh $i pass > Avg/passAvg-$i.txt
done
