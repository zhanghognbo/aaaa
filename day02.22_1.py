# # 1. 通过用户输入数字，计算阶乘。（30分）
# a=int(input("请输入数字："))
# jie=1
# sum=0
# i=1
# # 3=1*1+1*2+2*3=9
# # 3*2*1
# while i<=a:
#     jie=jie*i
#     i+=1
# print(jie)
# # 将一个列表的数据复制到另一个列表中，并反向排序输出。
# list=[]
# list1=[]
# import random
# for i in range(5):
#     list.append(random.randrange(10))
# print(list)
# list1=list
# print(list1)
# list1.reverse()
# print(list1)
# list1=sorted(list1,reverse=True)
# print(list1)
list=[]
for i in range(101,201):
    bool=True
    for j in range(2,i-1):
        if(i%j==0):
            bool=False
    if(bool==True):
        print(bool)
        list.append(i)
    else:
        continue
print(list)
# for i in range(101,201):
#     bool=True
#     for j in range(2,i-1):
#         if(i%j==0):
#             bool=False
#     if(bool==True):
#         list.append(i)
#     else:
#         continue
# print(list)


