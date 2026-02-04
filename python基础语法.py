
'''
定义一个变量
a=10;
print (a);
'''

'''
文档字符串 Docstring
'''

'''
字符串练习
name = '哈基米'
sex = '猫'
age = 24
thing = '疯狂哈气'
end = 'GG'
print(name,sex,age,thing,end)
'''

'''
查找关键词
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 
'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 
'with', 'yield']
'''

# 'ctrl+/'注释
# 'ctrl+shift+/'取消注释
# 'crtl+shift+f10'运行当前文件

'''
输出内容不换行
print ('kingfisher',end="")
print ('is a bird')
'''

'''
输入
desc=input()
输出
print(desc)
'''

'''
查看数据类型·
type()
'''

'''
随机数生成
impott random
整数
random.randint(1,100)
浮点数
random.uniform(1,100)
'''

'''
字符串练习
s='123456789'
print(s,type(s))
s1=str()
print(s1,type(s1))
print(s[4])正向5
print(s[2])正向3
print(s[-2])方向倒数2
'''

'''
字符串切片
索引值获得部分片段内容
s='123456789'
print(s[2:5])# 从索引2到索引4(不包含索引5)
print(s[2:10:2])# 从索引2到索引9(不包含索引10),步长为2,即每隔一个字符取一个字符
print(s[2:10:3])# 从索引2到索引9(不包含索引10),步长为3,即每隔两个字符取一个字符
'''

'''
字符串拼接
a+b+c+d
join([a,b,c,d])
formatted_str()=f'{a}{b}{c}{d}'
formatted_str()='{}{}{}{}'.format(a,b,c,d)SSS
'''