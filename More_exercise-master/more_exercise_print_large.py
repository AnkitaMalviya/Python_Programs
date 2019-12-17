def large(num1,num2,num3):
    if user1>user2 and user1>user3:
        return user1
    elif user2>user3 and user2>user1:
        return user2
    else:
        return user3
i=0
while i<=2:
    user=int(raw_input("enter your number"))
    if i==0:
        user1=user
    elif i==1:
        user2=user
    else:
        user3=user
    i=i+1
print large(user1,user2,user3)
