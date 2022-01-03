# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import math
 
n = 0
sheet_name = []
version = []
sumOfTestsuites_num = []
with open('SumOfTestsuites-mockito-fail.txt','r') as fileSOT:
	for lineSOT in fileSOT:
		lineSOT_arry = lineSOT.strip('\n').split(' ')
		sheet_name.append(lineSOT_arry[0]) 
		version.append(sheet_name[n].split('mockito')[1] )  #version[1]就是版本号
		sumOfTestsuites_num.append(lineSOT_arry[1]) 
		# print(sheet_name[n])
		# print(version[n])
		n = n + 1
n = 0
total_p = []
with open("SumOfTestsuites-mockito.txt",'r') as file:
	for line in file:
		line_name = line.strip('\n').split(' ')
		total_p.append(int(line_name[1]) - int(sumOfTestsuites_num[n]))
		n = n + 1 



#------------------建表
def write_excel_xls(path, sheet_name, title):
	index = len(sheet_name)  # 获取需要写入sheet个数
	workbook = xlwt.Workbook()  # 新建一个工作簿
	for t in range(0,index):
		sheet = workbook.add_sheet(sheet_name[t])  # 在工作簿中新建一个表格
		for j in range(0, len(title[0])):
			sheet.write(0, j, title[0][j])
	workbook.save(path)  # 保存工作簿
	print("xls格式表格写入数据成功！")


def write_TFp_append(path,sheet_name,version): 
	# workbook = xlrd.open_workbook(path)
	index = len(sheet_name) 
	for t in range(0,index):
		workbook = xlrd.open_workbook(path)
		worksheet = workbook.sheet_by_name(sheet_name[t])
		rows_old = worksheet.nrows
		new_workbook = copy(workbook)
		new_worksheet = new_workbook.get_sheet(sheet_name[t])

		Filename = "Avg/passAvg-" + version[t] + ".txt"
		target = 1
		with open(Filename,'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				# print("%s |" % line_name[1] )
				new_worksheet.write(target, 0, line_name[0])
				new_worksheet.write(target, 1, float('0' + line_name[2]))
				new_worksheet.write(target, 2, (float('0' + line_name[2])+1))
				if float('0' + line_name[2]) == 0:
					new_worksheet.write(target, 3, 0.000000000001)
				else:
					new_worksheet.write(target, 3, float(line_name[2]))
				target = target + 1
		Filename = "Avg/failAvg-" + version[t] + ".txt"
		target = 1
		with open(Filename,'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				# print("%s |" % line_name[1] )
				new_worksheet.write(target, 4, float('0' + line_name[2]))
				if float('0' + line_name[2]) == 0:
					new_worksheet.write(target, 5, 0.000000000001)
				else:
					new_worksheet.write(target, 5, float('0' + line_name[2]))
				target = target + 1

		Filename = "SBFL/ef-" + sheet_name[t] + ".txt"
		target = 1
		with open(Filename,'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				# print("%s |" % line_name[1] )
				if line_name[1] == "0":
					line_name[1] = 0.000000000001
				new_worksheet.write(target, 7, float(line_name[1]))
				target = target + 1
		Filename = "SBFL/ep-" + sheet_name[t] + ".txt"
		target = 1
		with open(Filename,'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				if line_name[1] == "0":
					line_name[1] = 0.000000000001
				new_worksheet.write(target, 6, float(line_name[1]))
				new_worksheet.write(target, 9, int(sumOfTestsuites_num[t]))
				new_worksheet.write(target, 8, total_p[t])
				IDFp = math.log10(int(total_p[t]) / float(line_name[1]))
				new_worksheet.write(target, 10, IDFp)
				target = target + 1
		new_workbook.save(path)

		workbook = xlrd.open_workbook(path)
		worksheet = workbook.sheet_by_name(sheet_name[t])
		new_workbook = copy(workbook)
		new_worksheet = new_workbook.get_sheet(sheet_name[t])
		rows_old = worksheet.nrows
		# print(rows_old)
		for row in range(1,rows_old):
			IDFf = math.log10(worksheet.cell_value(row,9) / worksheet.cell_value(row,7))
			if IDFf == 0:
				IDFf = 0.01
			value_min = worksheet.cell_value(row,5) * worksheet.cell_value(row,10) / (worksheet.cell_value(row,3) * IDFf )
			value_plus1 = worksheet.cell_value(row,5) * worksheet.cell_value(row,10) / (worksheet.cell_value(row,2) * IDFf)
			new_worksheet.write(row, 11, IDFf)
			new_worksheet.write(row, 12, value_min)
			new_worksheet.write(row, 14, value_plus1)


		new_workbook.save(path)
		print(sheet_name[t] + "写入数据成功！")
	# workbook.save(path)  # 保存工作簿
	

book_name_xls = 'Test4-1.xls'
value_title = [["Methods","TF-p","TF-p+1","TF-p+min","TF-f","TF-f+min", "ep","ef","totalp","totapf","IDFp","IDFf","TF-f*IDFp/(TF-p+min*IDFf)","Rank","TF-f*IDFp/(TF-p+1*IDFf)","Rank"],]
write_excel_xls(book_name_xls, sheet_name, value_title)
write_TFp_append(book_name_xls, sheet_name, version)
