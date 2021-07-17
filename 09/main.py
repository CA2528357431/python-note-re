import re

x = re.compile(".(.(.)d)e")
st = "abcdefgh"
mat = x.match(st)

print(mat.groups())
# 所有括号里的匹配

print(mat.group())
print(mat.group(0))
# 整体匹配

print(mat.group(1))
# 第一个（）的匹配
# 括号个数按左括号出现顺序算

print(mat.group(2))
# 第二个（）的匹配