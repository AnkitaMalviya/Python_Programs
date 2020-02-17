n = [19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
new_list=[] 
index=0   
while index<len(n):
    var=index+1
    while var<len(n):
        if n[index]==n[var]:
            if n[index] not in new_list:
                    new_list.append(n[index])
        var=var+1
    index=index+1
print new_list

