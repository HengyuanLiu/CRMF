import xlwt
import xlrd
from xlutils.copy import copy
import sys
import re
import numpy as np

styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour red;')
styleBlueBkg1 = xlwt.easyxf('font: bold on, colour_index 6;')
styleBlueBkg2 = xlwt.easyxf('pattern: pattern solid, fore_colour red; font: bold on, colour_index 3;')
flag=sys.argv[2]
# print(flag)
rb = xlrd.open_workbook(sys.argv[1]+flag+'.xls')

# 对超出范围的做标记


sheet_num=0
with open(sys.argv[1]+'-colour.txt','r') as fileSOT:
    wb = copy(rb)
    hit_num = 0
    for lineSOT in fileSOT:
        lineSOT_arry = lineSOT.strip('\n')
        # print(lineSOT_arry)
        
        # if lineSOT_arry == 'time':
        if re.match(sys.argv[1]+'\d{1,3}',lineSOT_arry):
            worksheet = rb.sheet_by_name(lineSOT_arry)
            sheet_name_beifen=lineSOT_arry
            rows_n = worksheet.nrows
            # sum_row = 0.0
            # paichu = 0
            # count_n = 0
            arr = []
            count_n = 0
            for i in range(1,rows_n):
                if worksheet.cell_value(i,1) == 2000 or worksheet.cell_value(i,1) == 3000:
                    count_n = count_n +1
                else:
                    arr.append(worksheet.cell_value(i,1))
                    # if lineSOT_arry == "time14":
                    #     print(arr[i-1])
                    # count_n = count_n +1
                    # sum_row = sum_row + float(worksheet.cell_value(i,1))
            # count_n = rows_n - 1 - paichu
            # print(count_n)
            # print(worksheet.cell_value(count_n,1))
            arr_std = np.std(arr,ddof=1)
            mean = np.mean(arr)
            # print(lineSOT_arry)
            # print(arr_std)
            bound = mean + arr_std *3

            # # 控制排除率<30%
            # anum=0
            # for i in range(1,rows_n):
            #     if worksheet.cell_value(i,1) > bound and worksheet.cell_value(i,1)!=2000 and worksheet.cell_value(i,1) != 3000:
            #         anum=anum+1
            # if anum/(rows_n-count_n) > 0.5:
            #     bound = arr_std *4


            # if arr_std > 5:
            #     arr = []
            #     for i in range(1,rows_n):
            #         if worksheet.cell_value(i,1) > arr_std*3 or worksheet.cell_value(i,1) == 2000 or worksheet.cell_value(i,1) == 3000:
            #             pass
            #         else:
            #             arr.append(worksheet.cell_value(i,1))
            #     arr_std = np.std(arr,ddof=1)
            #     print(arr_std)
            #     bound = arr_std *3
            # else:
            #     pass
            # print(bound)
            sheet_num = sheet_num + 1
            continue
        else:
            ro = rb.sheets()[sheet_num]
            ws = wb.get_sheet(sheet_num)
            
# col = 2   
            target = 0
            for i in range(ro.nrows):
                if i == int(lineSOT_arry)-1:
                    ws.write(i, 0, ro.cell(i, 0).value, styleBlueBkg1)
                    ws.write(i, 1, ro.cell(i, 1).value, styleBlueBkg1)
                    ws.write(i, 2, ro.cell(i, 2).value, styleBlueBkg1)
                    target = 1
                    # continue
                if i > 0 and float(worksheet.cell_value(i,1)) > bound and float(worksheet.cell_value(i,1)) != 2000 and float(worksheet.cell_value(i,1)) != 3000 :
                    if target == 0:
                        ws.write(i, 0, ro.cell(i, 0).value, styleBlueBkg)
                        ws.write(i, 1, ro.cell(i, 1).value, styleBlueBkg)
                        ws.write(i, 2, ro.cell(i, 2).value, styleBlueBkg)
                    else:
                        ws.write(i, 0, ro.cell(i, 0).value, styleBlueBkg2)
                        ws.write(i, 1, ro.cell(i, 1).value, styleBlueBkg2)
                        ws.write(i, 2, ro.cell(i, 2).value, styleBlueBkg2)
                    hit_num = hit_num + 1
                else:
                    if i > 0:
                        # print(sheet_num)
                        with open("../"+sys.argv[1]+"/susClassNew/"+str(sheet_name_beifen)+'.txt','a') as fileW:
                            fileW.write(str(worksheet.cell_value(i,0)))
                            # fileW.write(" ")
                            # fileW.write(str(worksheet.cell_value(i,1)))
                            # fileW.write(" ")
                            # fileW.write(str(worksheet.cell_value(i,2)))
                            fileW.write("\n")

                target = 0
            # print(hit_num)
    # result = str(ro.cell(i, col).value)
    # if result == '不合格':
    #     ws.write(i, col, ro.cell(i, col).value, styleBlueBkg)
    #     ws.write(i, 1, ro.cell(i, 1).value, styleBlueBkg)
    wb.save(sys.argv[1]+ flag +'-2'+'-withcolour.xls')

# import pandas as pd
# import numpy as np
 
# columns = [['A', 'A', 'B', 'B', 'C'], ['a', 'b', 'c', 'd', 'e']]
# # 创建形状为（10，5） 的DataFrame 并设置二级标题
# # demo_df = pd.DataFrame(np.arange(50).reshape(10, 5), columns=columns)
# demo_df = pd.read_excel( 'time.xls' ,sheet_name='time1')
# print(demo_df)
 
 
# def style_color(df, colors):
#     """
    
#     :param df: pd.DataFrame
#     :param colors: 字典  内容是 {标题:颜色}
#     :return: 
#     """
#     return df.style.apply(style_apply, colors=colors)
 
 
# def style_apply(series, colors, back_ground=''):
#     """
#     :param series: 传过来的数据是DataFramt中的一列   类型为pd.Series
#     :param colors: 内容是字典  其中key 为标题名   value 为颜色
#     :param back_ground: 北京颜色
#     :return:
#     """
#     series_name = series.name[0]
#     a = list()
#     # 为了给每一个单元格上色
#     for col in series:
#         # 其中 col 为pd.DataFrame 中的 一个小单元格   大家可以根据不同需求为单元格设置不同的颜色
#         # 获取什么一级标题获取什么颜色
#         if series_name in colors:
#             for title_name in colors:
#                 if title_name == series_name:
#                     back_ground = 'background-color: ' + '#FFB6C1'
#                     # '; border-left-color: #080808'
#         a.append('background-color: ' + '#FFB6C1')
#     print(a[1])
#     a[0]=""
#     a[1]='background-color: ' + '#EEEE00'
#     return a
 
 
# style_df = style_color(demo_df, {"A": '#FFB6C1', "B": '#00EEEE', "C": '#EEEE00'})
 
# with pd.ExcelWriter('df_style.xlsx', engine='openpyxl') as writer:
#     #注意： 二级标题的to_excel index 不能为False
#     style_df.to_excel(writer, sheet_name='sheet_name')