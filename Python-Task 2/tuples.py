# TUPLE

lang_Founder=("Guido van Rossum","James Gosling","Bjarne Stroustrup")
#to display number of items in tuple
print(len(lang_Founder))

#first index is inclusive(before the :)and last (after :) is not
print(lang_Founder[0:2])

#to display the last item in the tuple
print(lang_Founder[-1])

#to display the element from the tuple with maximum value
print(max(lang_Founder))

#to display the element from the tuple with minimum vaue
print(min(lang_Founder))

#to display the number of times a specified value occurs in a tuple
print(lang_Founder.count("James Gosling"))

#to display the item for the specified value and returns the position of where it was found
print(lang_Founder.index("Bjarne Stroustrup"))
