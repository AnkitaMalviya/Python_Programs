string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
index=0
new=[]
while index<len(string_list):
    string=string_list[index]
    if string==string_list[index]:
        if string_list[index] not in new:
            new.append(string_list[index])
    index=index+1 
print new 
