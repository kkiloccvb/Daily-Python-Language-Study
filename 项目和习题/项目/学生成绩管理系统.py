student_list=[]
def print_menu(number):
    print("\n" + "="*15 + " 功能菜单 " + "="*15)
    print("[1]添加学生成绩")
    print("[2]删除学生成绩") 
    print("[3]查询学生成绩")
    print("[4]显示所有学生成绩")
    print("[q]结束")
    print("选择的选项为[:]",number) 
def add_student():
    info={}
    info["uid"]=input("请输入学号：")
    info["name"]=input("请输入姓名：")
    info["chinese"]=input("请输入语文成绩")
    info["math"]=input("请输入数学成绩")
    info["english"]=input("请输入英语成绩")
    student_list.append(info)
    print("添加成功")
def del_student():
    uid = input("请输入要删除成绩的学生的学号：")
    for stu in student_list:
        if stu['uid'] == uid:
            print("你要删除的学生为：", stu)
            choice = input("确认删除吗？[1]:yes / [2]:no  请输入：")
            if choice == "1":
                student_list.remove(stu)
                print("删除成功！")
                break
            elif choice == "2":
                print("已取消操作")
                break
            else:
                print("指令无效，取消删除")
                break
    else:
        print("您输入的学号不存在")
def search_student():
    name=input("请输入要查询成绩的学生姓名")
    for stu in student_list:
        if stu['name'] == name:
            print(stu)
            break
    else:
        print("您输入的学号不存在")
def show_all_student():
    for s in student_list:
        print(f"{s['uid']}\t{s['name']}\t{s['chinese']}\t{s['math']}\t{s['english']}")
def main():
    while True:
        print("欢迎使用成绩管理系统1.0版本")
        n=input("请选择你要使用的功能:")
        print_menu(n)
        match n:
            case "1":
                add_student()
            case "2":
                del_student()
            case "3":
                search_student()
            case "4":
                show_all_student()
            case "q":
                print("程序已退出，再见")
                exit()
            case _:
                print("输入有误，重新输入")
if __name__ == "__main__":
    main()

