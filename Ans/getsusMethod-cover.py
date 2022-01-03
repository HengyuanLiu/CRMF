import xlwt
import xlrd
from xlutils.copy import copy

import sys

prom = sys.argv[1]

n = 0
sheet_name = []
version = []
sumOfTestsuites_num = []
with open('../'+prom+'/SumOfTestsuites-'+prom+'.txt','r') as fileSOT:
    for lineSOT in fileSOT:
        lineSOT_arry = lineSOT.strip('\n').split(' ')
        sheet_name.append(lineSOT_arry[0]) 
        version.append(sheet_name[n].split(prom)[1] )  #version[1]就是版本号
        sumOfTestsuites_num.append(lineSOT_arry[1]) 
        # print(sheet_name[n])
        # print(version[n])
        n = n + 1

method = []
index = len(sheet_name)
for t in range(0,index):
    workbook = xlrd.open_workbook(prom+'5-2-withcolour.xls')
    worksheet = workbook.sheet_by_name(sheet_name[t])
    nrows = worksheet.nrows
    for row in range(1,nrows):
        # method.append(worksheet.cell_value(row,0))
        with open("../"+prom+"/susClass-cover/"+sheet_name[t]+'.txt','a') as fileW:
            fileW.write(str(worksheet.cell_value(row,0)))
            fileW.write("\n")
