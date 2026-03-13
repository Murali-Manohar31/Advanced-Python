#Write a program to input name, marks and phone number of a student and format it

name=input("Enter your name : ")
marks=int(input("Enter your marks: "))
number=int(input("enter your number: "))

s= "The name of the student is {}, his marks are {} , his phone number is{}".format(name,marks,number)
print(s)