userInput=input("enter your number")
user = userInput
sumNum = 0
while user>0:
    a=user%10
    sumNum = sumNum+a**3
    user = user/10  
               
print (sumNum) 
if userInput==sumNum:
    print(userInput,"armstrong number")
else:
    print("not" )          