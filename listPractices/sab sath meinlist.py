elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
Total=0
sum=0
while i<len(elements):
    if elements[i]%2==0:
        Total=Total+elements[i]
    else:
        sum=sum+elements[i]
    i=i+1
print Total
print sum
        