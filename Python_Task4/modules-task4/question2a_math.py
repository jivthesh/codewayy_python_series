import myModule
#to display the square of a number
myNumber=int(input("Enter a Number:"))
find_square=myModule.square(myNumber)
print("Square of a number:",find_square)

#Creating empty list
list_num=[]

#asking number of elements to put in list'''
num=int(input("Enter number of elements in a list:"))

# iterating till num to append elements in list 
for i in range(1,num+1):
    ele=int(input("Enter elements:"))
    list_num.append(ele)

#to display the minimum number
    minimum_num=myModule.minimum(list_num)
print("Minimum number in a list:",minimum_num)


#to display the maximum number
maximum_num=myModule.maximum(list_num)
print("Maximum number in a list:",maximum_num)


#to display sum
sum_Num=myModule.sum_list(list_num)
print("Sum of elements in the list:",sum_Num)
