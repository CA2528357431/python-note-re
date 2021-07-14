# 正则

import re

a = 'shdgfkw  bg2vriub  wow wo world word well talk woowo  ljsbvou   21231sthed231a  dsfAAAA32sd23哈尔滨ssdfdsh哈尔滨士大夫'

x = re.compile(r'(s.*s)')
xx = x.findall(a)
print(xx)
# 默认是贪婪——尽可能长
x = re.compile(r'(s.*?s)')
xx = x.findall(a)
print(xx)
# 懒惰——尽可能短
