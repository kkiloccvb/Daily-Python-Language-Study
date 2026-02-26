#练习2.3用变量表示一个人的名字，并向其显示一条消息。
first_name="                    Zhang"
sure_name="fei               "
full_name=f"{first_name}{sure_name}"
print(f"Hello {first_name}{sure_name},Hello {first_name.lstrip()}{sure_name.rstrip()}, would you like to learn some Python today,right?{full_name.strip()}")

#练习2.4 用变量表示一个人的名字，再分别以全小写、全大写和首字母大写的方式显示这个人名。
name1="kingfisher"
name2="KINGFISHER"
print(name1.upper())
print(name2.lower())
print(name1.title())

#练习2.5 找到你钦佩的名人说的一句名言，将这个名人的姓名和名言打印出来。输出应类似于下面这样（包括引号）。
name="Albert Einstein"
said='"A person who never made a mistake never tried anything new."'
print(f"{name.title()}once said,{said}")

#练习2.6 用变量 famous_person 表示名人的姓名，再创建要显示的消息并将其赋给变量 message，然后打印这条消息。
famous_person="Albert Einstein"
said='"A person who never made a mistake never tried anything new."'
message=(f"{famous_person}once said,{said}")
print(message)

#练习2.7 用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。
name="   diken      "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#练习2.8　请将值 'python_notes.txt'赋给变量 filename，再使用 removesuffix() 方法来显示不包含扩展名的文件名，就像文件浏览器所做的那样。
a=filename.removesuffix('.txt')#移除后缀
b=filename.removeprefix('python_notes')#移除前缀
print(a,b)

#练习2.9 编写 4 个表达式，分别使用加法、减法、乘法和除法运算，但结果都是数字 8。为了使用函数调用 print() 来显示结果，务必将这些表达式用括号括起来。
filename='python_notes.txt'
print(3+2+3)
print(2*4)
print(16/2)
print(9-1)

#练习2.10 用一个变量来表示你最喜欢的数，再使用这个变量创建一条消息，指出你最喜欢的数是什么，然后将这条消息打印出来。
favorite_number = 8
message = f"我最喜欢的数字是：{favorite_number}"
print(message)



















































































