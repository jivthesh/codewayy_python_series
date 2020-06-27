#to return square of numbers
def square(number):
    squareOfNumber=number*number
    print("Square of number:",squareOfNumber)


#to return minimum number in a list
def minimum(list_num):
    min = list_num[ 0 ]
    for i in list_num:
        if i < min:
            min = i
            print ("The minimum number in the list is: ", min)



#to return maximum number in a list
def maximum(list_num):
    max=list_num[0]
    for i in list_num:
        if i > max:
            max = i
            print("Maximum elements in a list:",max)


#to return sum of elements in a list
def sum_list(list_num):
    total=0
    for n in list_num:
        total=total+n
        print("Sum of all elements in a given list:",total)
    



