list=[3,5,49,-1,-2,0]
# index=0
# while index<len(list):
#     index2=index+1
#     while index2<len(list):
#         if list[index]>list[index2]:
#             n=list[index2]
#             list[index2]=list[index]
#             list[index]=n
#             print list
#         index2=index2+1
#     index=index+1
# print list 


i=0
while i<len(list):
    j=0
    while j<len(list)-i-1:
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        j=j+1
    print list
    i=i+1 



