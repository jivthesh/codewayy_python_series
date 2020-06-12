tuple1=("Guido van Rossum","James Gosling","Bjarne Stroustrup")
#to display number of items in tuple
print(len(tuple1))
#first index is inclusive(before the :)and last (after :) is not
print(tuple1[0:2])
#to display the last item in the tuple
print(tuple1[-1])
#to display the element from the tuple with maximum value
print(max(tuple1))
#to display the element from the tuple with minimum vaue
print(min(tuple1))
#to display the number of times a specified value occurs in a tuple
print(tuple1.count("James Gosling"))
#to display the item for the specified value and returns the position of where it was found
print(tuple1.index("Bjarne Stroustrup"))
