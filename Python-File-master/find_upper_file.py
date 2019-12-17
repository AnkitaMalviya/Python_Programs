file_txt=open("find_upper_file.txt","r")
file=file_txt.read()
i=0
count=0
while i<len(file):
    if file[i].isupper():
        count=count+1
    i=i+1
print count
file_txt.close()

