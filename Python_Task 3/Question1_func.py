
#function to return full name
def myName():
    name=input("Enter your Full Name:")
    print("Your Full Name is:",name)

#function to return total marks:
def total_Marks():
    eng_Marks=int(input("Enter your English Marks:"))
    maths_Marks=int(input("Enter your Maths Marks:"))
    comp_Marks=int(input("Enter your Computer Marks:"))
    DataStruc_Marks=int(input("Enter your Data Structure Marks:"))
    DISCO_Marks=int(input("Enter your DISCO marks:"))
    global totMarks
    totMarks=eng_Marks+maths_Marks+comp_Marks+DataStruc_Marks+DISCO_Marks
    print("Total Marks:",totMarks)

#function to return percentage
def cal_Percentage(totMarks):
    global score
    score=totMarks/5
    print("Your Score is:",score)

#function to return garde
def my_Grade(score):
    if(score>=95):
        print('Your grade is A')
    elif(score>=85 and score<=95):
        print('Your grade is B')
    elif(score>=75 and score<=85):
        print('Your grade is C')
    elif(score>=65 and score<=75):
        print('Your grade is D')
    elif(score<=65):
        print("Failed")
    
#function to return all the other function
def display_Details():
    myName()
    total_Marks()
    cal_Percentage(totMarks)
    my_Grade(score)

#Calling that function
display_Details()
    
    
    
    
                  
    
    
