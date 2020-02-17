student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
index=0
less=0
greater=0
while index<len(student_marks):
    if student_marks[index]<50:
        less=less+1
    else:
        greater=greater+1
    index=index+1
print"less than 50 count=",less
print"greater than 50 count=",greater 