name = "himank mittal"
age = 19
gender = "male"
email = "himankmittal@gmail.com"

# problem
# print("my name is " + name + " my age is " + age + " my gender is " + gender + " my email is " + email)

#solution 1 - int variable +replace by ,
print("my name is " + name + " my age is " , age , " my gender is " + gender + " my email is " + email)

#solution 2 - enclosed the variable inside the string ny filt (F)
print(f"my name is {name} my age is {age} my gender is {gender} my email is {email}")

#solution 3 - typecasting
ageinstring = str(age)
print("my name is " + name + " my age is " + ageinstring + " my gender is " + gender + " my email is " + email)

#typecasting in python : convert one data type int another data type
# note : string can not be converted into int reason string not have any ascii no.

purchaseitemprice = 90.32
paiditemprice = int(purchaseitemprice)
print("paid amount is " , paiditemprice)

#data types in python 
print(type(name))  # type  function return datatype of variable
print(type(age))

# 1. str : it can store the string data e.g. name="himank mittal"
# 2. int : it can store the numerc data e.g. age = 19
# 3. float : it can store the decimal no. e.g. percentage = 75.42

# to get the input from the  user using input() function
# note : the input() function has default return type str
collegename = input("enter your college name ")
collegefee = input("enter your college fee ")
print("my college name is " + collegename + " " +collegefee)
collegefees= int(collegefee)
collegefees = collegefees - 25000
print("after scholarship my fee" , collegefees)