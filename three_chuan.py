import random
list=[]
for i in range(20):
    list.append(random.choice(range(100)))
print(list)
for i in range(len(list)):
    list[::2]=sorted(list[::2],reverse=True)
print(list)
