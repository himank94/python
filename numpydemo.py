#numpy = create data set
#pandas = represents dataset changes
#matplotlib = show in graph
import numpy as np

# create numpy array to store friends name , edit
myfriends = np.array(["himank      " , "prem" , "vasu" , "pratham"])
print(myfriends)
print(type(myfriends))
print(myfriends[2])

for name in myfriends:
    print(name)

myfriends[0] = "ivan sharma"
print(myfriends)

myfriends.sort()
print(myfriends)

mydata = np.flip(myfriends)
print(mydata)

y=3
while y>=0:
    print(myfriends[y])
    y=y-1