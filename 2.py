no=int(input("enter a number= "))
count=0
for i in range(2,no+1):
    if no%i==0:
        count+=1
if(count==1):
    print(no,"is a prime number")
else:
    print(no,"is not a prime number")