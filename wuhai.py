str1=input('请输入一个数:')  #123456         654321
num=0
num1=0                                                              #  i  n     i   n    i  n
for i ,n in enumerate(str1[::-1]): # i 返回的是下表  n 返回的是数字   0  6     1  5     2  4
    # print(i,'end=\t')
    # print(n,'end=\t')
    for m in range(10):   #0 1 2 3 4 5 6 7 8 9
        if n==str(m):
           num+=m*(10**i)    #6+ 50 +400+3000+20000+100000
str2=input("请输入一个数：")
for j,x in enumerate(str2[::-1]):
    for z in range(10):
        if x==str(z):
            num1+=z*(10**j)
print(num+num1)