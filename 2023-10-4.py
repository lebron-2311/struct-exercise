# writer：LeBron James
# My email 1269497440@qq.com
"""grade = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0}
sum = 0
count = 0
a = input()
while a != "False":
    s = int(input())
    sum += grade[a] * s
    count = count + 1

print("%.2f" % (sum / count))"""
"""print(4*4+3*3+2*4)
print(4+3+4)
print(33/11)
grade = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0}
total_grade_points = 0
total_credit_hours = 0

while True:
    grade_level = input("请输入课程等级（输入False结束输入）：")
    if grade_level == "False":
        break

    credit_hours = float(input("请输入课程学分："))

    if grade_level.upper() in grade:
        grade_points = grade[grade_level.upper()]
        total_grade_points += grade_points * credit_hours
        total_credit_hours += credit_hours
    else:
        print("无效的等级，请重新输入。")

if total_credit_hours > 0:
    average_gpa = total_grade_points / total_credit_hours
    print("牛牛的平均绩点为：%.2f" % average_gpa)
else:
    print("没有输入任何课程信息。")
"""

""""grade = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0}
sum = 0
total_credit_num = 0
while True:
    grade_level = input()
    if grade_level == "False":
        break
    credit_num = float(input())
    sum += grade[grade_level] * credit_num
    total_credit_num += credit_num

print("%.2f" % (sum / total_credit_num))"""

"""牛客网的登录系统需要验证用户名与密码，当二者都正确时才允许登录，其中管理员的用户名为'admis'，密码为'Nowcoder666'。请你使用if-else语句，根据输入的用户名ID和密码，判断该用户等否登录。
输入描述：
第一行输入字符串表示用户名；
第二行输入字符串表示密码。
输出描述：
登录成功输出"Welcome!"，登录失败输出"user id or password is not correct!"""
"""name = input()
password = input()
if(name=="admis" and password=="Nowcoder666"):
    print("Welcome!")
else:
    print("user id or password is not correct!")"""

"""描述
Python的条件语句依靠将运算结果转变成布尔值后进行判断，然后分支，如果我们直接判断布尔值会怎么样呢？输入布尔变量，使用条件语句判断，如果为真则输出"Hello World!"，否则输出"Erros!"。
输入描述：
输入0 或者 1。
输出描述：
输出"Hello World!"或者"Erros!"。"""
"""
a = bool(int(input()))
if (a):
    print("Hello World!")
else:
    print("Erros!")"""

"""描述
创建一个空列表my_list，如果列表为空，请使用print()语句一行输出字符串'my_list is empty!'，
否则使用print()语句一行输出字符串'my_list is not empty!'。
输入描述：
无
输出描述：
按题目描述进行输出即可。"""

"""my_list=[]
if(len(my_list)==0):
    print("my_list is empty!")
else:
    print("my_list is not empty!")"""

"""my_list = ['P', 'y', 't', 'h', 'o', 'n']
print("Here is the original list:")
print(my_list)

print("\nThe number that my_list has is:")
print(len(my_list))
"""
"""users_list = ['Niuniu', 'Niumei', 'Niu Ke Le']
for i in users_list:
    print("Hi,"+i+"! Welcome to Nowcoder!")
print("Happy Programmers' Day to everyone!")"""

"""my_list=[]
for i in range(10,51):
    my_list.append(i)
print(my_list)
print(my_list[0], my_list[-1])"""

"""my_list = []
my_list = input().split()
sum = 0
for i in my_list:
    sum += int(i)
avg = sum / len(my_list)
print("%d %.2f" % (sum, avg))"""

"""my_lis=[]
for a in range(0,19,2):#通过 range(0, 19, 2) 创建了一个迭代器。这个迭代器将从0开始，每次增加2，直到达到19之前的数。
    my_lis.append(a)
for i in my_lis:
    print(i)

mylist=[i for i in range(0,19,2)]
print(mylist)"""
"""mylist = (i for i in range(1, 51))
for i in mylist:
    if i % 5 ==0 :
        print(i)
"""
mylist = []
for i in range(1, 11):
    mylist.append(2**i)
    print(mylist[i-1])