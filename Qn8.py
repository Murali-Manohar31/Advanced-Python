def divisible5(n):
    if(n%5==0):
        return True
    return False
a=[4512,75,8907,4125,7895]

f=list(filter(divisible5,a))
print(f)