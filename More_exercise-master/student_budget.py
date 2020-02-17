print"enter your student quantity="
student=int(raw_input())
print "enter your student kharcha="
student_ka_kharcha=int(raw_input())
index=0
total_Budget=0
while index<student:
    total_Budget=total_Budget+student_ka_kharcha
    index=index+1
print "all student ka budget=",total_Budget
if total_Budget<=50000:
    print"budget ke andar"
else:
    print"budget ke bahar"




# user=int(raw_input("number of student"))
# user1=int(raw_input("enter a kharcha"))
# index=0
# var=user*user1 
# print var
# if var<=50000:
# 	print"budget ke under"
# else:
# 	print"budget ke baher" 
