file_txt=open("people1-exercise.txt","r")
file=file_txt.readlines()
i=0
count=0
while i<len(file):
    count=count+1
    i=i+1
print count 
file_txt.close()