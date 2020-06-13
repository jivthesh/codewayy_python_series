# TUPLE

founder=("Guido van Rossum","James Gosling","Bjarne Stroustrup")
#to display number of items in tuple
print(len(founder))
#first index is inclusive(before the :)and last (after :) is not
print(founder[0:2])
#to display the last item in the tuple
print(founder[-1])
#to display the element from the tuple with maximum value
print(max(founder))
#to display the element from the tuple with minimum vaue
print(min(founder))
#to display the number of times a specified value occurs in a tuple
print(founder.count("James Gosling"))
#to display the item for the specified value and returns the position of where it was found
print(founder.index("Bjarne Stroustrup"))
