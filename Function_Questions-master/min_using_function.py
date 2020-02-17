def min_number(list):
    index=0
    min=len(list)
    while index<len(list):
        if list[index]<min:
            min=list[index]
        index=index+1
    return min 
print min_number([3,2,9,8,0,4])

