from pymongo import MongoClient

# create mongo client connection
client = MongoClient("mongodb://localhost:27017/")

# create database for todo app
mydb = client["todoDB"]

# create new collection from database in todo app
mycol = mydb["tasklist"]

# create data using dictionary
# mytask = {"taskName":input("enter task name ") , "taskdesc":input("enter task description ") , "taskdate":input("enter task date ") , "taskstatus":int(input("enter task status "))}

# # add data into collection
# mycol.insert_one(mytask)

#create friend collection in tododb
myfriendlist = mydb["friendlist"]

#create new friend in friend list
friend = [{"name":"ivan" , "age":36 , "gender":"male"} , {"name":"pratham" , "age":20 , "gender":"male"} , {"name":"vasu" , "age":18 , "gender":"male"}]

#to add friend into collection
# myfriendlist.insert_many(friend)

# delete the data in database
# deletefriend = {"name":"ivan"}
# myfriendlist.delete_one(deletefriend)

# update the friend list
# name = {"name":"pratham sharma"}
# myfriendlist.update_one({'age':20} , {"$set":name})

# to get the friend list
friends = myfriendlist.find()
for data in friends:
    print(data)