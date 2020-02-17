number=30
n = [10, 11, 12, 13, 14, 17, 18, 19]
index=0
new=[]
while index<len(n):
    var=index+1
    while var<len(n):
        sum=n[index]+n[var]
        if sum==number:
            new.append([n[index],n[var]])
        var=var+1
    index=index+1
print new
