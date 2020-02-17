banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file_txt=open("file-question3.txt","w")
i=0
while i<len(banks_list):
    file_txt.write(banks_list[i]+"\n")
    i=i+1
file_txt.close()
