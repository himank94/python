# oops in python
# object oriented programming structure -> objects

# class -> it is  container which contains the collection of variables , function
# e.g. -> tripti class
# tripti.fullname="triptisahu"
# tripti.age=19
# tripti.sleeping()
# tripti.eating()
# tripti.watching()

#class syntax:
#  class ClassName:
#      statement
#e.g.
class Himank:
    age = 19
    fullname = "himank mittal"
    email = "himank@gmail.com"
    def pocketmoney(this , amount):
        print("my pocket money is " , amount)
    def monsalary(this):
        day= int(input("enter the per day salary "))
        salary = day *30
        print("my monthly salary is " , salary)
        
# create class object
himank:Himank = Himank()
print("my name is " , himank.fullname , "age is " , himank.age)
himank.pocketmoney(15000)
himank.monsalary()
