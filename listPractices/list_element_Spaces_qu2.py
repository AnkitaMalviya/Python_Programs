list = [15,13,33,2]
space=""
rem_space=""
new=[]
index=0
while index<len(list):
    if list[index]==list[0]:
        space=space+str(list[index])
        new.append(space)
    else:
        rem_space=rem_space+str(list[index])
        new.append(rem_space)
    index=index+1
new=space+rem_space
print new 