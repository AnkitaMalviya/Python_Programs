numbers=[50, 40, 23,27,28,70, 56, 12, 5, 10, 7]
i=0
total=0
while i<len(numbers):
    if numbers[i]>20 and numbers[i]<40:
        total=total+1
    i=i+1
print total
