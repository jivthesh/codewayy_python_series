#SETS


courses_opt1={"Data Science","Cloud Computing","Ethical Hacking",}
courses_opt2={"Data mining","Mobile App","Data Analytics"}
#to add elements to the set
courses_opt1.add("Data Analytics")
print(courses_opt1)
#to remove the specified item,and if the value is not present it will generate an error
courses_opt1.discard("Data Science")
print(courses_opt1)
#to display the set that contains the item that only exist in set2 and not in set1
print(courses_opt2.difference(courses_opt1))
#to display the items that are present in both set1 and set2
print(courses_opt1.intersection(courses_opt2))
#to display the sets that contains elements from both the sets,duplicate are excluded
print(courses_opt1.union(courses_opt2))
#returns TRUE if no item in set1 is present in set2 or FALSE otherwise
print(courses_opt1.isdisjoint(courses_opt2))
#returns TRUE if all items of set2 is present in set1,FALSE otherwise
print(courses_opt1.issuperset(courses_opt2))



