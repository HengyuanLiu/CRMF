# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import math

n = 0
sheet_name = []
version = []
sumOfTestsuites_num = []
with open('SumOfTestsuites-lang-fail.txt','r') as fileSOT:
	for lineSOT in fileSOT:
		lineSOT_arry = lineSOT.strip('\n').split(' ')
		sheet_name.append(lineSOT_arry[0]) 
		version.append(sheet_name[n].split('lang')[1] )  #version就是版本号
		sumOfTestsuites_num.append(lineSOT_arry[1]) 
		# print(sheet_name[n])
		# print(version[n])
		n = n + 1
n = 0
total_p = []
with open("SumOfTestsuites-lang.txt",'r') as file:
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

		Filename = "e_FLSF/ef-" + sheet_name[t] + ".txt"
		target = 1
		with open(Filename,'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				new_worksheet.write(target, 0, line_name[0])
				new_worksheet.write(target, 1, float(line_name[1]))
				target = target + 1
		Filename = "e_FLSF/ep-" + sheet_name[t] + ".txt"
		target = 1
		with open(Filename,'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				new_worksheet.write(target, 2, float(line_name[1]))
				new_worksheet.write(target, 3, int(sumOfTestsuites_num[t]))
				new_worksheet.write(target, 4, total_p[t])
				target = target + 1
		new_workbook.save(path)
		workbook = xlrd.open_workbook(path)
		worksheet = workbook.sheet_by_name(sheet_name[t])
		new_workbook = copy(workbook)
		new_worksheet = new_workbook.get_sheet(sheet_name[t])
		for row in range(1,target):
			if worksheet.cell_value(row,1) == 0 and worksheet.cell_value(row,2) == 0:
				Tarantula = -1
			else:
				Tarantula = (worksheet.cell_value(row,1)/worksheet.cell_value(row,3))/(worksheet.cell_value(row,1)/worksheet.cell_value(row,3)+worksheet.cell_value(row,2)/worksheet.cell_value(row,4))
			new_worksheet.write(row, 5, Tarantula)
		new_workbook.save(path)
		print(sheet_name[t] + "写入数据成功！")

book_name_xls = 'Test4-flsf.xls'
value_title = [["Methods", "Rf","Rp", "Total_f", "Total_p", "Tarantula-flsf", "rank"],]
write_excel_xls(book_name_xls, sheet_name, value_title)
write_TFp_append(book_name_xls, sheet_name, version)
