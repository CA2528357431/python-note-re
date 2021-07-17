#正则
import re

a = 'shdgfkw  bg2vriub  wow wo world word well talk woowo  ljsbvou   21231sthed231a  dsfAAAA32sd23哈尔滨ssdfdsh哈尔滨士大夫'

x = re.compile(r'(\d+)')
xx = x.findall(a)
print(xx)
x = re.compile(r'(\s+)')
xx = x.findall(a)
print(xx)
# \d数字,\s空格，\w字符， .任意除了回车
# \D非数字,\S非空格，\W非字符， .任意除了回车

x = re.compile(r'([a-z A-Z]\d+)')
xx = x.findall(a)
print(xx)
# a-z A-Z表示范围 []一个分位

x = re.compile(r'[^a-z A-Z]')
xx = x.findall(a)
print(xx)
#  ^  表示非

x = re.compile(r'(A?)')
xx = x.findall(a)
print(xx)
# 1/0次
x = re.compile(r'(A*)')
xx = x.findall(a)
print(xx)
# 0-max次
x = re.compile(r'(A+)')
xx = x.findall(a)
print(xx)
# 1-max次

x = re.compile(r'(A{1,2})')
xx = x.findall(a)
print(xx)
# 1-2次
x = re.compile(r'(A{1,})')
xx = x.findall(a)
print(xx)
# 1-max次
x = re.compile(r'(A{1})')
xx = x.findall(a)
print(xx)
# 1次

d = '112432\n5mdbj132'
x = re.compile('^[\w\n]*$')
xx = x.findall(d)
print(xx)
#  ^$ 定义 起止

x = re.compile(r'\b\w{4}\b')
xx = x.findall(a)
print(xx)
# \b 单词、词块 \b