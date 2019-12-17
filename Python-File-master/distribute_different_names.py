delhi_txt=open("question3.txt","r+")
file=delhi_txt.readlines()
index=0
new=[]
while index<len(file):
    j=0
    while j<len(file):
        if file[index][j]=="delhi":
            new.append(file[index][j])
        j=j+1
    index=index+1
print new
delhi_txt.close()


