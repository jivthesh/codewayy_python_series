
#function to return full name
def my_name():
    name=input("Enter your Full Name:")
    print("Your Full Name is:",name)

#function to return total marks:
def total_marks():
    eng_marks=int(input("Enter your English Marks:"))
    maths_marks=int(input("Enter your Maths Marks:"))
    comp_marks=int(input("Enter your Computer Marks:"))
    DataStruc_marks=int(input("Enter your Data Structure Marks:"))
    DISCO_marks=int(input("Enter your DISCO marks:"))
    global tot_marks
    tot_marks=eng_marks+maths_marks+comp_marks+DataStruc_marks+DISCO_marks
    print("Total Marks:",tot_marks)

#function to return percentage
def cal_percentage(tot_marks):
    global score
    score=tot_marks/5
    print("Your Score is:",score)

#function to return garde
def grade(score):
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
    my_name()
    total_marks()
    cal_percentage(tot_marks)
    grade(score)

#Calling that function
display_Details()
    
    
    
    
                  
    
    
