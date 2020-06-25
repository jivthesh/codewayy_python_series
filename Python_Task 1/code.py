#Write a program in python which you should display your following details:
#1.Full name, 2.College Name,3.Initialize marks of 5 different subjects,4.Calculate total marks and percentage


name=input("Enter your Name:")
last_name=input("Enter your Surname:")
college_name=input("Enter your College Name:")
college_add=input("Enter your College Address:")
#to add str1 and str2
print("Full Name:",name+last_name)
#to add str3 and str4
print("College:",college_name+","+college_add)
#to input the marks of 5 subjects
sub1=int(input("Enter marks of sub1:"))
sub2=int(input("Enter marks of sub2:"))
sub3=int(input("Enter marks of sub3:"))
sub4=int(input("Enter marks of sub4:"))
sub5=int(input("Enter marks of sub5:"))
#to calculate total marks and percentage
tot=sub1+sub2+sub3+sub4+sub5
per=tot/5
#to print the output
print("Total marks:",tot)
print("Percentage:",per)


