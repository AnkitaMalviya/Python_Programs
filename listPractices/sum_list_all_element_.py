#sum all element in list
magic_square = [[8, 3, 4,5],[1, 5, 9],[6, 7, 2]]
index=0
sum=0
while index<len(magic_square):
    var=0
    while var<len(magic_square[index]):
        sum=sum+magic_square[index][var]
        var=var+1
    index=index+1
print sum
print type(magic_square[0])
print type(magic_square[1])
print type(magic_square[2])
