import math
print("Hi, welcome to simple calculator")
print("Please enter the value of length ")
#length=int(input())
#print("The length is:",length)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(" press 1 for addtion \n press 2 for subtraction \n press 3 to multiply \n press 4 for division")
choice=int(input("enter your choice "))
add=a+b
sub=a-b
mul=a*b
div=a/b
if (choice==1):
    print("addtion = ",add)
elif (choice==2):
    print("subtraction = ",sub)
elif (choice==3):
    print("multiplication = ",mul)
elif (choice==4):
    print("division = ",div)
else:
    print("enter a valid option ")
c=int(input("Enter a number: "))
square_root=math.sqrt(c)
print("this is sqrt of c:", square_root)
