#Q4

import re 
  
# initializing string  
string =input("Enter a string:")
  
# initializing substring 
test_str = "at"
  
# printing original string  
print("The original string is : " +string)

#printing substring  
print("The substring to find : " + test_str) 
  
# using re.finditer() 
# All occurrences of substring in string  
res = [i.start() for i in re.finditer(test_str,string)] 
  
# printing result  
print("The start indices of the substrings are : " + str(res)) 
