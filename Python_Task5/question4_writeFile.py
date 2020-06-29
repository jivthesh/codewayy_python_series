
#writing the files
writeFile=open("File.txt","w")
string=input("Enter a string:")
writeFile.write(string)
writeFile.close()

#reading the files
readFile=open("File.txt")
print(readFile.readline())
