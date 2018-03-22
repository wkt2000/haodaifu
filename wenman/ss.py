# coding:utf-8
s ='<td valign="top">安康市金州路85号</td>'
# import re
# f = re.match(r'>(.*?)</',s)
# print(f.group(0))
import re
# html='<a href="http://www.jb51.net">脚本之家</a>,Python学习！'
dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',s)
print(dd)