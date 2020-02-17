numbers=[50, 40, 70, 56, 12, 5, 10, 7]
index=0
great_20=0
while index<len(numbers):
    if numbers[index]>20 and numbers[index]<40:
        great_20=great_20+1
    index=index+1 
print great_20 
