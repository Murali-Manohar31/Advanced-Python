''' to greet all the person names stored in a list ‘l’ and which starts 
with S'''
l = ["Murali", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello{name}")
