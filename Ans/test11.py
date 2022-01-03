# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import sys
#两个参数，第一个为程序名，第二个为输出xls文件的序号

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



book_name_xls = sys.argv[1]+sys.argv[2]+'.xls'
sheet_name_xls = sys.argv[1]+"-"
value_title = [["Class","Distance","rank"],]
write_excel_xls(book_name_xls, sheet_name_xls, value_title)

with open(sys.argv[1]+'list.txt','r') as fileSOT:
	for lineSOT in fileSOT:
		lineSOT_arry = lineSOT.strip('\n')
		sheet_name = lineSOT_arry
		version = sheet_name.split(sys.argv[1]) #version[1]就是版本号
		# print(version[1])
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


		add_sheet_xls(book_name_xls, sheet_name, value_title )

		#------------------添加数据
		def write_append(path,value,sheet_name,lastone): 
			workbook = xlrd.open_workbook(path)
			worksheet = workbook.sheet_by_name(sheet_name)
			rows_old = worksheet.nrows 
			new_workbook = copy(workbook)
			new_worksheet = new_workbook.get_sheet(sheet_name)
			new_worksheet.write(rows_old, 0, value[0])
			new_worksheet.write(rows_old, 1, float(value[1]))
			if rows_old == 1:
				new_worksheet.write(rows_old, 2, int(rows_old))
			if rows_old > 1 :
				# print(lastone[1])
				if lastone[1] == "-1.0":
					if value[1] == "-1.0":
						new_worksheet.write(rows_old, 2, int(rows_old))
					else:
						new_worksheet.write(rows_old, 2, 1)
				else:
					if value[1] == lastone[1]:
						new_worksheet.write(rows_old, 2, worksheet.cell_value(rows_old-1,2))
					else:
						temp=1
						while float(worksheet.cell_value(rows_old-temp,1)) == float(lastone[1]):
							temp = temp +1
							if rows_old == temp:
								break
						# 	print(temp)
						# print(worksheet.cell_value(rows_old-temp,1),lastone[1])
						new_worksheet.write(rows_old, 2, worksheet.cell_value(rows_old-1,2)+temp-1)
			new_workbook.save(path)

		Filename = "finalAns/" +sys.argv[1]+"/"+sys.argv[1]+version[1]+"-ans.txt"
		with open(Filename,'r') as file:
			lastone = []
			lastone.append(" ")
			lastone.append(" ")
			for line in file:
				line_name = line.strip('\n').split(' ')
				# print("%s |" % line_name[1] )
				write_append(book_name_xls,line_name,sheet_name,lastone)
				lastone = line_name

