def max_marks(*args):
    i=0
    while i<len(args):
        j=0
        b=0
        while j<len(args[i]):
            if b<args[i][j]:
                b=args[i][j]
            j=j+1
        print b
        i=i+1
max_marks([45, 21, 42, 63], [12, 53,42, 42], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99])
print type(max_marks)

