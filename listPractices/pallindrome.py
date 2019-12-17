name=["n","i","t","i","n"]
i=0
b=-1
while i<len(name):
    print name[i],name[b]
    if name[i]==name[b]:
        var="palindrome hai"
    else:
        var="palindrome nahi hai"
        break
    i=i+1
    b=b-1
print var



