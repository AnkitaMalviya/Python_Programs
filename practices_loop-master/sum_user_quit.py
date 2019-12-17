#In this program if user input 4 then sum all numbers from starting to ending. if user input quit then program exit"

user=raw_input("enter your number")
index=1
var1=0
while index<=user:
    if user=="quit":
        break 
    user=int(user)
    if index<=user:
        var1=var1+index
    index=index+1
if var1!=0:
    print var1 
