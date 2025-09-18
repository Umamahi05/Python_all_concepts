import csv

with open("Book1.csv","r") as rHnd:
    rdr = csv.DictReader(rHnd)
    for row in rdr:
        print(row["age"])

'''
with(open("Book1.csv") as rH, open("Out.csv","w") as wH):
    for line in rH:q
    
        print(line.strip())
        #age = line.split(",")[-1] OR
        #print(age)
        cols = line.strip().split(",")
        age = cols[2]
        wH.write(age)


#With Block - no need to close the file explicitely.
with(open("log_file.txt", "r") as log):
    while True:
        line = log.readline()
        if not line:
            break
        
        if "ERROR" in line:
            print("Found Error:", line.strip())

with open("log_file.txt") as f:
    line = f.readline()
    for _ in range(10): #_ acts as a throwaway vble 
        print(f.readline().strip())


with open("firstfile.txt","r") as fHnd:
    for each_line in fHnd:
        print(each_line.strip())
'''




#file = open("filename.txt", "mode")
'''
#Creating a file and write some contents
wFileObj = open("firstfile.txt", "w")
wFileObj.write("Hi Hello! Welcome to the new text file \n")
wFileObj.write("This is the initial text in this file. Later we update it.")
wFileObj.close()

#Opening the existing file and read the contents
rFileObj = open("firstfile.txt", "r")
content = rFileObj.read()
print("File Content:\n",content)
rFileObj.close()

#append the file
aFileObj = open("firstfile.txt","a")
aFileObj.write("Adding a new line \n")
aFileObj.close()
'''