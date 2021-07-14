# 正则
import re

a = 'shake wow wo world word well talk woowo  braek  ssss  move straight哈尔滨hsdfz哈尔滨士大夫'


x = re.compile(r'[s-z]')
xx = x.split(a)
print(xx)
# 分割


c = 'aaaaaasdfsafwefadcevwegxxxxxxxxxx'
xx = re.sub('[ax]{2}', '*', c)
print(xx)
# 替换



