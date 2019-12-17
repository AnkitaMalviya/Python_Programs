#In this code if user input postive number then print negative and if user give negative number then it will be print negative number. 
user=input("enter your number")
user1=input("enter your number")
while user<=user1:
    if user>0 and user1>0:
        print -user
        user=user+1
else:
    if user<0 and user1<0:
        while user>=user1:
            print user
            user=user-1 