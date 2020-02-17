banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file_txt=open("file-question3.txt","w+")
i=0
while i<len(banks_list):
    a=banks_list[i]+"\n"
    file_txt.write(a)
    i=i+1
file_txt.close()  


file1=open("file-question3.txt","r+")
file=file1.read()
print file
file1.close()
