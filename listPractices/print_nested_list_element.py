list1=[1,5,8,10,11,[5,9,2,0],85,[4,2,9,10]]
print len(list1)
index=0
while index<len(list1):
    if (type(list1[index])==list):
        var=0
        while var<len(list1[index]):
            print list1[index][var]
            var=var+1
    index=index+1

