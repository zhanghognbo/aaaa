c=open("d://aa.jpg","rb+")
b=c.read()
d=open("d://cc.jpg","wb+")
d.write(b)

c1=open("d://aa.jpg","rb+")
b=c1.read()
d=open("d://dd.jpg","wb+")
d.write(b)

c2=open("d://aa.jpg","rb+")
b=c2.read()
d=open("d://ee.jpg","wb+")
d.write(b)
