with open("file1.txt","r") as file_txt:
    while True:
        file=file_txt.readline()
        if len(file)==1:
            break
        print file
file_txt.close()   
