numbers = [54, 40, 23, 70,52,12, 5, 10, 7]
index=0
max=0
while index<len(numbers):
    if max<numbers[index]:
        max=numbers[index]
    index=index+1
c=0
sec_max=0
while c<len(numbers):
    if max>numbers[c] and sec_max<numbers[c]:
        sec_max=numbers[c]
    c=c+1
print sec_max



