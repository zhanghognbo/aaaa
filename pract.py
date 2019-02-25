# try:
#     a=int(input("请输入手机号码："))
#     b=str(a)
#     if len(b)==11:
#         print("输入手机号正确")
#     else:
#         print("请输入有效的手机号！")
# except ValueError:
#     print("请输入数字")
# import random
# list=[]
# list1=[]
# list2=[]
# for i in range(1,51):
#     list.append(random.randint(-10,10))
# print(list)
# for i in range(len(list)):
#     if list[i]>0:
#         list1.append(list[i])
#     else:
#         list2.append(list[i])
# print(list1)
# print(list2)
# list=[]
# import random
# for i in range(1,21):
#     list.append(random.choice(range(100)))
# print(list)
# list[::2]=sorted(list[::2],reverse=True)
# print(list)
# import random
# str='abcd'
# str1=''
# for i in range(1000):
#     str1+=random.choice(str)
# print(str1)
# print(len(str1))
# for i in range(len(str1)):
#     key=dict.get(i)
# L=["a","b","c"]
# print(L[1:])
# print(bool(0))
# n=(int(input("请输入数的前几项？")))
# n1=0
# n2=1
# count=2
# if n<=0:
#     print("请输正整数：")
# elif n==1:
#
#     print(n1)
# else:
#     print("斐波那契数列：")
#     print(n1, ",",n2,end=" , ")
#     while count<n:
#         a=n1+n2
#         print(a,end=" , ")
#         n1=n2
#         n2=a
#         count+=1
print(int('101',2))


