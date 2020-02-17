numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
max=0
while index<len(numbers):
    if numbers[index]>max:
        max=numbers[index]
    index=index+1
print max