#Q3

def string_test(string):
    d={"UPPER_CASE":0, "LOWER_CASE":0}  
#appemding each alphabet from the string 
    for i in string:
        if i.isupper():
           d["UPPER_CASE"]+=1
        elif i.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", string)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('Machine Learning Language')
