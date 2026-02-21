class employee:
    def __init__(self):
        print("constructor of employee")
    a=1
class programmer(employee):
    def __init__(self):
        super().__init__() #superfunc will call the constructor of the base class
        print("constructor of programmer")
    b=2
class xyz(programmer):
    c=3
    
'''m=employee()
print(m.a)
#print(m.b)#it will show error as there is no b in object employee

m=programmer()
print(m.a,m.b)'''

m=xyz()
print(m.a,m.b,m.c)

