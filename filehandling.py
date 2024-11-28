# file handling :- work on the file
# create file : syntax
# variablename = open("filename.extension" , "filemode")
#eg.  
#mylaptoppassword= open("password.txt","w")
# write file :  syntax:
# e.g.  mylaptoppassword.write("guhiguhi")
# read from file
# e.g.  mylaptoppassword.read()
#delete file
# import os
#os.remove("password.txt")

#write file :-syntax
#e.g.
# mylaptoppassword =

# create file for saving my laptop password
# open function will create the file when file is not exists and write the file
mypassword = open("password.txt","w")

# write my laptop password in file
mypassword.write("my laptop password is cndcbbcnj")

# overwrite the new password using userinput
mypassword.write(input("enter your new password "))

# read the password from file
mypassword = open("password.txt","r")
mydata = mypassword.read()
if "laptop" in mydata:
    print("yes")
else:
    print("no")

# to close the file
mypassword.close()

# delete the file
import os
os.remove("password.txt")

# create read write delete csv , excel , json , txt
# create csv file
mycsv = open("myfile.csv","w")
mycsv.write("pawan himank prem pratham anmol")

myexcel = open("myexcel.xlsx" , "w")
myexcel.write("name pawan himank raman")