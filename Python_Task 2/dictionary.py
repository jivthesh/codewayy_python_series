dict1={"Google":"Sergey Brin","Microsoft":"Bill Gates","Apple":"Steve Jobs"}
#to display the dicctionary's key-value pair
print(dict1.items())
#to display the keys
print(dict1.keys())
#to remove  the inserted key-value pair
dict1.popitem()
print(dict1)
#to insert the specified item in the dictionary
dict1.update({"Intel":"Robert Noyce"})
print(dict1)
#to display the value of the item with specified key
print(dict1.get("Microsoft"))
#to display the copy of the dictionary
print(dict1.copy())
#to display a dictionary with specified keys and value
dict2=("Sergey Brin","Larry Page","Sundar Pichai")
values={}
print(values.fromkeys(dict2,"Google"))



