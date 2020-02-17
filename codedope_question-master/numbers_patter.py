index=7
space=0
while index>=1:
    var1=1
    while var1<=index:
        if var1%2==0:
            print "0",
        elif var1 ==1:
            print " "*space,"1",
            space+=1
        else:
            print "1",
        var1=var1+1
    print""
    space +=1
    index=index-2
    
   
