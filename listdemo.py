# list can store multiple data and data can be of different types int str float 
#list can store the duplicate data
#list is an ordered data set - sorting ascending or descending
#list index no. starts with 0
# ordered , changable , duplicate

#create list and store your friends name

friendlist = ["vasu" , "sparsh" , "wani"]
#print the friendlist
print(friendlist)
# add the age of your friends into list
#append will add the data into the end of the list
friendlist.append(36)
friendlist.append(40)
friendlist.append(45)
print(friendlist)

# add the data into list using index no
friendlist.insert(3,"himank")
print(friendlist)

# to access the data using index no
print(friendlist[2])
print(friendlist[3])
# access the complete list
for name in friendlist:
    print(name)

# to delete the data from list
# remove will delete the data using value
friendlist.remove("himank")
print(friendlist)

#pop will delete the data using index
friendlist.pop(3)
print(friendlist)

# add the 5 favt city name in list
#add  my favt city kasol in 0 index
# remove the last city in list using pop
# sorting the list data 
#print the list data
favtcity = ["pilkhuwa" , "jaipur" , "chandigarh" , "goa" , "ghaziabad"]
favtcity.insert(0 , "kasol")
favtcity.pop()
favtcity.sort()
print(favtcity)