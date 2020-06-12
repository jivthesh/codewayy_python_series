set1={"Data Science","Cloud Computing","Ethical Hacking",}
set2={"Data mining","Mobile App","Data Analytics"}
#to add elements to the set
set1.add("Data Analytics")
print(set1)
#to remove the specified item,and if the value is not present it will generate an error
set1.discard("Data Science")
print(set1)
#to display the set that contains the item that only exist in set2 and not in set1
print(set2.difference(set1))
#to display the items that are present in both set1 and set2
print(set1.intersection(set2))
#to display the sets that contains elements from both the sets,duplicate are excluded
print(set1.union(set2))
#returns TRUE if no item in set1 is present in set2 or FALSE otherwise
print(set1.isdisjoint(set2))
#returns TRUE if all items of set2 is present in set1,FALSE otherwise
print(set1.issuperset(set2))



