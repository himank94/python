a=int(input("enter a number= "))
f=1
if a==0:
    print("factorial of 0 is 1")
elif a<0:
    print("factorial does not exist")
for i in range(1,a+1):
    f=f*i
print(f)