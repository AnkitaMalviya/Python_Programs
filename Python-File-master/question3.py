file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("other.txt","w")
file_txt=open("question3.txt","r+")
file=file_txt.readlines()
i=0
while i<len(file):
    if "delhi" in file[i]:
        file1.write(file[i])
    elif "shimla" in file[i]:
        file2.write(file[i])
    else:
        file3.write(file[i])
    i=i+1
file_txt.close
file1.close()
file2.close()
file3.close()


