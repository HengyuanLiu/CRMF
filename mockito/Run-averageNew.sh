#!/bin/bash

# for i in  4 6
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

# for i in  {9..17}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

# for i in  {4..33}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

# for i in  6
# do
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

for i in  `seq $1 $2`
do
	./averageNew.sh $i fail > Avg/failAvg-$i.txt
	./averageNew.sh $i pass > Avg/passAvg-$i.txt
done