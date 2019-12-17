list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
index=0
new=[]
while index<len(list1):
    if list1[index] in list2:
        new.append(list1[index])
    index=index+1
new.sort()
print new
 
    #"-------------------"
    
    # without in operator

index=0
new=[]
while index<len(list1):
    var1=0
    while var1<len(list2):
        if list1[index]==list2[var1]:
            new.append(list1[index])
        var1=var1+1
    index=index+1
new.sort()
print new