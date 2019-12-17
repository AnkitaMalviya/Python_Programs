elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
even=0
odd=0
even1=0
odd1=0
while index<len(elements):
    if elements[index]%2==0:
        even=elements[index]
        even1=even1+even
    else:
        odd=elements[index]
        odd1=odd1+odd
    index=index+1
print"even","=",even1
print"odd","=",odd1


#count how many even and how many odd
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print even
print odd