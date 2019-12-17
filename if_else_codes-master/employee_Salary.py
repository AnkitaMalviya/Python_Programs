print"employee salary information"
salary=5000
print"enter your year"
year=input()
if year>=3:
    print"@you get discount@"
    print"year","=",year
    discount=salary*10/100
    print "discount","=",discount
    total=salary+discount
    print"total_Salary","=",total
else:
    print "you not get discount"