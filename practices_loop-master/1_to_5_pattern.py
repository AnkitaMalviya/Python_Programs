index=1
while index<=10:
    print str(index)*index
    index=index+1          


#without using multipliction operator

index=1
while index<=10:
    var=1
    while var<=index:
        print index,
        var=var+1
    print("")
    index=index+1    

