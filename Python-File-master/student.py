students=["neha","aman","ekta","naina","nikki"]
students_file=open("name.html","w+")
students_file.write("<html>\n")
students_file.write("<head>\n")
students_file.write("<title> Different names</title>\n")
students_file.write("</head>\n")
students_file.write("<body>\n")
students_file.write("<ul>\n")
for student in students:
    students_file.write("<li>"+student+"</li>\n")
students_file.write("</ul>\n")
students_file.write("</body>\n")
students_file.write("<html>") 


students_file=open("name.html","r+")
stud=students_file.read()
print stud
students_file.close()
