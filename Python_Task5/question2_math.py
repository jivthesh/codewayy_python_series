#Import math Library
import math

#returns the squareroot of number
num=int(input("Enter a number:"))
print(math.sqrt(num))

#return the ceil value
Num=float(input("Enter a float number:"))
print(math.ceil(Num))

#return the floor value
print(math.floor(Num))


#sorting the list
print("\nSorting of List:")
Sort_List=[3,8,5,9,6]
print("Original List:",Sort_List)
Sort_List.sort()
print("List after sorting:",Sort_List)

#sorting the tuples
print("\nSorting of Tuples:")
Sort_Tuple=(8,9,6,7,4)
print("Original Tuple list:",Sort_Tuple)
new_tuple=sorted(Sort_Tuple)
print("Sorted tuple:",new_tuple)


#sorting of set
print("\nSorting of Set:")
sortSet = {'mango', 'kiwi', 'apple', 'orange', 'banana'}
print("Original set:",sortSet)
print("Sorted List from Set = ", sorted(sortSet))






