sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
index=0
new_list=[]
while index<len(sentence):
    index2=index
    str=" "
    while index2<len(sentence):
        if sentence[index2]==" ":
            break
        else:
            str=str+sentence[index2]
        index2=index2+1
    new_list.append(str)
    index=index2+1
print (new_list)



      
