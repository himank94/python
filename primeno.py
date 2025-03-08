def prime(a):
    count=0
    for i in range(2,a+1):
        if a%i==0:
            count+=1
    if(count==1):
        print(a,"is a prime number")
    else:
        print(a,"is not a prime number")