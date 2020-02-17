my_name=open("name.txt","w+")
my_name.write("neha-israni\naman-israni\nekta-israni")
my_name.close()

my_name=open("name.txt","r+")
name=my_name.read()
print name
my_name.close()