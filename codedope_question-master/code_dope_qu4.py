index=0
new=[]
while index<10:
    print"enter number"
    user=input()
    new.append(user)
    index=index+1
b=new
new1=[]
index=-1
while index>=(-len(b)):
    new1.append(b[index])
    index=index-1
print new1
