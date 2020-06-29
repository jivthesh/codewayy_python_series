# this returns a file object
f=open("pythonFile.txt","r")

#read() method is for reading the content of the file
print("The content of the file:",f.read())

#close the file when you are finish with it
f.close()
