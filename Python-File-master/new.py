file_txt=open("new.txt","w")
file_txt.write("hjuygffghjkxcvhjkjhgfdfghjkhgfghj")
file_txt.close() 


file_txt1=open("new.txt","r")
file1=file_txt1.read()
file_txt1.close()

file_txt2=open("new2.txt","w")
file_txt2.write(file1)
file_txt2.close() 