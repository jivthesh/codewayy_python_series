#printing all the numbers till 10 uing for loop
for num in range(1,11):
    if(num==3 or num==7):
        continue
    print(num,end=' ')
print("\n")

#displaying all the numbers till 10 using while loop
number=1
while(number!=11):
    if(number==3 or number==7):
        number+=1
    else:
        print(number)
        number+=1
        
