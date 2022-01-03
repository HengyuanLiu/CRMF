#!/bin/bash
#52,86,104的错误都不在普通成员方法中。有不在方法中的，也有在构造函数中的。
# for i in  5 8 13 18 19 23 24 29 32 33 
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done
# for i in  23 24 29 32 33 
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

for i in `seq $1 $2` #4 6 11 22 71 77 98
do
	./averageNew.sh $i fail > Avg/failAvg-$i.txt
	./averageNew.sh $i pass > Avg/passAvg-$i.txt
done

# for i in {46..51}   #没有52
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

# for i in {53..61}   #没有52
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done


# for i in {71..85}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done


# for i in {87..103}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

# for i in {105..106}
# do
# 	./averageNew.sh $i fail > Avg/failAvg-$i.txt
# 	./averageNew.sh $i pass > Avg/passAvg-$i.txt
# done

# for i in 8 13 18 19 23 24 29 32 33 37 #8 13
# do
# 	./methodCount.sh $i 
# done

# for i in {38..44}
# do
# 	./methodCount.sh $i 
# done

# for i in {46..51}
# do
# 	./methodCount.sh $i 
# done

# for i in {53..61}
# do
# 	./methodCount.sh $i 
# done

# for i in {71..85}
# do
# 	./methodCount.sh $i 
# done

# for i in {87..103}
# do
# 	./methodCount.sh $i 
# done

# for i in {105..106}
# do
# 	./methodCount.sh $i 
# done