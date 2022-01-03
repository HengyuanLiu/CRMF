# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import math
# 由于重新执行后半部分耗时，先考虑修改当前结果表格。后面需要的话再补写这个脚本。 
# 应该依照MC里的文件剔除susMethod中未被覆盖的方法，但是当前先写成去掉表格中的相关数据。

n = 0
sheet_name = []
version = []
with open('SumOfTestsuites-chart.txt','r') as fileSOT:
	for lineSOT in fileSOT:
		lineSOT_arry = lineSOT.strip('\n').split(' ')
		sheet_name.append(lineSOT_arry[0]) 
		version.append(sheet_name[n].split('chart')[1] )  #version[1]就是版本号
		# print(sheet_name[n])
		# print(version[n])
		n = n + 1


#------------------建表
def write_excel_xls(path, old_path, sheet_name):
	index = len(sheet_name)  # 获取需要写入sheet个数
	workbook = xlwt.Workbook()  # 新建一个工作簿
	workbook_old = xlrd.open_workbook(old_path)
	for t in range(0,index):
		sheet = workbook.add_sheet(sheet_name[t])  # 在工作簿中新建一个表格
		worksheet = workbook_old.sheet_by_name(sheet_name[t])
		rows_old = worksheet.nrows
		temp = 0
		for i in range(0,rows_old):
			if worksheet.cell_value(i,6) == 0.000000000001:
				temp = temp +1
			else:
				for j in range(0,13):
					sheet.write(i-temp, j, worksheet.cell_value(i,j))
	workbook.save(path)  # 保存工作簿
	print(path + "表格写入数据成功！")

def write_excel_xls_sbfl(path, old_path, sheet_name):
	index = len(sheet_name)  # 获取需要写入sheet个数
	workbook = xlwt.Workbook()  # 新建一个工作簿
	workbook_old = xlrd.open_workbook(old_path)
	for t in range(0,index):
		sheet = workbook.add_sheet(sheet_name[t])  # 在工作簿中新建一个表格
		worksheet = workbook_old.sheet_by_name(sheet_name[t])
		rows_old = worksheet.nrows
		temp = 0
		for i in range(0,rows_old):
			if worksheet.cell_value(i,1) == 0 and worksheet.cell_value(i,2) == 0:
				temp = temp +1
			else:
				for j in range(0,9):
					sheet.write(i-temp, j, worksheet.cell_value(i,j))
	workbook.save(path)  # 保存工作簿
	print(path + "表格写入数据成功！")

def write_excel_xls_flsf(path, old_path, sheet_name):
	index = len(sheet_name)  # 获取需要写入sheet个数
	workbook = xlwt.Workbook()  # 新建一个工作簿
	workbook_old = xlrd.open_workbook(old_path)
	for t in range(0,index):
		sheet = workbook.add_sheet(sheet_name[t])  # 在工作簿中新建一个表格
		worksheet = workbook_old.sheet_by_name(sheet_name[t])
		rows_old = worksheet.nrows
		temp = 0
		for i in range(0,rows_old):
			if worksheet.cell_value(i,1) == 0 and worksheet.cell_value(i,2) == 0:
				temp = temp +1
			else:
				for j in range(0,7):
					sheet.write(i-temp, j, worksheet.cell_value(i,j))
	workbook.save(path)  # 保存工作簿
	print(path + "表格写入数据成功！")

def write_excel_xls_new(path, old_path, sheet_name):
	index = len(sheet_name)  # 获取需要写入sheet个数
	workbook = xlwt.Workbook()  # 新建一个工作簿
	workbook_old = xlrd.open_workbook(old_path)
	for t in range(0,index):
		sheet = workbook.add_sheet(sheet_name[t])  # 在工作簿中新建一个表格
		worksheet = workbook_old.sheet_by_name(sheet_name[t])
		rows_old = worksheet.nrows
		temp = 0
		for i in range(0,rows_old):
			if worksheet.cell_value(i,6) == 0.000000000001 and worksheet.cell_value(i,7) == 0.000000000001:
				temp = temp +1
			else:
				for j in range(0,15):
					sheet.write(i-temp, j, worksheet.cell_value(i,j))
	workbook.save(path)  # 保存工作簿
	print(path + "表格写入数据成功！")

book_name_xls = 'Test4.xls'
old_book_name_xls = 'Test4-old.xls'
# value_title = [["Methods","TF-p","TF-p+1","TF-p+min","TF-f","TF-f+min", "MC","SumOfTestsuites","IDF","TF-f*IDF/TF-p+min","Rank","TF-f*IDF/TF-p+1","Rank"],]
write_excel_xls(book_name_xls, old_book_name_xls, sheet_name)
write_excel_xls_new('Test4-1.xls', 'Test4-1-old.xls', sheet_name)
write_excel_xls_sbfl('Test4-sbfl.xls', 'Test4-sbfl-old.xls', sheet_name)
write_excel_xls_flsf('Test4-flsf.xls', 'Test4-flsf-old.xls', sheet_name)