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
formatted_str()='{}{}{}{}'.format(a,b,c,d)
'''

'''
格式化功能(宽度为10个字符)
{:<10} 左对齐
{:>10} 右对齐
{:^10} 中间对齐

pi=3.1415926
print(f'pi:{pi:<20}')  # 左对齐
print(f'pi:{pi:>20}')  # 右对齐 
print(f'pi:{pi:^20}')  # 中间对齐
--》输出结果
pi:3.1415926           
pi:           3.1415926
pi:     3.1415926      
'''

'''
特殊字符
\n 换行
\t 水平制表
r 原始字符串，忽略转义字符
'''

'''
join 字符串拼接
find 查找元素位置
count 查找元素个数
replace 替换字符
split 字符串分割
format 格式化输出
upper 大写字母
lower 小写字母
strip 去除空格
'''
ss='  kingfisher is a bird  '
s1='123456789'
print(ss.join(['hello','LOL']))
print(ss.split(' a '))
print(s1.find('5'))
print(ss.count('i'))
s2=s1.replace('3','LOL')
print(s2)