list=["nehai18@navgurukul.org","pragati18@navgurukul.org"]
i=0
while i<len(list):
    j=0
    str=""
    while j<len(list[i]):
        if list[i][j]=="@":
            break
        else:
            str=str+list[i][j]
        j=j+1
    print str,
    i=i+1
