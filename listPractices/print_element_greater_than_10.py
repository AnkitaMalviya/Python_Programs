student=[1,4,5,18,19,7,8,9,7,3,7,10,31]
total=len(student)
index=0
less=0
greater=0
while index<total:
    if student[index]<10:
        less=less+1
    else:
        greater=greater+1
    index=index+1
print less
print greater

