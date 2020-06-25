#Write a program in python which you should display your following details:
#1.Full name, 2.College Name,3.Initialize marks of 5 different subjects,4.Calculate total marks and percentage


myName=input("Enter your Name:")
last_Name=input("Enter your Surname:")
college_Name=input("Enter your College Name:")
college_Address=input("Enter your College Address:")
#to add str1 and str2
print("Full Name:",myName+last_Name)
#to add str3 and str4
print("College:",college_Name+","+college_Address)
#to input the marks of 5 subjects
eng_Marks=int(input("Enter marks of English:"))
math_Marks=int(input("Enter marks of Maths:"))
comp_Marks=int(input("Enter marks of Computer:"))
sci_Marks=int(input("Enter marks of Science:"))
eco_Marks=int(input("Enter marks of Economics:"))
#to calculate total marks and percentage
totalMarks=eng_Marks+math_Marks+comp_Marks+sci_Marks+eco_Marks
cal_Percentage=totalMarks/5
#to print the output
print("Total marks:",totalMarks)
print("Percentage:",cal_Percentage)


