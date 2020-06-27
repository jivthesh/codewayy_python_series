rows=int(input("Enter number of rows:"))
columns=int(input("Enter number of columns:"))

#Initialize matrix
prime=[]
print("Enter the number of matrix:")

for i in range(rows):
    a=[]
    for j in range(columns):
        a.append(int(input()))
    prime.append(a)

for i in range(rows):
    for j in range(columns):
        print(prime[i][j],end=" ")
    print()

print("the prime number from the matrix are:")
for i in range(rows):
    for j in range(columns):
        if(prime[i][j]>1):
            for num in range(2,prime[i][j]):
                if(prime[i][j]%num)==0:
                    break
                else:
                    print(prime[i][j])
                 
