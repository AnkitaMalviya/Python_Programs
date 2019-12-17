list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
index=0
new=[]
while index<len(list1):
    if list1[index] not in new:
        new.append(list1[index])
    var=0
    while var<len(list2):
        if list2[var] not in new:
            new.append(list2[var])
        var=var+1
    index=index+1
a=sorted(new)
print (a)


