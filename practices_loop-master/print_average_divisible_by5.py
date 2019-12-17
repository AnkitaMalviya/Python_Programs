index=1
sum=0
while index<=11:
    user=input("enter your weight")
    sum=sum+user
    index=index+1
average=sum/11
print"average","=",average
if average%5==0:
    print"yes"
else:
    print"no"

