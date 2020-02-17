numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
max=0
while index<len(numbers):
    if numbers[index]>max:
        max=numbers[index]
    index=index+1
print max
var2=0
sec_max=0
while var2<len(numbers):
    if max>numbers[var2] and sec_max<numbers[var2]:
        sec_max=numbers[var2]
    var2=var2+1
print sec_max