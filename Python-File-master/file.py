file_txt=open("file_1.txt","w+")
file_txt.write("nehhsfgbdshhiy;shlvh")
file_txt.write("\n yaha maine kuch aur bhi likha.")
file_txt.close()

file=open("file_1.txt","r+")
print(file.read())
file.close()