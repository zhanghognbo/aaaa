import random
list=[]
list1=[]
list2=[]
for i in range(50):
    list.append(random.randint(-10,10))
print(list)
for i in range(len(list)):
    if list[i]>0:
        list1.append(list[i])
    else:
        list2.append(list[i])
print(list1)
print(list2)