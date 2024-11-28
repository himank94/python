# error  handling  or  exception handling
# control over the error in programs

# error in programs
#print(x)

#solution
try:
    print(x)
except NameError:
    print("'x' is not defined")
    
#2 error type in python
x="pawan"
y=10
#c=x+y
#print(c)

try:
    c=x+y
except TypeError:
    print("can only concatenate str (not int) to str")
    
#3 error 3
#y=1/0
try:
    y=1/0
except ZeroDivisionError:
    print("divide by zero error")
    
#4 error 4
name = "pawan"
#no = int(name)
try:
    no= int(name)
except ValueError:
    print("string value can not convert to integer value")

#5 error 5
friends = ["ivan" , "anshu" , "wani"]
#friends[4]
try:
    friends[4]
except IndexError:
    print("you are calling wrong index")

#error 6
m = 10
n=20
#if m>n:
#print(m)
try:
    if m>n:
    print(m)
except IndentationError:
    print("identation error")