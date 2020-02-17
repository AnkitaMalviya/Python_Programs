list=[5,7,0,0,9,10,0,4,0,3,8,3,2,7,0]
index=0
new=[]
new1=[]
while index<len(list):
    if list[index]==0:
        new.append(list[index])
    else:
        new1.append(list[index])
    index=index+1
new1.extend(new)
print new1


#without extend function

list=[5,7,0,0,9,0,0,3,8,3,2,0,0]
index=0
while index<len(list):
    if (index==7):
        break
    if list[index]==0:
      a=list.pop(index)
      list.append(a)
      index=index-1
    index=index+1
print list
