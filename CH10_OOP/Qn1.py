class programmer:
    company="Microsoft"
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
        
p = programmer("John",10000,27)
print(p.name,p.salary,p.age,)
d = programmer("domgesh",100300,27)
print(d.name,d.salary,d.age,)