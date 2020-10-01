#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
#Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
student=raw_input("enter your choice Y and N=")
if student=="Y":
  print("you are able to give exam")
  print("no of classes held")
  held=input()
  print"no of classes attendence"
  attendence=input()
  total=100*attendence/held
  print"attendence",total
  if total>=75:
    print("you are allowed for exam")
  else:
    print("you are not allowed for exam")
else:
  print("you are not allowed to seat for exam")

