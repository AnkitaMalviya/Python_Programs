user1="2345678"
print len(user1)
i=0
count=0
while i<len(user1):
    a=int(user1[i])
    if a%2==1:
        count=count+1
    i=i+1
