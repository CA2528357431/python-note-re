# 正则
import re


a = 'shdgfkw  bg2vriub  wow wo world word well talk woowo  ljsbvou   21231sthed231a  dsfAAAA32sd23哈尔滨ssdfdsh哈尔滨士大夫'

x = re.compile(r'哈尔滨\w.*\w{3}哈尔滨')
xx = x.findall(a)
print(xx)
x = re.compile(r'(哈尔滨\w).*(\w{3}哈尔滨)')
xx = x.findall(a)
print(xx)
# ()内是目标  可有多个

x = re.compile(r'[s-z]|d')
xx = x.findall(a)
print(xx)
#  | 表示或


