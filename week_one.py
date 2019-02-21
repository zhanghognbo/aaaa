# phone=input("请输入手机号：")
# # isdiget()判断是否字符串是否是数字
# print(phone.isdigit())
import random
# print(random.randint(-10,10))
# 2. 编写程序，生成一个包含50个随机整数的列表，随机整数的范围是从-10到10，然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表。
list=[]
list1=[]
list2=[]
for i in range(1,51):
    t=random.randint(-10,10)
    list.append(t)
print(list)
for i in range(len(list)):
    if list[i]>0:
        list1.append(list[i])
    else:
        list2.append(list[i])
print(list1)
print(list2)