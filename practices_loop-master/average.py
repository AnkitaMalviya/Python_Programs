#Take 10 integers from keyboard using loop and print their average value on the screen.
index=1
sum=0
while index<=10:
    user=input("enter your number")
    sum=sum+user
    index=index+1
average=sum/10
print"average","=",average
