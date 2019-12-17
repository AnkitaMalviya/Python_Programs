#print"first letter capital"

String="neha"
index=0
new1=[]
while index<len(String):
    if String[index]=="n":
        s=String[index].upper()
        new1.append(s)
    else:
        new1.append(String[index])
    index=index+1
print "".join(new1)

