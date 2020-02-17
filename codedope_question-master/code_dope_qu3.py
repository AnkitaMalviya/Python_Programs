a=[[1,2,3],[4,5,6]]
i=0
new=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        new.append(a[i][j])
        j=j+1
    i=i+1
print new
