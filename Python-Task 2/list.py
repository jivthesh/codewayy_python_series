list1=["Python","Java","Pearl","Django"]
#to add an item to the end of the list
list1.append("C++")
print(list1)
#to display the total length of the list
print(len(list1))
#to insert an item at the specified index
list1.insert(1,"C")
print(list1)
#to remove an element at the specified index
list1.pop(3)
print(list1)
#to add all the elements of the list to another list
list2=["HTML","CSS","javascript"]
list2.extend(["php","Java 10"])
print(list2)
#to copy the list
mylist=list2.copy()
print(mylist)
#to count the number of elements with specified value
list3=["pearl","diamond","ruby","pearl"]
print(list3.count("pearl"))


