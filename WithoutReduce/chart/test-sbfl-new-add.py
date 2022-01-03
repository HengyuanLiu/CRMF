# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import math

n = 0
sheet_name = []
# version = []
# sumOfTestsuites_num = []
with open('SumOfTestsuites-chart-fail.txt','r') as fileSOT:
	for lineSOT in fileSOT:
		lineSOT_arry = lineSOT.strip('\n').split(' ')
		sheet_name.append(lineSOT_arry[0]) 
		# version.append(sheet_name[n].split('chart')[1] )  #version就是版本号
		# sumOfTestsuites_num.append(lineSOT_arry[1]) 
		# print(sheet_name[n])
		# print(version[n])
		n = n + 1



def write_TFp_append(path,sheet_name): 
	# workbook = xlrd.open_workbook(path)
	index = len(sheet_name) 
	for t in range(0,index):
		workbook = xlrd.open_workbook(path)
		worksheet = workbook.sheet_by_name(sheet_name[t])
		rows_old = worksheet.nrows
		new_workbook = copy(workbook)
		new_worksheet = new_workbook.get_sheet(sheet_name[t])
		new_worksheet.write(0, 6, "Jaccard")
		new_worksheet.write(0, 8, "Ochiai")
		new_worksheet.write(0, 9, "Dstar")

		for row in range(1,rows_old):
			Jaccard = worksheet.cell_value(row,1)/(worksheet.cell_value(row,3)+worksheet.cell_value(row,2))
			if worksheet.cell_value(row,1) == 0:
				Ochiai = 0
			else:
				Ochiai = worksheet.cell_value(row,1)/math.sqrt(worksheet.cell_value(row,3)*(worksheet.cell_value(row,1)+worksheet.cell_value(row,2)))
			if worksheet.cell_value(row,2)+worksheet.cell_value(row,3)-worksheet.cell_value(row,1) == 0:
				Dstar = 200
			else:
				Dstar = (worksheet.cell_value(row,1)**3)/(worksheet.cell_value(row,2)+worksheet.cell_value(row,3)-worksheet.cell_value(row,1))
			op2 = worksheet.cell_value(row,1)-worksheet.cell_value(row,2)/( worksheet.cell_value(row,4) + 1)
			if worksheet.cell_value(row,1) == 0 and worksheet.cell_value(row,2) == 0 :
				Tarantula = 0
			else:
				Tarantula = (worksheet.cell_value(row,1)/worksheet.cell_value(row,3))/(worksheet.cell_value(row,1)/worksheet.cell_value(row,3)+worksheet.cell_value(row,2)/worksheet.cell_value(row,4))
			new_worksheet.write(row, 5, op2)
			new_worksheet.write(row, 6, Jaccard)
			new_worksheet.write(row, 7, Tarantula)
			new_worksheet.write(row, 8, Ochiai)
			new_worksheet.write(row, 9, Dstar)

		new_workbook.save(path)
		print(sheet_name[t] + "写入数据成功！")
	# workbook.save(path)  # 保存工作簿
	

book_name_xls = 'Test4-sbfl.xls'
write_TFp_append(book_name_xls, sheet_name)



