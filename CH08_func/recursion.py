n = int(input("enter a number: "))

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
print(f"factorial is : {factorial(n)}")
