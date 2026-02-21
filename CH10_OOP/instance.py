class employee():  #here is class is employee
    salary=100000
    language="python"
    
devil=employee()  #here is obj is devil
devil.language="javascript" #its a instance attribute
print(devil.language,devil.salary)


'''Instance attributes, take preference over class attributes during assignment & 
retrieval.'''