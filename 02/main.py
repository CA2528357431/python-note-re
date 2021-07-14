import re

b = '123fafw'
x = re.compile(r'(\d+)')
xx = x.match(b)
print(xx)
# 开头是否匹配
# 成功则返回对象
# 否则none

st = xx.group()
print(st)
# 符合部分的字符串

start = xx.start()
print(start)
end = xx.end()
print(end)
# 匹配起止位置

span = xx.span()
print(span)
# 返回起止位置的tuple



a = 'shake wow wo world word well talk woowo  braek  ssss  move straight哈尔滨hsdfz哈尔滨士大夫'

x=re.compile(r'wo')
xx=x.search(a)
#找到第一个匹配的
span=xx.span()
print(span)
start=xx.start()
print(start)
end=xx.end()
print(end)
#同match
