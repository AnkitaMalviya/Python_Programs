list1="piray"
new=sorted(list1)
print new
list2="priya"
new1=sorted(list2)
print new1
index=0
count=0
while index<len(new):
    count=count+1
    index=index+1
j=0
count1=0
while j<len(new1):
    count1=count1+1
    j=j+1
s=0
if count==count1:
    while s<len(new):
        if new[s] in new1:
            a="anagram"
        else:
            a="not anagram"
            break
        s=s+1
    print a
else:
    print"not anagram"
        