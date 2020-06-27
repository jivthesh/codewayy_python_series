import myList
import myString
import myLogical

#to display the square of a number
number=int(input("Enter a Number:"))
myList.square(number)


#Creating empty list
list_num=[]
num=int(input("Enter  number of elements in a list:"))
for i in range(0,num):
    ele=int(input("Enter elements:"))
    list_num.append(ele)
    
#to display minimum number in a list
myList.minimum(list_num)

#to display the maximum number
myList.maximum(list_num)

#to display sum
Sum_Num=myList.sum_list(list_num)


#STRING:

test_string=input("Enter a String:")
#to find the middle character of a string
middleChar=myString.middle_char(test_string)
print(middleChar)

#to count number of vowel in a string
myString.vowels(test_string)


#to count the length of a string
lengthString=myString.length_str(test_string)



#LOGICAL OPERATORS

x =10
y = 20
#print true if both the condition are true
Check_AND=myLogical.ANDop(x,y)
print("Check whether it is true/false:",Check_AND)

#print true if one of thecondition is true
check_OR=myLogical.ORop(x,y)
print("Check whether it is true/false:",check_OR)

#reverse the result
check_NOT=myLogical.NOTop(x,y)
print("check:",check_NOT)

print(lengthString)

#to count words in string
wordsString=myString.words_str(test_string)
print(wordsString)
 
