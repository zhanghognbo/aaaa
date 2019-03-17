# phone=input("请输入手机号：")
# # isdiget()判断是否字符串是否是数字
# print(phone.isdigit())
# try:
#     print('请输入你的手机号')
#     # 识别是否全数字
#     a = int(input())
#     # 转换字符计算数量
#     c = str(a)
#     b = len(c)
#     # 判断手机号尾数是否通过
#     if len(c) == 11:
#         print('号码验证通过')
#     else:
#         print('该号码不存在')
# except ValueError:
#     print('请输入正确的手机号码')
#
# import random
# # print(random.randint(-10,10))
# # 2. 编写程序，生成一个包含50个随机整数的列表，随机整数的范围是从-10到10，然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表。
# list=[]
# list1=[]
# list2=[]
# for i in range(1,51):
#     t=random.randint(-10,10)
#     list.append(t)
# print(list)
# for i in range(len(list)):
#     if list[i]>0:
#         list1.append(list[i])
#     else:
#         list2.append(list[i])
# print(list1)
# print(list2)
# # W
# list=[3,1,8,10]
# random.shuffle(list)
# print("随机排序列表：",list)
# aaa=random.choice(range(100))
# print(aaa)
# 字符串翻转：
a=input("请输入字符串：")
print(a[::-1])
