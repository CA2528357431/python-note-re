import re

#零宽断言
#即可修饰匹配内容前后的内容，又可以修饰要匹配的内容

a='word wow woawo wo w wasting aworow walling arrrw'



x=re.compile(r'\b\w+(?=ing\b)')#匹配 \b\w+ 此\w+后方必须是ing\b
xx=x.findall(a)
print(xx)
#正预测零宽断言，对后续部分的要求
# 形式为（？=结构）

x=re.compile(r'(?<=\bwo)\w+\b')#匹配 \w+\b 而且\w+前方必须是\bwo
xx=x.findall(a)
print(xx)
#正回顾零宽断言，对之前部分的修饰
# 形式为（？<=结构）

x=re.compile(r'\b(?!w)\w+\b')#匹配 \b\w+ 此\w+第一个必须不是w
xx=x.findall(a)
print(xx)
#负预测零宽断言，对后续部分的要求
# 形式为（？!结构）

x=re.compile(r'\b\w{2}(?<!o)\w+\b')#匹配 \w{2}\w+ 而且\w{2}第二个前方第一个字符不是o
xx=x.findall(a)
print(xx)
#负回顾零宽断言，对之前部分的修饰
# 形式为（？<!结构）



