salary=5000
print"enter your year"
year=input()
if year>=3:
    print"year","=",year
    bonus=salary*10/100
    print"bonus","=",bonus
    total=salary+bonus
    bonus=total*year/3
    print"salary and bonus","=",bonus
else:
    print"you not get discount"
