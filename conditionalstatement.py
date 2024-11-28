#conditional statement will check the condition is true or not
#to check the condition we use if else

# wap to check the user eligible for voting
userage = int(input("enter your age "))
if userage >= 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")
    
# wap to check user is male or female
gender = input("enter your gender ")
if gender == "male":
    print("you are not allowed to sit in first compartment")
elif gender=="female":
    print("you are allowed to sit in first compartment")
else:
    print("you are allowed to sit in any compartment")
    
# wap  if gender is female and age is greater than 18 :govt job apply
# else male age greater than 18 : private job apply
if gender=="female" and userage>18:
    print("you are eligible to apply for govt job")
elif gender=="male" and userage>18:
    print("you are eligible to apply for private job")
else:
    print("you are not eligible")