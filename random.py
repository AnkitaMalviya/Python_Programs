import random
s = random.randrange(1, 5)
p = input("enter a no : ")
while(s!=p):
	print ("same nahi hai")
	s = random.randrange(1, 5)
	p = input("enter a no : ")	
print ("same hai")
