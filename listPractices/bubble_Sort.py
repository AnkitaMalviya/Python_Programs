list=[-2,45,0,11,-9]
index=0
while index<len(list):
    index2=index+1
    while index2<len(list):
        if list[index]>list[index2]:
            n=list[index2]
            list[index2]=list[index]
            list[index]=n
            print list
        index2=index2+1
    index=index+1
print list 
