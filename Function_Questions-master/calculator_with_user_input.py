def Calculator(numberx,numbery,operation):
        if operation=="add":
            return numberx+numbery
        elif operation=="substract":
            return numberx-numbery
        elif operation=="divide":
            return numberx/numbery
        else:
            return numberx*numbery 
index=0
while index<2:
    Calculator1=int(raw_input("enter your number"))
    if index==0:
        a=Calculator1
    else:
        b=Calculator1
    index=index+1
add_result=Calculator(a,b,"add")
print"add","=",(add_result) 
substract_result=Calculator(a,b,"substract")
print "substract","=", (substract_result)
multiply_result=Calculator(a,b,"multiply")
print"multiply","=", (multiply_result)
divide_result= Calculator(a,b,"divide")
print"divide","=", (divide_result)
