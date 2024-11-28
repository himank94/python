# list in python
#list stores multiple data
mylist = ["pawan" , "ivan" , "deepanshu"]
#tuple store multiple data
mytuple = ("pawan" , "ivan" , "deepanshu")
#set store multiple data
myset = {"pawan" , "ivan" , "deepanshu"}
#dictionary store multiple data in key value pair
mydict = {"name":"pawan" , "email":"himank@gmail.com"}

# to check the data type of all above data set
print("list:" , type(mylist), "tuple:" , type(mytuple), "set:" , type(myset), "dict:" , type(mydict))

#how to identify list , set , tuple , dictionary
# list :[] , tuple: () , set: {} , dict: {:}

# example of data set
myset = {"pawan","himank","vasu","himank"}
mytuple = ("pawan","himank","vasu","himank")
mylist = ["pawan","himank","vasu","himank"]
mydict={"name":"himank","age":19,"name":"himank"}

#access specific data from data set
print("list: " , mylist[0], "tuple: " , mytuple[0], "dict: " , mydict["name"])

#access complete data from data set
for data in mylist:
    print("list ",data)
for item in myset:
    print("set ",item)
for value in mytuple:
    print("tuple ",value)
for x in mydict.values():
    print("dict ",x)

# to check which data set support duplicate data
print("list ",mylist,"tuple ",mytuple,"set ",myset,"dict ",mydict) 
# list can contain duplicate item
# set no duplicate item
# tuple contains duplicate items
# dictionary no duplicate items

#to update the data in all data set
# mylist[0]= "tripti"
# print(mylist)
# mytuple[0]="tripti"
# print(mytuple)
# myset[0]="tripti"
# print(myset)
# mydict["name"] = "tripti"
# print(mydict)

#tuple and set is unchangeable
#list and dict is changable

#add new value in data set
mylist.append("sparsh")
myset.add("sparsh")
mydict.update({"name":"sparsh"})
print("list ",mylist,"tuple ",mytuple,"set ",myset,"dict ",mydict)
# list , set , dict addable
# tuple not addable because it does not have any function

# to remove the data from data set
mydict.pop("name")
mylist.pop(0)
myset.remove("himank")
print("list ",mylist,"tuple ",mytuple,"set ",myset,"dict ",mydict)

#list , dict , set removeable
#tuple not removeable as it does not have any function

# convert tuple to list
convertlist= list(mytuple)
print(type(convertlist))
convertlist.append("rohan")
convertlist.pop(2)
print(convertlist)
mytuple = tuple(convertlist)
print(mytuple)
