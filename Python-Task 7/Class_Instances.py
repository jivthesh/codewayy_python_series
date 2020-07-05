class Student:
    def __init__(self):
        self.FirstName=""
        self.LastName=""
        self.CollegeName=""
        self.BranchName=""
        self.marks=[]
        self.total=0
        self.percentage=0
        self.__grade=""
        

    def Full_Name(self):
        self.FirstName=input("\nEnter your First Name: ")
        self.LastName=input("Enter your Last Name: ")
        print("Full Name:",self.FirstName+" "+self.LastName)



    def College_Branch(self):
        self.CollegeName=input("\nEnter College Name:")
        self.BranchName=input("Enter Branch Name:")
        print("College And Branch:",self.CollegeName+","+self.BranchName)

        
    def Cal__Total(self):
        print("\nEnter marks of 5 subjects: ")
        for i in range(5):
            self.marks.append(int(input("Subject "+str(i+1)+": ")))
			
        for x in self.marks:
            self.total+=x
            print("Total Marks:",self.total)
			

    def Cal_Percentage(self):
        self.percentage=self.total/5
        print("\nPercentage:",self.percentage)
        
		

    def Cal_Grade(self):
        if self.percentage>=90:
            self.__grade="O"
        elif 80<=self.percentage<90:
            self.__grade="A"
        elif 70<=self.percentage<80:
            self.__grade="B"
        elif 60<=self.percentage<70:
            self.__grade="C"
        elif self.percentage>=50:
            self.__grade="D"
        else:
            self.__grade="F"
        print("\nGrade:",self.__grade)
			
    
stu_info=Student()
stu_info.Full_Name()
stu_info.College_Branch()
stu_info.Cal__Total()
stu_info.Cal_Percentage()
stu_info.Cal_Grade()

        

