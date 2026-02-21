class employee:
    a=1
class programmer(employee):
    b=2
class xyz(programmer):
    c=3
    
m=employee()
print(m.a)
#print(m.b)#it will show error as there is no b in object employee

m=programmer()
print(m.a,m.b)

m=xyz()
print(m.a,m.b,m.c)

