#练习3.1　将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表的每个元素，从而将每个朋友的姓名都打印出来。
personal_ames=['zhang san','li si','wang ermazi']
for name in personal_ames:
    message=f'My friend name is {name.title()}'
    print(message)

#练习3.2 继续使用练习 3.1 中的列表，但不打印每个朋友的姓名，而是为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
personal_ames=['zhang san','li si','wang ermazi']
for name in personal_ames:
    message=f'My friend name is {name.title()},happy new year'
    print(message)

#练习 3.3：自己的列表　想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的陈述，如下所示。
drive_tool=['car','motorcycle','plane','subway']
for tool in drive_tool:
    message=f"I would like to own a{tool}"
    print(message)