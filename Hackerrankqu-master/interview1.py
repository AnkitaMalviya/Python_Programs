# String : 'The quick Brow Fox'
# Output : 
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


String='The quick BRow Fox'
print String
new=String.replace(" ", "")
i=0
count=0
count1=0
while i<len(new):
    if new[i].isupper():
        count=count+1 
    else:
        count1=count1+1
    i=i+1 
print str(count)+"upper"
print str(count1)+"lower"
