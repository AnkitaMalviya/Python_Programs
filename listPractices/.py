list=[5,7,0,0,9,10,0,4,0,3,8,3,2,7,0]
# i=0
# new=[]
# new1=[]
# while i<len(list):
#     if list[i]==0:
#         new.append(list[i])
#     else:
#         new1.append(list[i])
#     i=i+1
# new1.extend(new)
# print new1



i=0
while i<len(list):
    if list[i]==0:
      a=list.pop(i)
      list.append(a)
    i=i+1
print list
