def Calculator(numberx,numbery,operation):
        if operation=="add":
            return numberx+numbery
        elif operation=="substract":
            return numberx-numbery
        elif operation=="divide":
            return numberx/numbery
        else:
            return numberx*numbery
number1=Calculator(20,25,"add")
print number1
number2=Calculator(40,3,"substract")
print number2
number3=Calculator(10,4,"multiply")
print number3
number4= Calculator(40,4,"divide")
print number4
    