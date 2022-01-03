# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import math
 
#------------------建表
def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


book_name_xls = 'Test4-sbfl.xls'
sheet_name_xls = 'lang0'
value_title = [["Methods", "ef", "ep", "Total_f", "Total_p", "op2", "rank", "Tarantula", "rank"],]
write_excel_xls(book_name_xls, sheet_name_xls, value_title)

with open('SumOfTestsuites-lang-fail.txt','r') as fileSOT:
	for lineSOT in fileSOT:
		lineSOT_arry = lineSOT.strip('\n').split(' ')
		sheet_name = lineSOT_arry[0]
		version = sheet_name.split('lang') #version[1]就是版本号
		# print(version)
		sumOfTestsuites_num = lineSOT_arry
		print(sumOfTestsuites_num)
		#---------------------新建sheet
		def add_sheet_xls(path, sheet_name, value):
			index = len(value)
			workbook = xlrd.open_workbook(path)
			new_workbook = copy(workbook)
			sheet = new_workbook.add_sheet(sheet_name)
			for i in range(0, index):
				for j in range(0, len(value[i])):
					sheet.write(i, j, value[i][j])
			new_workbook.save(path)
			print("新建sheet %s成功" % sheet_name )


		add_sheet_xls('Test4-sbfl.xls', sheet_name, value_title )

		#------------------添加ef数据
		def write_ef_append(path,value,sheet_name): 
			workbook = xlrd.open_workbook(path)
			worksheet = workbook.sheet_by_name(sheet_name)
			rows_old = worksheet.nrows
			new_workbook = copy(workbook)
			new_worksheet = new_workbook.get_sheet(sheet_name)
			new_worksheet.write(rows_old, 0, value[0])
			new_worksheet.write(rows_old, 1, int(value[1]))
			new_workbook.save(path)

		Filename = "SBFL/ef-" + sheet_name + ".txt"
		with open(Filename,'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				# print("%s |" % line_name[1] )
				write_ef_append("Test4-sbfl.xls",line_name,sheet_name)

		#------------------添加ep数据
		def write_ep_append(path,value,sheet_name,row): 
			workbook = xlrd.open_workbook(path)
			worksheet = workbook.sheet_by_name(sheet_name)
			new_workbook = copy(workbook)
			new_worksheet = new_workbook.get_sheet(sheet_name)
			new_worksheet.write(row, 2, int(value[1]))
			new_workbook.save(path)


		Filename = "SBFL/ep-" + sheet_name + ".txt"
		row = 1
		with open(Filename,'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				# print(line_name[2])
				# print("%s |" % line_name[1] )
				write_ep_append("Test4-sbfl.xls",line_name,sheet_name,row)
				row = row + 1
		#此时row等于需要填的总行数
		#------------------添加Total_f数据
		def write_int_append(path,value,sheet_name,row, column): 
			workbook = xlrd.open_workbook(path)
			worksheet = workbook.sheet_by_name(sheet_name)
			new_workbook = copy(workbook)
			new_worksheet = new_workbook.get_sheet(sheet_name)
			new_worksheet.write(row, column, int(value))
			new_workbook.save(path)

		def write_op2Tarantula_append(path,sheet_name,rows): 
			workbook = xlrd.open_workbook(path)
			worksheet = workbook.sheet_by_name(sheet_name)
			new_workbook = copy(workbook)
			new_worksheet = new_workbook.get_sheet(sheet_name)
			for row in range(1,rows):
				op2 = (worksheet.cell_value(row,1)-worksheet.cell_value(row,2))/( worksheet.cell_value(row,4) + 1)
				if worksheet.cell_value(row,1) == 0 and worksheet.cell_value(row,2) == 0:
					Tarantula = -1
				else:
					Tarantula = (worksheet.cell_value(row,1)/worksheet.cell_value(row,3))/(worksheet.cell_value(row,1)/worksheet.cell_value(row,3)+worksheet.cell_value(row,2)/worksheet.cell_value(row,4))
				new_worksheet.write(row, 5, op2)
				new_worksheet.write(row, 7, Tarantula)
			new_workbook.save(path)

		total_p = 0
		with open("SumOfTestsuites-lang.txt",'r') as file:
			for line in file:
				line_name = line.strip('\n').split(' ')
				if line_name[0] == sheet_name:
					total_p = int(line_name[1])-int(lineSOT_arry[1])
					break;
		row_len = row
		while row > 1 :
			row = row -1
			write_int_append("Test4-sbfl.xls",lineSOT_arry[1],sheet_name,row,3)		
			write_int_append("Test4-sbfl.xls",total_p,sheet_name,row,4)
		
		write_op2Tarantula_append("Test4-sbfl.xls",sheet_name,row_len)
