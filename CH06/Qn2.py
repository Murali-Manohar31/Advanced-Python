marks1 = int(input("Enter marks1 : "))
marks2 = int(input("Enter marks2 : "))
marks3 = int(input("Enter marks3 : "))

#check percentage
total_percentage = 100*((marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congrats you are passed", total_percentage)
else:
    print("better luck next time ", total_percentage)
