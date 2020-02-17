index=2
user=input("enter your number")
while index<user:
    if user%index==0:
        print"not prime number"
        break
    index=index+1
else:
    print"prime number"

    