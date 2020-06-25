#DICTIONARIES


myCompanies={"Google":"Sergey Brin","Microsoft":"Bill Gates","Apple":"Steve Jobs"}
#to display the dicctionary's key-value pair
print(myCompanies.items())
#to display the keys
print(myCompanies.keys())
#to remove  the inserted key-value pair
myCompanies.popitem()
print(myCompanies)
#to insert the specified item in the dictionary
myCompanies.update({"Intel":"Robert Noyce"})
print(myCompanies)
#to display the value of the item with specified key
print(myCompanies.get("Microsoft"))
#to display the copy of the dictionary
print(myCompanies.copy())
#to display a dictionary with specified keys and value
google_CEO=("Sergey Brin","Larry Page","Sundar Pichai")
values={}
print(values.fromkeys(google_CEO,"Google"))



