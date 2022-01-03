# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import math
 
n = 0
sheet_name = []
version = []
sumOfTestsuites_num = []
with open('SumOfTestsuites-time.txt','r') as fileSOT:
	for lineSOT in fileSOT:
		lineSOT_arry = lineSOT.strip('\n').split(' ')
		sheet_name.append(lineSOT_arry[0]) 
		version.append(sheet_name[n].split('time')[1] )  #version[1]就是版本号
		sumOfTestsuites_num.append(lineSOT_arry[1]) 
		# print(sheet_name[n])
		# print(version[n])
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

		Filename = "MC/MC-time" + version[t] + ".txt"
		with open(Filename,'r') as file:
			row = 1
			for line in file:
				line_name = line.strip('\n').split(' ')
				# print("%s |" % line_name[1] )
				if line_name[1] == "0":
					line_name[1] = 0.000000000001
				new_worksheet.write(row, 6, float(line_name[1]))
				new_worksheet.write(row, 7, int(sumOfTestsuites_num[t]))
				
				IDF = math.log10(int(sumOfTestsuites_num[t]) / float(line_name[1]))
				new_worksheet.write(row, 8, IDF)
				row = row + 1
		new_workbook.save(path)
		workbook = xlrd.open_workbook(path)
		worksheet = workbook.sheet_by_name(sheet_name[t])
		new_workbook = copy(workbook)
		new_worksheet = new_workbook.get_sheet(sheet_name[t])
		rows_old = worksheet.nrows
		for row in range(1,rows_old):
			value_min = worksheet.cell_value(row,5) * worksheet.cell_value(row,8) / worksheet.cell_value(row,3)
			value_plus1 = worksheet.cell_value(row,5) * worksheet.cell_value(row,8) / worksheet.cell_value(row,2)
			new_worksheet.write(row, 9, value_min)
			new_worksheet.write(row, 11, value_plus1)
		new_workbook.save(path)
		print(sheet_name[t] + "写入数据成功！")

	
book_name_xls = 'Test4.xls'
value_title = [["Methods","TF-p","TF-p+1","TF-p+min","TF-f","TF-f+min", "MC","SumOfTestsuites","IDF","TF-f*IDF/TF-p+min","Rank","TF-f*IDF/TF-p+1","Rank"],]
write_excel_xls(book_name_xls, sheet_name, value_title)
write_TFp_append(book_name_xls, sheet_name, version)






# #------------------添加MC数据  &  计算TF-IDF值
# #num表示要打开第几个sheet
# def write_int_append(path,value,sheet_name,row, column): 
# 	workbook = xlrd.open_workbook(path)
# 	worksheet = workbook.sheet_by_name(sheet_name)
# 	new_workbook = copy(workbook)
# 	new_worksheet = new_workbook.get_sheet(sheet_name)
# 	if column == 6: #表示MC列，需要判断是否为0,写入的类型不同。
# 		new_worksheet.write(row, column, float(value[1]))
# 	else:
# 		new_worksheet.write(row, column, int(value[1]))
# 	new_workbook.save(path)

# def write_TFIDF_append(path,sheet_name,row): 
# 	workbook = xlrd.open_workbook(path)
# 	worksheet = workbook.sheet_by_name(sheet_name)
# 	new_workbook = copy(workbook)
# 	new_worksheet = new_workbook.get_sheet(sheet_name)
# 	IDF = math.log10(worksheet.cell_value(row,7) / worksheet.cell_value(row,6))
# 	new_worksheet.write(row, 8, IDF)
# 	new_workbook.save(path)
# 	workbook = xlrd.open_workbook(path)
# 	worksheet = workbook.sheet_by_name(sheet_name)
# 	new_workbook = copy(workbook)
# 	new_worksheet = new_workbook.get_sheet(sheet_name)
# 	# print(worksheet.cell_value(row,4))
# 	# print(worksheet.cell_value(row,7))
# 	# print(worksheet.cell_value(row,3))
# 	value_min = worksheet.cell_value(row,5) * worksheet.cell_value(row,8) / worksheet.cell_value(row,3)
# 	value_plus1 = worksheet.cell_value(row,5) * worksheet.cell_value(row,8) / worksheet.cell_value(row,2)
# 	new_worksheet.write(row, 9, value_min)
# 	new_worksheet.write(row, 11, value_plus1)
# 	new_workbook.save(path)

# Filename = "MC/MC-time" + version[1] + ".txt"
# with open(Filename,'r') as file:
# 	row = 1
# 	for line in file:
# 		line_name = line.strip('\n').split(' ')
# 		# print("%s |" % line_name[1] )
# 		if line_name[1] == "0":
# 			line_name[1] = 0.000000000001
# 		write_int_append("Test4.xls",line_name,sheet_name,row,6)
# 		write_int_append("Test4.xls",sumOfTestsuites_num,sheet_name,row,7)
# 		write_TFIDF_append("Test4.xls",sheet_name,row)
# 		row = row + 1








# with open('SumOfTestsuites-time.txt','r') as fileSOT:
# 	for lineSOT in fileSOT:
# 		lineSOT_arry = lineSOT.strip('\n').split(' ')
# 		sheet_name = lineSOT_arry[0]
# 		version = sheet_name.split('time') #version[1]就是版本号
# 		# print(version)
# 		sumOfTestsuites_num = lineSOT_arry
# 		print(sumOfTestsuites_num)
# 		#---------------------新建sheet
# 		def add_sheet_xls(path, sheet_name, value):
# 			index = len(value)
# 			workbook = xlrd.open_workbook(path)
# 			new_workbook = copy(workbook)
# 			sheet = new_workbook.add_sheet(sheet_name)
# 			for i in range(0, index):
# 				for j in range(0, len(value[i])):
# 					sheet.write(i, j, value[i][j])
# 			new_workbook.save(path)
# 			print("新建sheet %s成功" % sheet_name )


# 		add_sheet_xls('Test4.xls', sheet_name, value_title )

# 		#------------------添加TF-p数据
# 		def write_TFp_append(path,value,sheet_name): 
# 			workbook = xlrd.open_workbook(path)
# 			worksheet = workbook.sheet_by_name(sheet_name)
# 			rows_old = worksheet.nrows
# 			new_workbook = copy(workbook)
# 			new_worksheet = new_workbook.get_sheet(sheet_name)
# 			new_worksheet.write(rows_old, 0, value[0])
# 			new_worksheet.write(rows_old, 1, float('0' + value[2]))
# 			new_worksheet.write(rows_old, 2, (float('0' + value[2])+1))
# 			if float('0' + value[2]) == 0:
# 				new_worksheet.write(rows_old, 3, 0.000000000001)
# 			else:
# 				new_worksheet.write(rows_old, 3, float(value[2]))
# 			new_workbook.save(path)

# 		Filename = "Avg/passAvg-" + version[1] + ".txt"
# 		with open(Filename,'r') as file:
# 			for line in file:
# 				line_name = line.strip('\n').split(' ')
# 				# print("%s |" % line_name[1] )
# 				write_TFp_append("Test4.xls",line_name,sheet_name)

# 		#------------------添加TF-f数据
# 		def write_TFf_append(path,value,sheet_name,row): 
# 			workbook = xlrd.open_workbook(path)
# 			worksheet = workbook.sheet_by_name(sheet_name)
# 			new_workbook = copy(workbook)
# 			new_worksheet = new_workbook.get_sheet(sheet_name)
# 			new_worksheet.write(row, 4, float('0' + value[2]))
# 			if float('0' + value[2]) == 0:
# 				new_worksheet.write(row, 5, 0.000000000001)
# 			else:
# 				new_worksheet.write(row, 5, float('0' + value[2]))
# 			new_workbook.save(path)


# 		Filename = "Avg/failAvg-" + version[1] + ".txt"
# 		with open(Filename,'r') as file:
# 			row = 1
# 			for line in file:
# 				line_name = line.strip('\n').split(' ')
# 				# print(line_name[2])
# 				# print("%s |" % line_name[1] )
# 				write_TFf_append("Test4.xls",line_name,sheet_name,row)
# 				row = row + 1

# 		#------------------添加MC数据  &  计算TF-IDF值
# 		#num表示要打开第几个sheet
# 		def write_int_append(path,value,sheet_name,row, column): 
# 			workbook = xlrd.open_workbook(path)
# 			worksheet = workbook.sheet_by_name(sheet_name)
# 			new_workbook = copy(workbook)
# 			new_worksheet = new_workbook.get_sheet(sheet_name)
# 			if column == 6: #表示MC列，需要判断是否为0,写入的类型不同。
# 				new_worksheet.write(row, column, float(value[1]))
# 			else:
# 				new_worksheet.write(row, column, int(value[1]))
# 			new_workbook.save(path)

# 		def write_TFIDF_append(path,sheet_name,row): 
# 			workbook = xlrd.open_workbook(path)
# 			worksheet = workbook.sheet_by_name(sheet_name)
# 			new_workbook = copy(workbook)
# 			new_worksheet = new_workbook.get_sheet(sheet_name)
# 			IDF = math.log10(worksheet.cell_value(row,7) / worksheet.cell_value(row,6))
# 			new_worksheet.write(row, 8, IDF)
# 			new_workbook.save(path)
# 			workbook = xlrd.open_workbook(path)
# 			worksheet = workbook.sheet_by_name(sheet_name)
# 			new_workbook = copy(workbook)
# 			new_worksheet = new_workbook.get_sheet(sheet_name)
# 			# print(worksheet.cell_value(row,4))
# 			# print(worksheet.cell_value(row,7))
# 			# print(worksheet.cell_value(row,3))
# 			value_min = worksheet.cell_value(row,5) * worksheet.cell_value(row,8) / worksheet.cell_value(row,3)
# 			value_plus1 = worksheet.cell_value(row,5) * worksheet.cell_value(row,8) / worksheet.cell_value(row,2)
# 			new_worksheet.write(row, 9, value_min)
# 			new_worksheet.write(row, 11, value_plus1)
# 			new_workbook.save(path)

# 		Filename = "MC/MC-time" + version[1] + ".txt"
# 		with open(Filename,'r') as file:
# 			row = 1
# 			for line in file:
# 				line_name = line.strip('\n').split(' ')
# 				# print("%s |" % line_name[1] )
# 				if line_name[1] == "0":
# 					line_name[1] = 0.000000000001
# 				write_int_append("Test4.xls",line_name,sheet_name,row,6)
# 				write_int_append("Test4.xls",sumOfTestsuites_num,sheet_name,row,7)
# 				write_TFIDF_append("Test4.xls",sheet_name,row)
# 				row = row + 1





		# with open('SumOfTestsuites-math.txt','r') as file:
		# 	row = 1
		# 	for line in file:
		# 		line_name = line.strip('\n').split(' ')
		# 		# print("%s |" % line_name[1] )
		# 		write_int_append("Test4.xls",line_name,1,row,6)
		# 		row = row + 1

