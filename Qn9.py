from functools import reduce

l=[123,888,987,243,876,999]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))