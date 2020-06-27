import myLogical
x =10
y = 20

Check_AND=myLogical.ANDop(x,y)
print("return true if both the condition are true:",Check_AND)


check_OR=myLogical.ORop(x,y)
print("return true if one of thecondition is true:",check_OR)


check_NOT=myLogical.NOTop(x,y)
print("reverse the result:",check_NOT)
