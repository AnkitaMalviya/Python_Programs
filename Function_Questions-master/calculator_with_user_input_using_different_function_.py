def calculatorAdd(numberx,numbery,operation):
    if operation=="add":
        return numberx+numbery
def calculatorSub(numberx,numbery,operation):
    if operation=="substract":
        return numberx-numbery
def calculatorDiv(numberx,numbery,operation):
    if operation=="divide":
        return numberx/numbery
def calculatorMul(numberx,numbery,operation):
    if operation=="multiply":
        return numberx*numbery
index=0
while index<2:
    Calculator1=int(raw_input("enter your number"))
    if index==0:
        a=Calculator1
    else:
        b=Calculator1
    index=index+1
add_result=calculatorAdd(a,b,"add")
print"add","=",(add_result)
substract_result=calculatorSub(a,b,"substract")
print "substract","=", (substract_result)
multiply_result=calculatorMul(a,b,"multiply")
print"multiply","=", (multiply_result)
divide_result= calculatorDiv(a,b,"divide")
print"divide","=", (divide_result)
