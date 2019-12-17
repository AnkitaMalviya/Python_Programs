char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
index=0
new=[]
while index <len(char_list):
    index2=0
    count=0
    while index2<len(char_list):
        if char_list[index]==char_list[index2]:
            count=count+1
        index2=index2+1
    if [char_list[index],count] not in new:
        new.append([char_list[index],count])  
    index=index+1
print new    

