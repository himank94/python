# function can perform any task
# it can be reuse , function will return the result
# def is define

# create function to print the name
def printname():
    print("my name is himank mittal")
# call function to print the name
printname()

#create function to concatenate fname and lname from user
fname = input("enter your first name ")
lname = input("enter your last name ")
def fullname(firstname , lastname):
    print(firstname + " " +lastname)
fullname(fname , lname)

# area of square when one side is given
length = int(input("enter the length "))
def area(l):
    print(l * l)
area(length)

