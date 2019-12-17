marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
i=0
sum=0
while i<len(marks):
    j=0
    Total=0
    count=0
    while j<len(marks[i]):
        Total=Total+marks[i][j]
        count=count+1
        j=j+1
    print Total
    Average=Total/count
    print"Average","=",Average
    sum=sum+Total
    i=i+1
print sum

