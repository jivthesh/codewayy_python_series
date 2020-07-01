#Q6

import math
def is_abundant(n):
    factor_Sum=sum([i for i in range(1,n) if n%i==0])
    return factor_Sum > n
a=int(input("Enter the number:"))
#check for abundant number
if is_abundant(a):
    print("The number is Abundant")
else:
    print("The number is Not Abundant")

   



number=int(input("Enter a number:"))
sum = 0
for x in range(1, number):
    if number % x == 0:
        sum += x
        #check for perfect number
if (sum == number):
    print("Perfect Number")
else:
    print("Not a Perfect Number")





def divisorsSum(n) : 
    sum = 0  
    i = 1
    while i<= math.sqrt(n) : 
        if (n % i == 0) : 
  
            
            if (n / i == i) : 
                sum = sum + i 
            else : 
                sum = sum + i; 
                sum = sum + (n / i) 
        i = i + 1
    return sum
    
# Function to check Deficient Number 
def isDeficient(n) :
    return (divisorsSum(n) < (2 * n)) 
   
# check deficient number
n=int(input("Enter a number"))
if ( isDeficient(n) ): 
    print("Deficient Number")
else : 
    print("Not a deficient Number")
   
