print"enter your number"
index=1
factor=1
user=input()
while index<=user:
    if user==0:
        print"1"
    else:
        factor=factor*index
    index=index+1
print factor
