list=[[8,3,4],[1,5,9,7],[6,7,2]]
index=0
while index<len(list):
        var=0
        while var<len(list[index]):
            print list[index][var],"index",index,var
            var=var+1
        index=index+1