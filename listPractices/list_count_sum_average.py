elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
count=0
one=0
Total=0
sum=0
while index<len(elements):
    if elements[index]%2==0:
        Total=Total+elements[index]
        count=count+1
    else:
        sum=sum+elements[index]
        one=one+1 
    index=index+1 
Average=Total/count
print "even number ka count","=",count,"hai"
print "odd number ka count""=",one,"hai"
print"saare numbers ka count","=",count+one,"hai"
print"even numbers ka sum hai","=",Total
print "odd numbers ka sum hai","=",sum
print"saare numbers ka sum hai","=",Total+sum
print"even numbers ka average hai","=",Total/count
print"odd numbers ka average hai","=",sum/one
All=Total+sum
print"saare numbers ka average hai","=",All/11


