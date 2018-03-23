# -*- coding: utf-8 -*-
# 导入xlwt模块
import xlwt
import json
# 创建一个Workbook对象，这就相当于创建了一个Excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
'''
Workbook类初始化时有encoding和style_compression参数
encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
默认是ascii。当然要记得在文件头部添加：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
style_compression:表示是否压缩，不常用。
'''
# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
sheet = book.add_sheet('test', cell_overwrite_ok=True)
# 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
# 向表test中添加数据
import os
import sys

num =0
# for (root, dirs, files) in os.walk(r"/Users/js/Desktop/haodaifu/wenman/wenman/file"):
#     for filename in files:
with open(r'/Users/js/Desktop/haodaifu/wenman/wenman/file/hospital.txt','r') as f:
    list_1 = f.readlines()
    print(len(list_1))
    for i in list_1:
        print(i)
        one_data = eval(i)
        print(one_data)
        print('-------')

        sheet.write(num, 0, one_data['hospital_name'])  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
        sheet.write(num, 1, one_data['hospital_address'])
        sheet.write(num, 2, one_data['hospital_phone'])  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
        sheet.write(num, 3, one_data['hospital_level'])
        sheet.write(num, 4, one_data['hospital_type'])  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
        sheet.write(num, 5, one_data['hospital_intro'])
        num += 1


book.save(r'/Users/js/Desktop/haodaifu/wenman/wenman/file/hospital.xls')  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错