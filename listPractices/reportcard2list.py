marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]
index=0
element=5
while index<len(marks):
    var1=0
    Total=0
    while var1<len(marks[index]):
        Total=Total+marks[index][var1]
        var1=var1+1
    print Total
    average=Total/element
    print"average","=",average
    index=index+1
    element=element-1 


