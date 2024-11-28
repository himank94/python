# for loop is used to no. of iteration

username ="himank mittal"
for x in username:
    print(x)
    
# print 1 to 10 using for loop
for i in range(1,11):
    print(i)

# wap to create of any no
tableno = int(input("enter the no "))
for a in range(1,11):
    print(tableno * a)

# wap to print even no from 1 to 20
for b in range(1,21):
    if b%2 ==0:
        print(b)
        
# wap print this pattern 1 , 4 , 7 , 10 , 13 using for loop
for c in range(1,21,3):
    print(c)

#wap print this pattern 1 3 7 11 13  15 using for loop
for d in range(1,16,2):
    if d==9 or d==5:
        continue  # skip the current iteration
    else:
        print(d)
