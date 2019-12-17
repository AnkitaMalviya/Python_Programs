i=0
new=[]
while i<10:
    user=input("enter your number")
    new.append(user)
    i=i+1
print"enter number"
user=input()
i=0
while i<len(new):
    if user in new:
        out="present"
    else:
        out="not"
    i=i+1
print out
