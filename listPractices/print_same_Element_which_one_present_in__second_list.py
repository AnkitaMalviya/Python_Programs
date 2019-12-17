list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
index=0
new=[]
while index<len(list1):
    var=0
    while var<len(list2):
       if list1[index]==list2[var]:
           new.append(list1[index])
       var=var+1
    index=index+1
print new

