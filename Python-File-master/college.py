college_file=open("collegesname.txt","w+")
college_file.write("jakatdar\nnutankanya\nprakash\nmahilasamaj\nlalbahadur shashtri")


college_file=open("collegesname.txt","r+")
clg=college_file.read()
print clg
college_file.close()
