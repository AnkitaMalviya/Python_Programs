numbers = [50, 40, 23, 70,100,56, 12, 5, 10,7,2]
index=0
max=0
while index<len(numbers):
    if max<numbers[index]:
        max=numbers[index]
    index=index+1
print max


