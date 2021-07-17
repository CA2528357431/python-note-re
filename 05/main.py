# 正则

# 别名引用

import  re

a = r'<html><table>htmlabc123abcdefg</table></html>'
x = re.compile(r'<(?P<large>[a-z]+)><(?P<small>[a-z]+)>\w+</((?P=small))></((?P=large))>')
xx = x.findall(a)
print(xx)
#  (?P<名字>匹配规则)  来确定一个匹配的名字
#  (?P=small)  来引用
#  本文中引用时加两组括号————使用引用本身有一个括号，包裹选择有一个括号
a = r'<html><table>htmlabc123abcdefg</table></html>'
x = re.compile(r'<(?P<large>[a-z]+)><(?P<small>[a-z]+)>\w+</(?P=small)></(?P=large)>')
xx = x.findall(a)
print(xx)
