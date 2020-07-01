def check_marks(m):
    if m >= 90:
        return print(True)
    elif m < 90:
        raise Exception("Error! Not Eligible")

n=int(input("Enter a number:"))
for  i  in range(0,n,1):
    marks=int(input("Enter marks:"))
    check_marks(marks)
