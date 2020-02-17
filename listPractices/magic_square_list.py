magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
i=0
while i<len(magic_square):
    j=0
    Total=0 
    while j<len(magic_square[i]):
        Total=Total+magic_square[i][j]
        j=j+1
    print"horizontal",Total
    i=i+1
i=0
while i<len(magic_square):
    j=0
    Total=0
    while j<len(magic_square[i]):
        Total=Total+magic_square[j][i] 
        j=j+1
    print"vertically",Total 
    i=i+1
   
i=0
while i<len(magic_square):
    j=0
    Total=0
    while j<len(magic_square):
        Total=Total+magic_square[j][i]
        j=j+1
        i=i+1
    print "cross",Total   
i=0
j=-1
Total=0
while i<len(magic_square):
        Total=Total+magic_square[i][j]
        j=j-1
        i=i+1
print"cross2",Total
    