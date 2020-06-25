#LIST

pro_language=["Python","Java","Pearl","Django"]
#to add an item to the end of the list
pro_language.append("C++")
print(pro_language)

#to display the total length of the list
print(len(pro_language))

#to insert an item at the specified index
pro_language.insert(1,"C")
print(pro_language)

#to remove an element at the specified index
pro_language.pop(3)
print(pro_language)

#to add all the elements of the list to another list
web_development=["HTML","CSS","javascript"]
web_development.extend(["php","Java 10"])
print(web_development)

#to copy the list
web_development.copy()
print(web_development)

#to count the number of elements with specified value
thislist=["pearl","diamond","ruby","pearl"]
print(thislist.count("pearl"))


