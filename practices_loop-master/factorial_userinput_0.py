fac=1
user=input("enter your number")
if user==0:
    print "1"
else:
    while user>=1:
        fac=fac*user
        user=user-1
    print fac
