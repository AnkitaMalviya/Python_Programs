print"water consumed(in gallons)"
print"enter water consumed"
consumed_water=input()
if consumed_water>=45 and consumed_water<=75:
    print"Tax rate","=",475.00
elif consumed_water>75 and consumed_water<=125:
    print"Tax rate","=",750.00
elif consumed_water>125 and consumed_water<=200:
    print"Tax rate","=",1225.00
elif consumed_water>200 and consumed_water<=350:
    print"Tax rate","=",1650.00
elif consumed_water>350:
    print"Tax rate","=",2000.00  