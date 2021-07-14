# 正则

import re

a = '<html>abc123abcdefg</htmlaaa>'
# 想要 123 前后一样的字母

x = re.compile("<([a-z]+)>\w+</([a-z]+)>")
xx = x.findall(a)
print(xx)

a = '<html>abc123abcdefg</html>'
y = re.compile("<([a-z]+)>\w+</(\\1)>")
yy = y.findall(a)
print(yy)

z = re.compile(r"<([a-z]+)>\w+</(\1)>")
zz = z.findall(a)
print(zz)

# \1 表示引用第1个（）中的匹配内容
# python 中防止\被认为是转义字符，再加一个\,\\表示转义字符\,形成\\1。
# 也可以在引号之前加 r ,表示无视转义，按字面读取

