# binary_number = [1,0,1,0,0,1,1]
# i=-1
# b=1/2
# new=[]
# while i>=-len(binary_number):
#     if binary_number[i]==1:
#         z=b
#         new.append(z)    
#     else:
#          binary_number[i]
#     i=i-1
#     b=b+1
# j=0
# z=2
# new1=[]
# while j<len(new):
#     if new[j]==0:
#         a="1"
#     else:
#         a=2**new[j]
#         new1.append(a)
#     j=j+1
# new1.insert(0,1)
# print new1
# s=0
# sum=0
# while s<len(new1):
#     sum=sum+new1[s]
#     s=s+1
# print sum

binary_list=[1,1,0,0,1]
b=0
index=len(binary_list)-1
sum=0
while index>=0:
    solve=binary_list[index]*(2**b)
    sum=sum+solve
    b=b+1
    index=index-1
print sum