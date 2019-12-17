user=input("enter type")
if type(user)==int:
	print int
elif type(user)==str:
	print str
elif type(user)==bool:
	print bool
elif type(user)==complex:
	print complex
elif type(user)==float:
	print float
else:
	print "do not match"