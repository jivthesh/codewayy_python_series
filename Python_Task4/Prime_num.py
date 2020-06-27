
#Storing Prime numbers in a list
n=int(input("Enter a Number:"))
prime=[]
for i in range(1,100*n):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        #print(i)
        prime.append(i)
#print(prime)

#Printing the stored prime numbers in n*n matrices
serial=0
for i in range(1,n+1):
    for j in range(1,n+1):
        print(prime[serial],end=" ")
        serial=serial+1
    print(" ")
