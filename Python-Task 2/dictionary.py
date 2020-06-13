#DICTIONARIES


companies={"Google":"Sergey Brin","Microsoft":"Bill Gates","Apple":"Steve Jobs"}
#to display the dicctionary's key-value pair
print(companies.items())
#to display the keys
print(companies.keys())
#to remove  the inserted key-value pair
companies.popitem()
print(companies)
#to insert the specified item in the dictionary
companies.update({"Intel":"Robert Noyce"})
print(companies)
#to display the value of the item with specified key
print(companies.get("Microsoft"))
#to display the copy of the dictionary
print(companies.copy())
#to display a dictionary with specified keys and value
CEO=("Sergey Brin","Larry Page","Sundar Pichai")
values={}
print(values.fromkeys(CEO,"Google"))



