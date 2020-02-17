list1=[10,20,30,80,50,10,30,70,20,50,70,80]
index=0
count=0
new=[]
while index<len(list1):
    var=index+1
    while var<len(list1):
        if list1[index]==list1[var]:
            del(list1[var])
            new.append(list1[index])
            count=count+1 
            break
        var=var+1
    index=index+1
print count


